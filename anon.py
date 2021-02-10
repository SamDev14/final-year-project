import pandas as pd
import numpy as np
import scipy.stats
%matplotlib inline

import matplotlib.pyplot as plt
from sklearn_pandas import DataFrameMapper
from sklearn.preprocessing import labelEncoder

import warnings
warnings.filterwarnings("ignore")

from IPython.core.interactiveshell import interactiveshell
interactiveshell.ast_node_interactive = "all"

from utils import best_fit_distribution
from utils import plot_result


df = pd.read_csv("./AWS_Honeypot_marx-geo.csv")
df.shape
df.head()

encoders = [(["ip-address"], labelEncoder())]
mapper = DataFrameMapper(encoders, df_out=True)
new_cols = mapper.fit_transform(df.copy())
df = pd.concat([df.drop(columns=["ip-address"]), new_cols], axis="columns")
