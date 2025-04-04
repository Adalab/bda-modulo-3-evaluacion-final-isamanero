# Análisis Exploratorio de Datos (EDA) del Programa de Lealtad de una Aerolínea
## Descripción
Este informe técnico describe el análisis exploratorio de datos (EDA) 📋 realizado sobre un conjunto de datos que describe el comportamiento de los clientes dentro de un programa de lealtad de una aerolínea 🛩️ Los datos se dividen en dos archivos:

📄Customer Flight Analysis.csv: Contiene información sobre la actividad de vuelo de los clientes, incluyendo vuelos reservados, distancia volada, puntos acumulados y redimidos, y costes asociados a los puntos redimidos.

📄Customer Loyalty History.csv: Proporciona el perfil detallado de los clientes, como su ubicación, nivel educativo, ingresos, y detalles sobre su membresía en el programa de lealtad.

## Objetivos del Estudio

### 1. Exploración Inicial de los Datos y 2. Limpieza de datos
![image](https://github.com/user-attachments/assets/40de19dc-df31-4ad4-a526-b897348bdc2a)

### 3. Unión de Datos
Los dos conjuntos de datos fueron unidos en un solo archivo denominado Flight_Loyalty(union).csv.
En este archivo combinado, se observa que todos los valores tienen un 0% de nulos, excepto las columnas relacionadas con la cancelación de vuelos (Cancellation Year y Cancellation Month), que tienen un 87.66% de nulos.

### 4. Visualización y Resultados
Se realizaron análisis visuales, que pueden observarse en la carpeta "Imágenes y gráficos"

### 5. BONUS. Evaluación de Diferencias en Reservas de Vuelos por Nivel Educativo
Se evaluaron las diferencias en el número de vuelos reservados entre distintos niveles educativos (Bachelor, College, Master, High School or Below, Doctor). Para ello, se realizaron pruebas estadísticas de hipótesis para comparar los grupos, identificando diferencias significativas entre los niveles educativos.

### Conclusiones
Se detectaron algunos problemas con valores nulos, especialmente en los campos relacionados con las cancelaciones de vuelos, pero esto no afectó la calidad del análisis de clientes activos.

Los datos se limpiaron adecuadamente y se combinaron en un solo archivo para facilitar el análisis.

Se realizaron análisis visuales efectivos para explorar las variables clave y se descubrieron patrones importantes en el comportamiento de los clientes dentro del programa de lealtad. Como: 

