import pandas as pd 
pokemon_path = "./Pokemons.xlsx"

pokemon_df = pd.read_excel(pokemon_path, index_col=1)
print(pokemon_df)

