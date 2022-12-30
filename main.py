import nltk
import string
import re
import os

import spacy
from nltk.corpus import stopwords

from queries_database import queries_df, parameter_list, queries_dict
from pokemon_database import pokemons as pokemon_dict
from tf_idf import calculate_similarity,calculate_similarity2


def define_parameter_asked(query):
	similarity = -1
	parameter_asked = ''
	for parameter in parameter_list:
		for sample_query in queries_dict[parameter]:
			similarity_aux = calculate_similarity(query, sample_query)
			similarity_aux1 = calculate_similarity2(query, sample_query)


			print(f"Similarity: {similarity_aux}, in {parameter}")
			print(f"Similarity2 : {similarity_aux1}, in {parameter}")
			if similarity_aux > similarity:
				similarity = similarity_aux
				parameter_asked = parameter
	print(similarity)
	return parameter_asked

def get_pokemon(question):
    for word in question.split():
        if word in pokemons:
            return word

def get_answer(parameter_asked, pokemon):
	if parameter_asked == 'Ratio_de_Captura':
		if pokemon_dict[pokemon][parameter_asked] >= 20:
			return 'Medio'
		elif pokemon_dict[pokemon][parameter_asked] >= 100:
			return 'Alto'
		else: 
			return 'Bajo'
	return pokemon_dict[pokemon][parameter_asked]

#nlp = spacy.load("es_core_news_md")
print(parameter_list)
#POKEMON si esta en mayus se pasa a minus
#Procesar texto
#Hacer respuestas medianamnte coherentes
#Handle errors
query = "Que ataques aprende Psyduck"
pokemon = 'Psyduck'
parameter = define_parameter_asked(query)
print(get_answer(parameter, pokemon))