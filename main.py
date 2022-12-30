import nltk
import string
import re
import os

import spacy


from nltk.corpus import stopwords



from queries_database import queries_df, parameter_list, queries_dict
from pokemon_database import pokemon_df



def define_parameter_asked(query):
	similarity = -1
	parameter_asked = ''
	query_nlp = nlp(query)
	for parameter in parameter_list:
		for sample_query in queries_dict[parameter]:
			sample_query_nlp = nlp(sample_query)
			similarity_aux = query_nlp.similarity(sample_query_nlp)
			print(f"Similarity: {similarity_aux}, in {parameter}")
			if similarity_aux > similarity:
				similarity = similarity_aux
				parameter_asked = parameter
	return parameter_asked

#nlp = spacy.load("es_core_news_md")
nlp = spacy.load("es_core_news_lg")

query = "pokedex"
parameter = define_parameter_asked(query)
print(parameter)