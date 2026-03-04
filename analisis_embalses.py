import pandas as pd
from sqlalchemy import create_engine
import seaborn as sns
import matplotlib.pyplot as plt

#Crear la conexión con la base de datos
user='postgres'
password='postgres_caesar'
host='localhost'
puerto='5432'
database='postgres'

#Crear motor de conexión
engine=create_engine(f'postgresql+psycopg://{user}:{password}@{host}/{database}')

aportes_caudal=pd.read_sql('SELECT * FROM embalses.aporte_caudal',engine)
vertimientos=pd.read_sql('SELECT * FROM embalses.vertimientos',engine)
volumen_util=pd.read_sql('SELECT * FROM embalses.vol_util',engine)
porc_apor=pd.read_sql('SELECT * FROM embalses.porc_apor',engine)
caudal_med_histo=pd.read_sql('SELECT * FROM embalses.caudal_med_hist',engine)

volumen_util['date']=pd.to_datetime(volumen_util['date'],yearfirst=True)
vol_actual=volumen_util[volumen_util['date']=='2026-03-03'].sort_values(by='value', ascending=False)

#Gráfico volumen útil actual
ax=sns.barplot(vol_actual,x='name',y='value')
for c in ax.containers:
    labels=ax.bar_label(c,
                        fmt='%.2f%%',
                 label_type='edge',
                 padding=3)
    for l in labels:
        l.set_rotation(45)
plt.title('Porcentaje de volumen útil diario reportado al SIN')
plt.tight_layout()
plt.xticks(rotation=45)
plt.xlabel('Embalses')
plt.ylabel('Volumen útil diario (%)')
plt.ylim(0,1.1)
plt.show()

