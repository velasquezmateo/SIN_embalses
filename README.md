<div align="center">
  <h1>Análisis de Resiliencia Energética</h1>
  <h3>Disparidad Hídrica y Volatilidad del Mercado Eléctrico en Colombia</h3>
</div>
Este proyecto documenta un análisis técnico profundo sobre la resiliencia del Sistema Interconectado Nacional (SIN) de Colombia entre 2023 y 2026. A través de un pipeline de datos sencillo pero escalable, se explora cómo la disparidad hídrica regional y eventos operativos críticos dictan el precio de la energía en el país y su dependencia en materia del recurso hídrico para abastecer a la población nacional de energía. <br>

<div align="center">
<h2>🚀Descripción del Proyecto</h2>
</div>
Colombia posee una matriz energética cuya columna vertebral es la generación hidroeléctrica (aproximadamente el 70% de la capacidad instalada). Esta dependencia crea un ecosistema donde la seguridad energética del país no solo depende de la infraestructura, sino de la variabilidad climática y la gestión geográfica del agua.<br>
Este proyecto nace de la necesidad de analizar la resiliencia del Sistema Interconectado Nacional (SIN) frente a fenómenos climáticos extremos, conocer cómo se encuentra el estado actual del recurso hídrico y algunas disparidades operativas regionales entre los años 2023 y 2026.

<div align="center">
<h2>Objetivos</h2>
</div>
El objetivo principal es transformar datos crudos de XM y reportes de la Superservicios en información estratégica. Mediante el uso de técnicas avanzadas de procesamiento de datos y visualización, este repositorio se esmera en mostrar el estado actual de los embalses, su comportamiento frente al promedio histórico y algunos eventos extremos que evidencian la vulnerabilidad del sistema frente a eventos atmosféricos extremos como el Niño y la Niña.<br>
Por otro lado, se enfoca en mostrar la correlación entre las variables físicas (caudales, niveles de embalse) y las variables económicas (precios marginales del mercado) con el propósito de evaluar la reacción del precio en pesos por kWh frente a lo reportado por XM.<br>

<div align="center">
<h2>🛠️ Stack Tecnológico</h2>
</div>
<p align="center">
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />
<img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />
<img src="https://img.shields.io/badge/Seaborn-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Seaborn" />
</p>

<div align="center">
<h2>📥 Adquisición y Preparación de Datos</h2>
</div>

XM (Administrador del Mercado): Extracción de series de tiempo diarias de:<br>
-**Aportes Hídricos**: Valores de la hidrologia de los caudales de los rios del SIN, en metros cubicos por segundo<br>
-**Vertimientos**:Los vertimientos en m3 están relacionados con la cantidad de agua que debe ser evacuada en los embalses cuando la reserva sobrepasa la capacidad maxima de almacenamiento.<br>
-**Volumen Útil**: Porcentaje de volumen almacenado en el embalse por encima del Nivel Mínimo Técnico<br>
-**Caudal Medio Histórico**: Caudal medio mensual histórico para los rios del SIN, obtenido como el promedio de los valores de cada mes para todos años con información disponibles.<br>
-**Porcentaje de aportes**: [Aportes Caudal / Media Histórica]*100<br>
-**Listado embalses**: Listado de embalses que se encuentran registrados ante el CND y que son reportados por algún recurso del SIN<br>
-**Precio de Bolsa**: Precio de oferta de la última planta flexible para atender la demanda comercial nacional, más delta de incremento para remunerar los costos no cubiertos de las plantas térmicas en el despacho ideal<br>

<div align="center">
<h2>📝 Enfoque Metodológico y Tratamiento de Series de Tiempo</h2>
</div>

El siguiente análisis desglosa un sistema de embudo que permite generar un panorama desde lo macro hasta la situación actual de la matriz energética nacional:<br>

1. **Volumen de los embalses vs precio energético**:

<div align="center">
<img width="1351" height="698" alt="4" src="https://github.com/user-attachments/assets/9dde4877-0b0e-47c4-bcae-529e6eb8e5a5" />
</div>

Para comprender la correlación entre estas dos variables, se debe calcular el coeficiente de correlación y probar si existe significancia estadística. Se muestra a continuación un gráfico de dispersión que ajusta una línea para conocer su tendencia:<br>

<div align="center">
<img width="1536" height="754" alt="5" src="https://github.com/user-attachments/assets/5cf4cd7a-8f09-4546-85b8-5c36926a80f6" />
</div>

Luego de conocer su tendencia, se calcula si existe una correlación marcada o ligera entre estas dos características:<br>

Coeficiente de Spearman (ρ=−0.474): Existe una correlación negativa moderada. El signo negativo confirma la teoría: cuando el volumen de los embalses baja, el precio tiende a subir.<br>
Sin embargo, esto no asevera que la relación sea lineal, existen otros factores que influyen en el precio final por kWh, como la generación de energía por centrales termoeléctricas, demanda y políticas públicas que, combinados, explicarían mucho más la precisión del precio.<br>
De hecho, durante el 2024 Colombia vivió un fenómeno del Niño extremo durante la temporada seca que generó una drástica disminución del volumen útil de los embalses, lo cual preocupó a la nación y generó anomalías en los precios a finales del mismo año hacia cotas mayores a 2000 COP/kWh.<br>

