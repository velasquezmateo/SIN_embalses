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
embalses_listado=pd.read_sql('SELECT * FROM embalses.listado_embalses',engine)
precio_bolsa=pd.read_sql('SELECT * FROM embalses.precio_bolsa',engine)

#Fecha actual
fecha_actual=aportes_caudal['date'].max()

volumen_util['date']=pd.to_datetime(volumen_util['date'],yearfirst=True)
vol_actual=volumen_util[volumen_util['date']=='2026-03-03'].sort_values(by='value', ascending=False)
vol_actual['value']=vol_actual['value']*100
vol_actual['name']=vol_actual['name'].str.replace('AGREGADO BOGOTA', 'AGR. BOGOTA')
volumen_util['name']=volumen_util['name'].str.replace('AGREGADO BOGOTA', 'AGR. BOGOTA')

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
plt.legend(loc='upper center',shadow=True,fontsize=12)
plt.xticks(rotation=45,ha='right',fontsize=7)
plt.ylabel('Volumen útil diario (%)',fontweight='bold')
plt.ylim(0,110)
plt.grid(alpha=0.20,axis='y')
sns.despine()
plt.show()'''

#Realizar comparativo entre caudal actual e histórico de los principales afluentes de los embalses
caudal_merged=pd.merge(aportes_caudal,caudal_med_histo,how='inner',on=['name','date'],suffixes=('_actual','_hist'))
caudal_merged=caudal_merged.drop(columns=['id_actual','id_hist'])
caudal_merged['date']=pd.to_datetime(caudal_merged['date'],yearfirst=True)
caudal_actual=caudal_merged[caudal_merged['date']==f'{fecha_actual}'].nlargest(n=20,columns='value_actual')

#Analizar histórico del río Sinú
'''caudal_urra=caudal_merged[caudal_merged['name']=='SINU URRA']
sns.lineplot(data=caudal_urra,x='date',y='value_actual',
             color='skyblue',label='Caudal Sinú-Urrá')
sns.lineplot(data=caudal_urra,x='date',y='value_hist',linestyle='--',
             label='Promedio histórico de caudal',color='royalblue')
#Sombrear area bajo la curva
plt.fill_between(caudal_urra['date'], caudal_urra['value_actual'], color='skyblue', alpha=0.2)
plt.title('Caudal del río Sinú (diario)',fontsize=18)
plt.xlabel('Tiempo',fontsize=12,fontweight='bold')
plt.ylabel('Promedio caudal (m3/s)',fontsize=12,fontweight='bold')
plt.legend(shadow=True,loc='upper center',fontsize=12)
plt.xticks(rotation=45)
plt.xlim(caudal_urra['date'].min(),caudal_urra['date'].max())
plt.ylim(0,None)
plt.grid(alpha=0.20,axis='y')
sns.despine()
plt.show()'''

colors2=['#d32f2f' if actual >=hist else '#00f5b4'
         for actual,hist in zip(caudal_actual['value_actual'],caudal_actual['value_hist'])]

'''bar_caudal=sns.barplot(data=caudal_actual,x='name',y='value_actual',palette=colors2)
line_hist=sns.lineplot(data=caudal_actual,x='name',y='value_hist',
                       color='black',marker='o',linestyle='--',label='Promedio histórico')

for c in bar_caudal.containers:
    label=bar_caudal.bar_label(c,
                               fmt='%.2f',
                               label_type='edge',
                               padding=3,
                               fontsize=9
                               )
    for l in label:
        l.set_rotation(45)

plt.title('Comparación de caudal frente a la media histórica',fontsize=12)
plt.suptitle(f'Caudal actual de los principales ríos para el {fecha_actual}',fontsize=18,fontweight='bold',y=0.95)
plt.xticks(rotation=45,fontsize=7,ha='right')
plt.ylabel('Caudal (m3/s)',fontweight='bold')
plt.legend(loc='upper center')
plt.grid(alpha=0.20,axis='y')
sns.despine()
plt.show()
'''
vertimientos['date']=pd.to_datetime(vertimientos['date'],yearfirst=True)
grouped=vertimientos.groupby(['date','name'])['value'].sum().reset_index()
embalses=grouped[grouped['name'].isin(['ITUANGO','URRA1','TOPOCORO'])]
embalses_grouped=embalses.pivot_table(index='date',columns='name',values='value',aggfunc='sum').fillna(0)
embalses_grouped=embalses_grouped.reset_index()

'''sns.lineplot(data=embalses_grouped,x='date',y='URRA1',
             color='royalblue',label='Vertimiento embalse Urrá 1')
