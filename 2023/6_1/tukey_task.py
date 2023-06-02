import scikit_posthocs as sp
import pandas as pd
import numpy as np

df = pd.read_csv('task.csv')
data_melt = df.melt(var_name = 'method',value_name = 'score')
dfw = data_melt.query(' index > -1')
results = sp.posthoc_tukey(
    dfw,
    val_col = 'score',
    group_col = 'method'
)
print(results)