Ahora bien, surge una pregunta: ¿a nivel nacional los diferentes embalses ubicados en diversas zonas geográficas aportan volumen hídrico de manera similar o se presentan disparidades causadas por el clima regional?<br>

<div align="left">
<h2>🌎 Disparidad Regional: La Geografía del Estrés Hídrico</h2>
</div>

El análisis de participación relativa (Percent Stacked Area) revela que la seguridad energética de Colombia depende de una estructura hídrica profundamente desigual.<br>
<div align="center">
<img width="1296" height="684" alt="3" src="https://github.com/user-attachments/assets/b0acb1d3-4167-403b-89c2-571c08d953a6" />
</div>

**Impacto en el Precio**: Cuando estas regiones reducen su área en el gráfico, el sistema pierde su capacidad de regulación rápida. Aunque el volumen nacional parezca estable, el agotamiento en cuencas específicas como ORIENTE y VALLE pueden aumentar los precios de bolsa, ya que el sistema debe recurrir a plantas térmicas locales para suplir la demanda de estos nodos. En contraste, regiones como ANTIOQUIA, CALDAS CARIBE Y CENTRO registran una relativa estabilidad de captación de agua para hidroeléctricas en los períodos entre 2023-2026.<br>

<div align="left">
<h2>📈 Análisis de Actualidad</h2>
</div>

Para comprobar la robustez del análisis, se contrastaron los hallazgos históricos con el estado del Sistema Interconectado Nacional (SIN) al 3 de marzo de 2026. Los datos actuales confirman la persistencia de la paradoja hídrica:<br>

<div align="center">
<img width="1536" height="754" alt="6" src="https://github.com/user-attachments/assets/4a6cf780-749b-48f1-b2f6-adebe7e74a41" />
</div>

**Calima1** (97.86%) y **Topocoro** (96.59%) lideran el exceso de almacenamiento.
<br>
**Urrá 1** (85.60%) y **Ituango** (92.60%) se mantienen en la zona de alerta naranja/roja.
<br>
**Conclusión**: La alta concentración de agua en estos nodos obliga a una vigilancia operativa extrema. Como se analizó previamente, los aportes atípicos (como los del río Sinú) generan una presión que el sistema nacional no puede redistribuir, resultando en vertimientos técnicos a pesar de la demanda.
<br>
Se muestra a continuación un gráfico que resume las causas del estado actual de los niveles extremos de los embalses, tanto positivos como negativos:

<div align="left">
<h2>Superavit crítico vs déficit local</h2>
</div>
<div align="center">
<img width="1536" height="754" alt="7" src="https://github.com/user-attachments/assets/8d2110f8-7f55-4f4a-b4d2-7c17fc5cd5d0" />
</div>

Exceso en el Norte y Occidente: Ríos como el Cauca (1296.42m3/s) y el Sinú (Urrá) presentan caudales significativamente superiores a su media histórica. Esto ha llevado a que embalses como Ituango (92.60%) y Urrá (96.59%) superen el Umbral Crítico de Seguridad.
<br>
Cuando los embalses se encuentran en cotas cercanas al 100%, deben realizarse vertimientos forzosos para proteger la infraestructura. Como consecuencia se genera un aumento significativo en los caudales ríos abajo, que en casos tan extremos como los ocurridos en el embalse Sinú Urrá I, genera desplazamientos y pérdidas económicas en sectores como la agricultura y la ganadería.<br>

<div align="left">
<h2>La Anomalía Operativa en Urrá I</h2>
</div>
<div align="center">
<img width="1536" height="754" alt="8" src="https://github.com/user-attachments/assets/0855c9c6-34ec-4803-a499-dcc0cebd8d3d" />
</div>

Durante los últimos años, la gráfica de arriba demuestra que existen picos cada vez más elevados que se ubican en los meses de mayo y junio. Estos gráficos abren la puerta para que se enfatice en realizar modelos predictivos que prevengan escenarios como los ocurridos a principios del años 2026. Por ende, La anomalía de Urrá demuestra que la resiliencia energética no se logra solo con lluvia, sino con capacidad de almacenamiento y flexibilidad en la red. Es preferible desplazar generación térmica (costosa y contaminante) para dar paso a la hidroeléctrica que está en riesgo de verter, aprovechando cada m³ de agua antes de que se pierda por el rebosadero. pero tampoco se trata solo de "abrir las compuertas" cuando el embalse está a punto de rebosar, sino de una gestión inteligente que combine ingeniería, predicción de datos y política social que anticipen estos escenarios ante los fenómenos climáticos que se suceden actualmente para establecer si se requiere una expansión física de la represa que garantice la seguridad en las regiones que viven dentro de la cuenca y la estabilidad del mercado.



**Riesgo de Racionamiento Local**: Aunque el país "tenga agua" en el norte, la incapacidad de trasvasar esa energía de forma eficiente hacia el sur pone en riesgo la continuidad del servicio en nodos críticos, afectando hospitales, escuelas e industria local.








