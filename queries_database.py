import pandas as pd 
queries_path = "./Preguntas.xlsx"

queries_df = pd.read_excel(queries_path, index_col=1)
print(queries_df)

queries_df = queries_df.to_dict()

for key,query in queries_df.items():
	queries_df['key'] = query.split(',')

print(queries_df)