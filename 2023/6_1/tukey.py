import scikit_posthocs as sp
import pandas as pd

df = pd.read_csv('ex.csv')

dfw = df.query(' paper_color == "white"')

results = sp.posthoc_tukey(
    dfw,
    val_col = 'score',
    group_col = 'font_color'
)

print(results)