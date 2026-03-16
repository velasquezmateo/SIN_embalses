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

En el contexto energético colombiano, la seguridad del suministro eléctrico está intrínsecamente ligada a la variabilidad hidrológica del país. Históricamente, Colombia ha consolidado una matriz de generación predominantemente hidroeléctrica, la cual representa aproximadamente el 70% de su capacidad instalada. Si bien Colombia es un país geográficamente privilegiado por sus vertientes hidrológicas que nacen mayoritariamente en la cordillera de los Andes, conlleva una vulnerabilidad estructural ante fenómenos de variabilidad climática, con la aparición de fenómenos como el Niño, lo que en últimas impacta en la producción energética y por ende el bolsillo de los usuarios. Para conocer la relación "agua-precio energía", se debe estudiar si existe alguna relación tangible entre ambas variables. Para esto, me he propuesto pasar de la teoría y centrarme en obtener los datos necesarios con el fin de cuantificar qué tanto golpea el bolsillo del colombiano la falta de lluvia, usando herramientas estadísticas para probar que la relación entre el nivel de los embalses y el precio de la energía no es una coincidencia, sino un patrón predecible."

<div align="center">
<img width="1536" height="754" alt="Image" src="https://github.com/user-attachments/assets/1bdb46bd-e598-4644-97c2-ba865f358db6" />
</div>

Primero, se debe evaluar si existe correlación que no sea fruto del azar, para esto se debe calcular el coeficiente de correlación y probar si existe significancia estadística. Se muestra a continuación un gráfico de dispersión que ajusta una línea para conocer su tendencia:<br>

<div align="center">
<img width="1536" height="754" alt="Image" src="https://github.com/user-attachments/assets/4da83633-6a41-44e4-b8f2-c401224bafb6" />
</div>

Luego de conocer su tendencia, se calcula si existe una correlación marcada o ligera entre estas dos características:<br>

