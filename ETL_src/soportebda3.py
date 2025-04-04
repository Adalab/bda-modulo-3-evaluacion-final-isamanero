# En primer lugar, importamos las librerías que nos harán falta, desde el soporte:

# Para tratamiento de datos

import pandas as pd 
import numpy as np 

# Procesos de imputación

from sklearn.impute import SimpleImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.impute import KNNImputer

# Visuaicación de resultados

import matplotlib.pyplot as plt
import seaborn as sns

# Evaluar linealidad de las relaciones entre las variables
# y la distribución de las variables
# ------------------------------------------------------------------------------
#import scipy.stats as stats
import scipy.stats as stats
from scipy.stats import shapiro, poisson, chisquare, expon, kstest

import itertools
"""librería estándar de Python que contiene herramientas para manejar combinaciones,
permutaciones y otras operaciones sobre iterables"""

# Gestión de los warnings
import warnings
warnings.filterwarnings("ignore")




# FUNCIONES

# Revisión de valores atípicos
def revision_v_unicos(df):
    """
    Me permite revisar los valore únicos de un DataFrame
    Parámetros:
    param1 (df): Dataframe.
    Retorna:
    tipo: Cada columna, con sus valores únicos
    """
    for c in df.columns:
        
        print(f"Valores únicos en la columna '{c}':\n{df[c].unique()}\n")

# Revisión decimales reales
def tiene_decimales_reales(columna):
    """
    Revisión de valores en una serie de datos si
    son números decimales genuinos o si son simplemente
    números redondeados.

    Devuelve el total de números genuinos (reales, ej: 23.5)
    """
    return ((columna %1)!= 0).sum()



# Función para hipótesis
def prueba_hipotesis(*args):
    """
    Realiza una prueba de hipótesis para comparar grupos.
    1. Primero verifica si los datos son normales usando el test de Shapiro-Wilk o Kolmogorov-Smirnov.
    2. Si los datos son normales, usa Bartlett para probar igualdad de varianzas. Si no son normales, usa Levene.
    3. Si las varianzas son iguales, usa el t-test de Student; si no, usa la versión de Welch.
    4. Si los datos no son normales, usa el test de Mann-Whitney (alternativa no paramétrica).

    Parámetros:
    *args: listas o arrays con los datos de cada grupo.

    Retorna:
    dict con resultados del test de normalidad, varianza e hipótesis.
    """
    
    # Verificar si hay al menos dos grupos
    if len(args) < 2:
        raise ValueError("Se necesitan al menos dos conjuntos de datos para realizar la prueba.")
    
   # Comprobar normalidad en cada grupo
    normalidad = []
    for grupo in args:
        if len(grupo) > 50:
            p_valor_norm = stats.kstest(grupo, 'norm').pvalue  # Kolmogorov-Smirnov si n > 50
        else:
            p_valor_norm = stats.shapiro(grupo).pvalue  # Shapiro-Wilk si n <= 50
        normalidad.append(p_valor_norm > 0.05)

    datos_normales = all(normalidad)  # True si todos los grupos son normales

    # Prueba de igualdad de varianzas
    if datos_normales:
        p_valor_varianza = stats.bartlett(*args).pvalue  # Test de Bartlett si los datos son normales
    else:
        p_valor_varianza = stats.levene(*args, center="median").pvalue  # Test de Levene si no son normales

    varianzas_iguales = p_valor_varianza > 0.05

    # Aplicar el test adecuado
    if datos_normales:
        if varianzas_iguales:
            t_stat, p_valor = stats.ttest_ind(*args, equal_var=True)
            test_usado = "t-test de Student (varianzas iguales)"
        else:
            t_stat, p_valor = stats.ttest_ind(*args, equal_var=False)
            test_usado = "t-test de Welch (varianzas desiguales)"
    else:
        t_stat, p_valor = stats.mannwhitneyu(*args)
        test_usado = "Mann-Whitney U (prueba no paramétrica)"

    # Nivel de significancia
    alfa = 0.05

    # Resultados
    resultado = {
        "Test de Normalidad": normalidad,
        "Datos Normales": datos_normales,
        "p-valor Varianza": p_valor_varianza,
        "Varianzas Iguales": varianzas_iguales,
        "Test Usado": test_usado,
        "Estadístico": t_stat,
        "p-valor": p_valor,
        "Conclusión": "Rechazamos H0 (Diferencias significativas)" if p_valor < alfa else "No se rechaza H0 (No hay diferencias significativas)"
    }

    # Imprimir resultados de manera más clara
    print("\n📊 **Resultados de la Prueba de Hipótesis** 📊")
    print(f"✅ Test de Normalidad: {'Sí' if datos_normales else 'No'}")
    print(f"   - Normalidad por grupo: {normalidad}")
    print(f"✅ Test de Varianza: {'Iguales' if varianzas_iguales else 'Desiguales'} (p = {p_valor_varianza:.4f})")
    print(f"✅ Test aplicado: {test_usado}")
    print(f"📉 Estadístico: {t_stat:.4f}, p-valor: {p_valor:.4f}")
    print(f"🔍 Conclusión: {resultado['Conclusión']}\n")

    return resultado

#Función para realizar múltiples pruebas de hipótesis (función anterior)
def probar_combinaciones(df, columna_1, columna_2, funcion_prueba):
    """
    Función para probar todas las combinaciones posibles entre grupos
    usando una función de prueba de hipótesis.

    Parámetros:
    df (DataFrame): El DataFrame con los datos.
    columna_1 (str): Columna 1 a comparar
    columna_2 (str): El nombre de la columna que hace referencia
    funcion_prueba (function): La función que realizará la prueba de hipótesis entre dos grupos.
    """
    # Crear un diccionario para cada grupo educativo con sus respectivos datos de vuelos reservados
    grupos = {nombre: df[df[columna_1] == nombre][columna_2] 
              for nombre in df[columna_1].unique()}

    # Probar todas las combinaciones de dos grupos
    for (nombre1, datos1), (nombre2, datos2) in itertools.combinations(grupos.items(), 2):
        print(f"\nPrueba entre {nombre1} y {nombre2}")
        funcion_prueba(datos1, datos2)