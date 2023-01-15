import pandas as pd 
queries_path = "./modules/utils/Database/Preguntas.xlsx"

queries_df = pd.read_excel(queries_path, index_col=0)
queries_df = queries_df.to_dict('index')
queries_dict = dict()
parameter_list = list()

for key, value in queries_df.items():
	query = value['Preguntas'].split(',')
	queries_dict[key] = query
	parameter_list.append(key)
