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

#Fecha actual
fecha_actual=aportes_caudal['date'].max()


volumen_util['date']=pd.to_datetime(volumen_util['date'],yearfirst=True)
vol_actual=volumen_util[volumen_util['date']=='2026-03-03'].sort_values(by='value', ascending=False)
vol_actual['value']=vol_actual['value']*100
vol_actual['name']=vol_actual['name'].str.replace('AGREGADO BOGOTA', 'AGR. BOGOTA')

#Establecer umbral de capacidad para volumen útil diario
colors=['#d32f2f' if x >=95 else '#f57c00' if x >=85 else '#1976d2' for x in vol_actual['value']]

#Gráfico volumen útil actual
'''sns.set_theme(style="white")
fig, ax = plt.subplots(figsize=(12, 8))
bar=sns.barplot(vol_actual,x='name',y='value',palette=colors)

for c in bar.containers:
    labels=bar.bar_label(c,
                        fmt='%.2f%%',
                        label_type='edge',
                        padding=3)
    for l in labels:
        l.set_rotation(45)

ax.set_title(f'Porcentaje de volumen útil diario reportado al SIN para el {fecha_actual}',fontsize=18,fontweight='bold')
plt.axhline(95,linestyle='--',color='#d32f2f',linewidth=1,label='Umbral Crítico (95%)')
plt.axhline(85,linestyle='--',color='#f57c00',linewidth=1,label='Alerta (85%)')
plt.legend(loc='upper center',shadow=True)
plt.xticks(rotation=45,ha='right',fontsize=7)
plt.ylabel('Volumen útil diario (%)',fontweight='bold')
plt.ylim(0,110)
sns.despine()
plt.show()'''

#Realizar comparativo entre caudal actual e histórico de los principales afluentes de los embalses
caudal_merged=pd.merge(aportes_caudal,caudal_med_histo,how='inner',on=['name','date'],suffixes=('_actual','_hist'))
caudal_merged=caudal_merged.drop(columns=['id_actual','id_hist'])
caudal_merged['date']=pd.to_datetime(caudal_merged['date'],yearfirst=True)
caudal_actual=caudal_merged[caudal_merged['date']=='2026-03-03'].nlargest(n=20,columns='value_actual')


'''colors2=['#d32f2f' if actual >=hist else '#00f5b4'
         for actual,hist in zip(caudal_actual['value_actual'],caudal_actual['value_hist'])]

bar_caudal=sns.barplot(data=caudal_actual,x='name',y='value_actual',palette=colors2)
line_hist=sns.lineplot(data=caudal_actual,x='name',y='value_hist',color='black',marker='o',linestyle='--',label='Promedio histórico')

for c in bar_caudal.containers:
    label=bar_caudal.bar_label(c,
                               fmt='%.2f',
                               label_type='edge',
                               padding=3,
                               fontsize=9
                               )
    for l in label:
        l.set_rotation(45)

plt.title('Comparación frente a la media histórica',fontsize=12)
plt.suptitle(f'Caudal actual de los principales ríos para el {fecha_actual}',fontsize=18,fontweight='bold',y=0.95)
plt.xticks(rotation=45,fontsize=7,ha='right')
plt.ylabel('Caudal (m3/s)',fontweight='bold')
plt.legend(loc='upper center')
sns.despine()
plt.show()'''

vertimientos['date']=pd.to_datetime(vertimientos['date'],yearfirst=True)
vertimientos['mes']=vertimientos['date'].dt.month
vertimientos['nombre_mes']=vertimientos['date'].dt.month_name(locale='Spanish')
grouped=vertimientos.groupby(['date','name'])['value'].sum().reset_index()
embalses=vertimientos[vertimientos['name'].isin(['ITUANGO','URRA1'])]
embalses_name=vertimientos['name'].unique().tolist()

plt.stackplot(vertimientos['date'],embalses,labels=embalses_name)
plt.show()