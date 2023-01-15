import pandas as pd 
pokemon_path = "./modules/utils/Database/Pokemons.xlsx"

pokemon_df = pd.read_excel(pokemon_path, index_col = 0)
pokemon_df.drop('Página Web', axis = 1,inplace = True)

pokemons = pokemon_df.to_dict('index')
