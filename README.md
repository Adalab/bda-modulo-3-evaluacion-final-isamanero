# 🔎 Análisis Exploratorio de Datos (EDA) del Programa de Lealtad de una Aerolínea ✈️
## Descripción
Este informe técnico describe el análisis exploratorio de datos (EDA) 📋 realizado sobre un conjunto de datos que describe el comportamiento de los clientes dentro de un programa de lealtad de una aerolínea ✈️ Los datos se dividen en dos archivos:

📄Customer Flight Analysis.csv: Contiene información sobre la actividad de vuelo de los clientes, incluyendo vuelos reservados, distancia volada, puntos acumulados y redimidos, y costes asociados a los puntos redimidos.

📄Customer Loyalty History.csv: Proporciona el perfil detallado de los clientes, como su ubicación, nivel educativo, ingresos, y detalles sobre su membresía en el programa de lealtad.

## Objetivos del Estudio 📝

### 1. Exploración Inicial de los Datos y 2. Limpieza de datos (DOCUMENTACIÓN)
![image](Imágenes%20y%20gráficas/parte_documentacion.png)

**🧹 Resumen y preprocesamiento de los datos**
-Se realizaron comprobaciones iniciales para verificar la calidad y consistencia de los datos.
-Los valores nulos en la columna de **"Cancellation Month/Year"** se dejaron sin modificar, con la idea de que puedan completarse más adelante si se dispone de la información.
-En la columna **"Salary"**, los datos nulos fueron imputados utilizando la mediana. Esta decisión se tomó porque no afectaba significativamente al análisis, pero se recomienda tener en cuenta que estos valores son _"ficticios"_ para estudios futuros.
-Se creó una nueva columna **"Enrollment date"** combinando mes y año, con el objetivo de facilitar análisis temporales posteriores.

### 3. Unión de Datos
Los dos conjuntos de datos fueron unidos en un solo archivo denominado Flight_Loyalty(union).csv.
En este archivo combinado, se observa que todos los valores tienen un 0% de nulos, excepto las columnas relacionadas con la cancelación de vuelos (Cancellation Year y Cancellation Month), que tienen un 87.66% de nulos.

### 4. Visualización y Resultados 📊
Se realizaron análisis visuales, que pueden observarse en la carpeta "Imágenes y gráficos"

Podemos ver ejemplos como un gráfico de distrbución que muestra que los meses con mayorcantidad de vuelos reservados son de media los meses de junio, julio, agosto y diciembre.
![image](Imágenes%20y%20gráficas/Distribución%20de%20la%20cantidad%20de%20vuelos%20reservados%20por%20mes%20durante%20el%202017%20y%202018.jpg)

### 5. BONUS. Evaluación de Diferencias en Reservas de Vuelos por Nivel Educativo
Se evaluaron las diferencias en el número de vuelos reservados entre distintos niveles educativos (Bachelor, College, Master, High School or Below, Doctor). Para ello, se realizaron pruebas estadísticas de hipótesis para comparar los grupos, identificando diferencias significativas entre los niveles educativos.

Acceso al archivo .ipynb: [pinche aquí](https://github.com/Adalab/bda-modulo-3-evaluacion-final-isamanero/blob/main/EDA.ipynb)

### Conclusiones
Se detectaron algunos problemas con valores nulos, especialmente en los campos relacionados con las cancelaciones de vuelos, pero esto no afectó la calidad del análisis de clientes activos.

Los datos se limpiaron adecuadamente y se combinaron en un solo archivo para facilitar el análisis.

Se realizaron análisis visuales efectivos para explorar las variables clave y se descubrieron patrones importantes en el comportamiento de los clientes dentro del programa de lealtad. Como: 


