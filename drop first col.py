import pandas as pd
df = pd.read_csv('uniprot_sprot_human.dat-GO_Digger_Sparse.py.txt-TableGen.py.csv')
# If you know the name of the column skip this
first_column = df.columns[0]
# Delete first
df = df.drop([first_column], axis=1)
df.to_csv('file.csv', index=False)