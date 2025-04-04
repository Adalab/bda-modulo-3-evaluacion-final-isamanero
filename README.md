# Análisis Exploratorio de Datos (EDA) del Programa de Lealtad de una Aerolínea
## Descripción
Este informe técnico describe el análisis exploratorio de datos (EDA) realizado sobre un conjunto de datos que describe el comportamiento de los clientes dentro de un programa de lealtad de una aerolínea. Los datos se dividen en dos archivos:

Customer Flight Analysis.csv: Contiene información sobre la actividad de vuelo de los clientes, incluyendo vuelos reservados, distancia volada, puntos acumulados y redimidos, y costes asociados a los puntos redimidos.

Customer Loyalty History.csv: Proporciona el perfil detallado de los clientes, como su ubicación, nivel educativo, ingresos, y detalles sobre su membresía en el programa de lealtad.

## Objetivos del Estudio
Exploración inicial de los datos: Examinar las características generales de los datos para entender su estructura.

Limpieza de datos: Identificar y tratar problemas de calidad en los datos, como valores nulos y duplicados.

Visualización y resultados: Generar visualizaciones para resumir y analizar los patrones observados en los datos.

Bonus: Evaluación de diferencias en las reservas de vuelos según el nivel educativo de los clientes.

### 1. Exploración Inicial de los Datos
Customer Flight Analysis.csv
Dimensiones: (405,624 filas, 10 columnas)

Gestión de nulos: No se encontraron nulos en este archivo.

Duplicados: Se identificaron duplicados en la columna “Loyalty Number”, pero estos duplicados corresponden a diferentes fechas y son correctos.

Tipo de datos: Correcto. Se verificó que la columna Points Accumulated sea de tipo flotante.

Customer Loyalty History.csv
Dimensiones: (16,737 filas, 17 columnas)

Gestión de nulos:

Salary: 25.32% de los valores son nulos.

Cancellation Year y Cancellation Month: 87.65% de los valores son nulos, lo cual tiene sentido ya que estos campos están relacionados con la cancelación de vuelos, y la mayoría de los clientes no han cancelado vuelos.

Duplicados: No se encontraron duplicados.

Tipo de datos:

Salary: Se identificaron valores negativos, los cuales fueron transformados a su valor absoluto. Los valores nulos fueron reemplazados por la mediana, un valor estadístico estable.

Cancellation Year y Cancellation Month: Se decidió no modificar los valores nulos ni eliminar las columnas, ya que pueden ser útiles en el futuro para completar información sobre clientes activos.

Creación de la Columna 'Enrollment Date'
Se combinan las columnas Enrollment Month y Enrollment Year para crear una nueva columna Enrollment Date en formato datetime. Esto permite realizar análisis temporales más detallados.

### 2. Limpieza de Datos
Se realizó la limpieza y transformación de los datos, abordando los siguientes puntos:

Customer Flight Analysis.csv: No se identificaron problemas relevantes, ya que no hay nulos ni duplicados.

Customer Loyalty History.csv:

Salary: Se corrigieron valores negativos y se reemplazaron nulos con la mediana.

Cancellation Year y Cancellation Month: No se modificaron los valores nulos, ya que no afectan el análisis de los clientes activos.

### 3. Unión de Datos
Los dos conjuntos de datos fueron unidos en un solo archivo denominado Flight_Loyalty(union).csv. En este archivo combinado, se observa que todos los valores tienen un 0% de nulos, excepto las columnas relacionadas con la cancelación de vuelos (Cancellation Year y Cancellation Month), que tienen un 87.66% de nulos.

Resumen de la limpieza en el archivo combinado:
Sin nulos: Loyalty Number, Year, Month, Flights Booked, Flights with Companions, Total Flights, Distance, Points Accumulated, Points Redeemed, Dollar Cost Points Redeemed, Country, Province, City, Postal Code, Gender, Education, Salary, Marital Status, Loyalty Card, CLV, Enrollment Type, Enrollment Year, Enrollment Month, Enrollment Date.

Con nulos: Cancellation Year, Cancellation Month (87.66%).

### 4. Visualización y Resultados
Se realizaron análisis visuales para explorar las siguientes áreas:

Distribución de vuelos reservados por mes: Utilizando gráficos de barras y líneas para identificar patrones temporales en la actividad de vuelo de los clientes.

Relación entre distancia de vuelos y puntos acumulados: Se usaron diagramas de dispersión y gráficos de regresión para entender cómo la distancia de los vuelos afecta la acumulación de puntos.

Distribución de clientes por provincia/estado: Se usaron gráficos de barras y mapas para visualizar la geolocalización de los clientes.

Comparación del salario promedio por nivel educativo: Se realizaron gráficos de barras para comparar los salarios promedio según los diferentes niveles educativos de los clientes.

### 5. Evaluación de Diferencias en Reservas de Vuelos por Nivel Educativo
Se evaluaron las diferencias en el número de vuelos reservados entre distintos niveles educativos (Bachelor, College, Master, High School or Below, Doctor). Para ello, se realizaron pruebas estadísticas de hipótesis para comparar los grupos, identificando diferencias significativas entre los niveles educativos.

Conclusiones
Se detectaron algunos problemas con valores nulos, especialmente en los campos relacionados con las cancelaciones de vuelos, pero esto no afectó la calidad del análisis de clientes activos.

Los datos se limpiaron adecuadamente y se combinaron en un solo archivo para facilitar el análisis.

Se realizaron análisis visuales efectivos para explorar las variables clave y se descubrieron patrones importantes en el comportamiento de los clientes dentro del programa de lealtad.

Este análisis exploratorio proporciona una base sólida para continuar con estudios más profundos y la aplicación de técnicas de análisis predictivo.
