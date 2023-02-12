import pandas as pd

dvf_df = pd.read_csv("output.txt", sep="|")
print(dvf_df.head(2))