import pandas as pd
import numpy as np
from IPython import embed

# Get Columns
df_cols = df = pd.read_csv('/Users/MHunt5/Google Drive/School/CSU/STAA 556/Beer/SNAP-Ratebeer.txt',
                           sep='[:]',
                           header=None,
                           engine="python",
                           nrows=13,
                           usecols=[0]
                           )
cols = list(df_cols[0])

# Read in Data.  This takes a while
df = pd.read_csv('/Users/MHunt5/Google Drive/School/CSU/CIS 575/PROJECT/Beer/SNAP-Ratebeer.txt',
                 sep='^\S*',
                 header=None,
                 engine="python",
                 usecols=[1]
                 )
cols.append("Remove")

df = pd.DataFrame(np.reshape(df.values,(int(df.shape[0] / 14), 14)), columns=cols)
df = df.drop(columns='Remove')
df.columns = df.columns.str.replace("/", "_")
df["review_time"] = pd.to_datetime(df["review_time"], unit='s')
embed()
