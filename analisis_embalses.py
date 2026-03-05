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
vol_actual['value']=vol_actual['value']*100
vol_actual['name']=vol_actual['name'].str.replace('AGREGADO BOGOTA', 'AGR. BOGOTA')

#Establecer umbral de capacidad
colors=['#d32f2f' if x >=95 else '#f57c00' if x >=85 else '#1976d2' for x in vol_actual['value']]

#Gráfico volumen útil actual
sns.set_theme(style="white")
fig, ax = plt.subplots(figsize=(12, 8))
bar=sns.barplot(vol_actual,x='name',y='value',palette=colors)

for c in bar.containers:
    labels=bar.bar_label(c,
                        fmt='%.2f%%',
                        label_type='edge',
                        padding=3)
    for l in labels:
        l.set_rotation(45)

ax.set_title('Porcentaje de volumen útil diario reportado al SIN',fontsize=18,fontweight='bold')
plt.axhline(95,linestyle='--',color='black',linewidth=1,alpha=0.25,label='Umbral Crítico (95%)')
plt.axhline(85,linestyle='--',color='black',linewidth=1,alpha=0.25,label='Alerta (85%)')
plt.legend(loc='upper center',shadow=True)
plt.xticks(rotation=45)
plt.ylabel('Volumen útil diario (%)',fontweight='bold')
plt.xlabel('Embalses', fontweight='bold')
plt.ylim(0,110)
sns.despine()
plt.tight_layout()
plt.show()

