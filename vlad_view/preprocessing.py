import pandas as pd

from helper import querying_auditd, parents_to_children
from config import *

parents_hits = querying_auditd(par_type, index, size)
children_hits = querying_auditd(child_type, index, size)
auditd = parents_to_children(parents_hits, children_hits, par_fields, ch_fields)

# Hack with child_fields (nametype)
m = len(auditd[0])
n = len(par_fields + ch_fields)
columns = par_fields + ch_fields + ["nametype_" + str(i) for i in range(1, m - n + 1)]

# One-hot encoding with pandas
df_pandas = pd.DataFrame(auditd, columns=columns)
df_pandas_encoded = pd.get_dummies(df_pandas)
auditd_encoded = df_pandas_encoded.as_matrix()

# Correlation matrix
corr_matrix = df_pandas_encoded.corr()