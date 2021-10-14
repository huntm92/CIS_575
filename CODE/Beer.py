import pandas as pd
import numpy as np

# Get Columns
df_cols = df = pd.read_csv('/Users/MHunt5/Google Drive/School/CSU/STAA 556/Beer/SNAP-Ratebeer.txt', sep = '[:]', header = None, engine = "python", nrows = 13, usecols = [0])
cols = list(df_cols[0])

# Read in Data.  This takes a while
df = pd.read_csv('/Users/MHunt5/Google Drive/School/CSU/STAA 556/Beer/SNAP-Ratebeer.txt', sep = '(?:^\S*)', header = None, engine = "python", usecols = [1])
df_t = pd.DataFrame(np.reshape(df.values,(int(df.shape[0] / 13),13)), columns = cols)
df_t.columns = df_t.columns.str.replace("/","_")

