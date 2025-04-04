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

pd.set_option('display.max_columns', None) 