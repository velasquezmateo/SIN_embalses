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

Para comprender la correlación entre estas dos variables, se debe calcular el coeficiente de correlación y probar si existe significancia estadística. Se muestra a continuación un gráfico de regresión que ajusta una línea para conocer su tendencia:<br>

<div align="center">
<img width="1536" height="754" alt="5" src="https://github.com/user-attachments/assets/5cf4cd7a-8f09-4546-85b8-5c36926a80f6" />
</div>

Luego de conocer su tendencia, se calcula si existe una correlación marcada o ligera entre estas dos características:<br>

Coeficiente de Spearman (ρ=−0.474): Existe una correlación negativa moderada. El signo negativo confirma la teoría: cuando el volumen de los embalses baja, el precio tiende a subir.<br>
Sin embargo, esto no asevera que la relación sea lineal, existen otros factores que influyen en el precio final por kWh, como la generación de energía por centrales termoeléctricas, demanda y políticas públicas que, combinados, explicarían mucho más la precisión del precio.<br>
De hecho, durante el 2024 Colombia vivió un fenómeno del Niño extremo que generó una drástica disminución del volumen útil de los embalses, lo cual preocupó a la sociedad y generó anomalías en los precios a finales del mismo año hacia cotas mayores a 2000 COP/kWh.<br>

Ahora bien, surge una pregunta: ¿a nivel nacional los diferentes embalses ubicados en diversas zonas geográficas aportan volumen hídrico de manera similar o se presentan disparidades causadas por el clima regional?<br>

<div align="left">
<h2>🌎 Disparidad Regional: La Geografía del Estrés Hídrico</h2>
</div>

El análisis de participación relativa (Percent Stacked Area) revela que la seguridad energética de Colombia depende de una estructura hídrica profundamente desigual.<br>
<div align="center">
<img width="1296" height="684" alt="3" src="https://github.com/user-attachments/assets/b0acb1d3-4167-403b-89c2-571c08d953a6" />
</div>

**Impacto en el Precio**: Cuando estas regiones reducen su área en el gráfico, el sistema pierde su capacidad de regulación rápida. Aunque el volumen nacional parezca estable, el agotamiento en estas cuencas específicas dispara los precios de bolsa, ya que el sistema debe recurrir a plantas térmicas locales para suplir la demanda de estos nodos.<br>