**Coeficiente de Spearman (ρ=−0.474)**: Existe una correlación negativa moderada. El signo negativo confirma la teoría: cuando el volumen de los embalses baja, el precio tiende a subir.
<br>
**Significancia (p<0.05)**: El valor obtenido es casi cero. (Para ver el cálculo detallado de la correlación y el procesamiento de datos, consulta el script de Python:
[Análisis de Correlación Hídrica (Python)](./analisis_embalses.py)
<br>
Sin embargo, esto no asevera que la relación sea lineal, existen otros factores que influyen en el precio final por kWh, como la generación de energía por centrales termoeléctricas, demanda y políticas públicas que, combinados, explicarían mucho más la precisión del precio.<br>
De hecho, durante el 2024 Colombia vivió un fenómeno del Niño extremo durante la temporada seca de enero a marzo que generó una drástica disminución del volumen útil de los embalses a nivel nacional, lo cual preocupó a la nación y generó anomalías en los precios a finales del mismo año hacia cotas mayores a 2000 COP/kWh.
<br>
A esto se suma un acontecimiento que tomó por sorpresa a gran parte de la población: la pérdida de soberanía de abastecimiento de gas natural de Colombia. Una racha que se detuvo tras 50 años de suministro continuo, lo que obligó al Estado a importar el combustible.
Esta situación se agravó ante la falta de continuidad en la exploración y extracción de nuevos yacimientos como consecuencia de políticas anti fósiles del gobierno colombiano que desestimuló la inversión y llevó a que el capital busque mejores condiciones en otros países de la región, como Argentina y Guyana, que muestran elevadas tasas de crecimiento.
<br>
Con el panorama de la pérdida de soberanía de Colombia en extracción y suministro de gas y una paulatina importación de éste para suplir la demanda que requiere el sector industrial, comercial y los parques térmicos, el recurso hídrico cobra una mayor relevancia, ya que puede ser un gran contrapeso a las altas tarifas que ocasionaría tarde o temprano la importación del combustible fósil mencionado.

Ahora bien, aquí llegan preguntas indispensables:¿Qué tanto depende el sector energético del nivel de sus embalses para suministrar energía a todas las regiones del país? y ¿a nivel nacional los diferentes embalses ubicados en diversas zonas geográficas aportan volumen hídrico de manera similar o se presentan disparidades causadas por el clima regional?
<br>

<div align="left">
<h2>🌎 Disparidad Regional: La Geografía del Estrés Hídrico</h2>
</div>

El análisis de participación relativa (Percent Stacked Area) revela que la seguridad energética de Colombia depende de una estructura hídrica profundamente desigual.<br>
<div align="center">
<img width="1536" height="754" alt="Image" src="https://github.com/user-attachments/assets/e31e8cfa-b1d7-4c4d-bcdd-a0e154ce5b1a" />
</div>

**Impacto en el Precio**: Cuando estas regiones reducen su área en el gráfico, el sistema pierde su capacidad de regulación rápida. Aunque el volumen nacional parezca estable, el agotamiento en cuencas específicas como ORIENTE y VALLE pueden aumentar los precios de bolsa, ya que el sistema debe recurrir a plantas térmicas locales para suplir la demanda de estos nodos, lo que eleva el costo marginal de forma inmediata, independientemente de que el resto del país tenga los embalses llenos. En contraste, regiones como ANTIOQUIA, CALDAS CARIBE Y CENTRO registran una resiliencia de captación de agua para hidroeléctricas en los períodos entre 2023-2026.<br>
Como resultado, se establecen una serie de acciones con objetivos establecidos para mitigar los impactos tanto del aumento del caudal, como un déficit de éste:
<br>

**Fortalecimiento de la infraestructura**: Acelerar proyectos de conectividad desde regionescon alta capacidad de generación eléctrica hacia las que poseen un déficit marcado en un marco de tiempo establecido.<br>
**Generación de energías alternativas**: Que regiones como ORIENTE y VALLE reduzcan su dependencia de la hidroelectricidad local durante los meses de baja captación, permitiendo que sus embalses se recuperen más rápido, incentivando la instalación masiva de granjas solares y sistemas de almacenamiento en estas cuencas específicas. <br>
La verdadera seguridad energética de Colombia no vendrá de tener más agua, sino de tener más flexibilidad.<br>

<div align="left">
<h2>📈 Análisis de Actualidad</h2>
</div>

Para comprobar la robustez del análisis, se contrastaron los hallazgos históricos con el estado del Sistema Interconectado Nacional (SIN). Los datos actuales confirman la persistencia de la paradoja hídrica:<br>

<div align="center">
<img width="1536" height="754" alt="Image" src="https://github.com/user-attachments/assets/7fb8fc40-fc85-4c54-b7e2-32d4cca1186c" />
</div>

**Ituango** (101.76%) supera el 100%. El embalse vuelve a cruzar el umbral de capacidad porque el río CAUCA continúa muy por encima de su promedio histórico, generando vertimientos que ya los 24 días consecutivos.
<br>
**Chuza** (34.36%) y **Muña** (34.4%): dos de los embalses que surten de energía a la región centro del país registran niveles bajos. Los aportes naturales son ineficientes para mantener a cabo las actividades de generación energética a mediano plazo. El AGR. BOGOTA (56.87%) persiste con niveles más elevados para garantizar el suministro eléctrico.
<br>
Se muestra a continuación un gráfico que resume las causas del estado actual de los niveles extremos de los embalses, tanto positivos como negativos:

<div align="left">
<h2>Superavit crítico vs déficit local</h2>
</div>
<div align="center">
<img width="1536" height="754" alt="Image" src="https://github.com/user-attachments/assets/f8f8a800-a2a0-44d8-b7f9-8fbd04a16c1c" />
</div>

Exceso en el Norte y Suroccidente: Ríos como el **Cauca** enla represa de **HidroItuango**  (839.51m3/s) y en la represa **Salvajina** se presentan caudales significativamente superiores a su media histórica. Esto ha llevado a que estos embalses generen excedentes que no permiten ser convertidos en energía.<br>
**Guatapé** (20.23%) y **Miel I** cruzan por debajo de su nivel histórico promedio, mostrando una tendencia general en la moderación de sus aportes.
<br>
Cuando los embalses se encuentran en cotas cercanas al 100%, deben realizarse vertimientos forzosos para proteger la infraestructura. Como consecuencia se genera un aumento significativo en los caudales ríos abajo, que en casos tan extremos como los ocurridos en el embalse Sinú Urrá I, genera desplazamientos y pérdidas económicas en sectores como la agricultura y la ganadería.<br>

<div align="left">
<h2>🏞️ La Anomalía Operativa en Urrá I</h2>
</div>
<div align="center">
<img width="1536" height="754" alt="Image" src="https://github.com/user-attachments/assets/299dd3dd-4cf7-4ded-b0be-61d16406d88b" />
</div>

Durante los últimos años, la gráfica de arriba demuestra que existen picos cada vez más elevados que se ubican en los meses de mayo y junio. Además, el inicio de año que comprende los meses de enero, febrero y marzo suelen venir acompañados por valores decrecientes del caudal del río Sinú que surte al embalse en cuestión, mismo intervalo temporal que corresponde a la temporada seca y de muy pocas lluvias en Colombia. Sin embargo, el gráfico muestra que durante el mes de enero y febrero de 2026 se presentó un acontecimiento atípico que generó preocupación sobre la capacidad de resiliencia y de respuesta que se tiene a la hora de enfrentar escenarios donde el caudal puede ascender 5 veces más que su promedio histórico. Por ende, La anomalía de Urrá demuestra que la resiliencia energética no se logra solo con lluvia, sino con capacidad de almacenamiento y flexibilidad en la red. Es preferible desplazar generación térmica (costosa y contaminante) para dar paso a la hidroeléctrica que está en riesgo de verter, aprovechando cada m³ de agua antes de que se pierda por el rebosadero. pero tampoco se trata solo de "abrir las compuertas" cuando el embalse está a punto de rebosar, sino de una gestión inteligente que combine ingeniería, predicción de datos y política social que anticipen estos escenarios ante los fenómenos climáticos que se suceden actualmente para establecer si se requiere una expansión física de la represa que garantice la seguridad en las regiones que viven dentro de la cuenca y la estabilidad del mercado.
<br>
<div align="center">
<h2>Instalación y Uso</h2>
Si deseas contribuir y participar en este análisis, clona el repositorio a través de Git. Así, seguiremos construyendo una comunidad de analistas enfocada en brindar información actualizada a través de insights y proyecciones útiles para la toma de decisiones en el sector energético.

                            ```
                            git clone https://github.com/velasquezmateo/SIN_embalses.git
                            cd SIN_embalses
                            pip install -r requirements.txt
                            ```


<div align="center">
<h2>🏁 Insights</h2>
</div>

El análisis de resiliencia hidro-eléctrica confirma que la seguridad energética de Colombia no depende de la abundancia total del recurso, sino de su ubicación estratégica y de la flexibilidad del sistema para gestionarlo. A pesar de que la estadística valida una relación inversa entre el volumen útil y el precio de bolsa, la disparidad hídrica regional —evidenciada por el contraste entre los excedentes críticos de Urrá I y el agotamiento de cuencas en el Valle y Oriente— rompe la correlación perfecta y expone la vulnerabilidad de una red con limitaciones de transmisión. Por eso, se deben enfocar esfuerzos en fortalecer las áreas que históricamente se ven más golpeadas ante fenómenos extremos, tanto de lluvias intensas como sequías prolongadas. Así, diversificar la matriz en nodos críticos (Oriente y Valle) aligera la presión sobre embalses específicos.
<br>
En última instancia, la resiliencia del sector eléctrico no se logrará únicamente con lluvias, sino mediante el uso de modelos predictivos y una red flexible capaz de transformar un riesgo de inundación en el Norte en una solución de costo y estabilidad para el Sur, garantizando así un equilibrio entre la eficiencia operativa y el bienestar social de las comunidades.
<br>
¡Gracias por tu interés en este proyecto! Podrás contactarme a través del siguiente enlace
<br>

<div align="center">
<h2>👤 Autor</h2>
<h3>Mateo Velásquez Castro</h3>
<h4>Data Analyst con enfoque en Ingeniería de Datos</h4>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/velasquezmateo/)
</div>










