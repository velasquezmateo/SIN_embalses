# Importación de datos desde la API de XM
import datetime
from sqlalchemy import create_engine
from pydataxm.pydatasimem import CatalogSIMEM
import pydataxm.pydataxm as api
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', 1000)  # Ajustar el ancho de la consola

# Crear una instancia de catalogo con el tip
catalogo_conjuntos = CatalogSIMEM('Datasets')
api=api.ReadDB()

#Aquí se aloja la información del conjunto de datos incluyendo el comienzo de registros hasta su final
df=catalogo_conjuntos.get_data()
conjunto_datos=df[df['nombreConjuntoDatos'].str.lower().str.contains('embalse')]

#Aquí se encuentran las métricas o códigos para obtener los datos (No es el ID)
metrica=api.get_collections()
metric_description=metrica[metrica['MetricName'].str.lower().str.contains('aporte')]   #Filtrar nombres de tablas por palabra clave

fecha_inicio=datetime.date(2023,1,1)
fecha_fin=datetime.date(2026,3,3)

porc_apor=api.request_data('PorcApor','Sistema',fecha_inicio,fecha_fin)
#[Aportes Caudal / Media Histórica]*100

apor_caudal=api.request_data('AporCaudal','Rio',fecha_inicio,fecha_fin)
#Valores de la hidrologia de los caudales de los rios del SIN, en metros cubicos por segundo
apor_caudal=apor_caudal.drop(columns='Id')
apor_caudal.columns=[c.lower() for c in apor_caudal.columns]

vert_masa=api.request_data('VertMasa','Embalse',fecha_inicio,fecha_fin)
#Los vertimientos en m3 están relacionados con la cantidad de agua que debe ser evacuada en los embalses cuando la reserva
# sobrepasa la capacidad maxima de almacenamiento.
vert_masa=vert_masa.drop(columns='Id')
vert_masa.columns=[c.lower() for c in vert_masa.columns]

vol_util=api.request_data('PorcVoluUtilDiar','Embalse',fecha_inicio,fecha_fin)
#Porcentaje de volumen almacenado en el embalse por encima del Nivel Mínimo Técnico
vol_util=vol_util.drop(columns='Id')
vol_util.columns=[c.lower() for c in vol_util.columns]

caudal_med_hist=api.request_data('AporCaudalMediHist','Rio',fecha_inicio,fecha_fin)
#Caudal medio mensual histórico para los rios del SIN, obtenido como el promedio de los valores de cada mes para todos
# años con información disponibles
caudal_med_hist=caudal_med_hist.drop(columns='Id')
caudal_med_hist.columns=[c.lower() for c in caudal_med_hist.columns]

porc_apor=api.request_data('PorcApor','Sistema',fecha_inicio,fecha_fin)
# [Aportes Caudal / Media Histórica]*100
porc_apor['Value']=round(porc_apor['Value']*100)
porc_apor=porc_apor.drop(columns='Id')
porc_apor.columns=[c.lower() for c in porc_apor.columns]

#Crear la conexión con la base de datos
user='postgres'
password=''
host='localhost'
puerto='5432'
database=''

#Crear motor de conexión
engine=create_engine(f'postgresql+psycopg://{user}:{password}@{host}/{database}')

#Enviar las tablas a PostgreSQL
apor_caudal.to_sql(name='aporte_caudal',
                   con=engine,
                   if_exists='append',
                   schema='embalses',
                   index=False)

vert_masa.to_sql(name='vertimientos',
                   con=engine,
                   if_exists='append',
                   schema='embalses',
                   index=False)
vol_util.to_sql(name='vol_util',
                   con=engine,
                   if_exists='append',
                   schema='embalses',
                   index=False)
caudal_med_hist.to_sql(name='caudal_med_hist',
                   con=engine,
                   if_exists='append',
                   schema='embalses',
                   index=False)
porc_apor.to_sql(name='porc_apor',
                   con=engine,
                   if_exists='append',
                   schema='embalses',
                   index=False)