sns.lineplot(data=embalses_grouped,x='date',y='ITUANGO',
             color='skyblue',label='Vertimiento embalse Hidroituango')
plt.fill_between(embalses_grouped['date'], embalses_grouped['URRA1'],
                 color='royalblue', alpha=0.2)
plt.fill_between(embalses_grouped['date'], embalses_grouped['ITUANGO'],
                 color='skyblue', alpha=0.2)
plt.title('Serie de tiempo vertimientos en embalses Hidroituango y Urrá 1 (diario)',fontsize=18,fontweight='bold')
plt.xlabel('Tiempo',fontsize=12,fontweight='bold')
plt.ylabel('Volumen de agua (m3)',fontsize=12,fontweight='bold')
plt.legend(loc='upper center',shadow=True,fontsize=12)
plt.xlim(embalses_grouped['date'].min(),embalses_grouped['date'].max())
plt.ylim(0,None)
plt.xticks(rotation=45)
plt.grid(alpha=0.20,axis='y')
sns.despine()
plt.show()'''

# Fusionar volumen útil y listado de embalses
embalses_listado=embalses_listado.drop(columns='date')
embalses_listado=embalses_listado.rename(columns={'values_name':'name'})
embalses_regiones=pd.merge(volumen_util,embalses_listado,how='left',on='name')
embalses_regiones=embalses_regiones.drop(columns=['id_x','id_y'])
regiones_grouped=embalses_regiones.groupby(['date','values_hydroregion'])['value'].mean().reset_index()
regiones_pivot=regiones_grouped.pivot(index='date',columns='values_hydroregion',values='value')
regiones_pivot=regiones_pivot.reset_index()

'''sns.lineplot(data=regiones_pivot,x='date',y='ANTIOQUIA',color='green')
sns.lineplot(data=regiones_pivot,x='date',y='CALDAS',color='blue')
sns.lineplot(data=regiones_pivot,x='date',y='CENTRO',color='red')
sns.lineplot(data=regiones_pivot,x='date',y='ORIENTE',color='black')
sns.lineplot(data=regiones_pivot,x='date',y='CARIBE',color='orange')
plt.show()'''

#Analizar precio de bolsa con volumen útil
precio_bolsa['date']=pd.to_datetime(precio_bolsa['date'],yearfirst=True)
#Agrupar para igual granularidad con las otras variables
precio_bolsa_grouped=precio_bolsa.groupby('date').agg({'valor':'mean'}).reset_index()
#Agrupar volumen diario (Promedio Nacional Diario)
volumen_diario=volumen_util.groupby('date')['value'].mean().reset_index()

#Fusionar precio de bolsa con volumen útil
precio_volumen=pd.merge(precio_bolsa_grouped,volumen_diario,how='inner',on='date')
precio_volumen['precio_7d']=precio_volumen['valor'].rolling(window=7,min_periods=1).mean()
precio_volumen['volumen_7d']=precio_volumen['value'].rolling(window=7,min_periods=1).mean()


#Graficar la correlación entre el precio y el volumen útil de los embalses
fig, ax1= plt.subplots(figsize=(12,8))

ax1.plot(precio_volumen['date'],precio_volumen['volumen_7d'],
         color='steelblue',label='Volumen útil (Suavizado)',alpha=0.8)
ax1.fill_between(x=precio_volumen['date'],y1=precio_volumen['volumen_7d'],color='skyblue',alpha=0.1)
ax1.set_ylabel('Nivel de Volumen Útil Nacional (%)',fontsize=12)
ax1.set_xlim(precio_volumen['date'].min(),precio_volumen['date'].max())
ax1.set_ylim(0,1)


#Graficar segundo eje Y
ax2=ax1.twinx()
ax2.plot(precio_volumen['date'],precio_volumen['precio_7d'],
         color='olivedrab',label='Precio de bolsa (Suavizado)',linewidth=1.5)
ax2.set_ylabel('Precio de bolsa (COP/kWh)',fontsize=12)
ax2.set_xlim(precio_volumen['date'].min(),precio_volumen['date'].max())
ax2.set_ylim(0,precio_volumen['precio_7d'].max()*1.1)


plt.title('Divergencia Hídrico-Económica: Volumen Útil vs. Precio de Bolsa', fontsize=16, pad=20, fontweight='bold')
sns.despine()
plt.grid(axis='y',alpha=0.3,color='grey',linestyle='--')

plt.show()
