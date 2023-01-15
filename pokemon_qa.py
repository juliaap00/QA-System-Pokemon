import nltk
import string
import re
import os

import spacy
from nltk.corpus import stopwords

from queries_database import queries_df, parameter_list, queries_dict
from pokemon_database import pokemons as pokemons
from tf_idf import calculate_similarity,calculate_similarity2

import unicodedata

def remove_accents(string):
    # Make a translation table to remove the accents
    table = str.maketrans("", "", "áéíóúñÁÉÍÓÚÑ")

    # Use the translation table to remove the accents
    stripped_string = string.translate(table)

    # Normalize the string to NFC form
    normalized_string = unicodedata.normalize("NFC", stripped_string)

    return normalized_string


def define_parameter_asked(query):
	similarity = -1
	parameter_asked = ''
	for parameter in parameter_list:
		for sample_query in queries_dict[parameter]:
			sample_query =  remove_accents(sample_query)
			similarity_aux = calculate_similarity(query, sample_query)
			#similarity_aux1 = calculate_similarity2(query, sample_query)


			#print(f"Similarity: {similarity_aux}, in {parameter}")
			#print(f"Similarity2 : {similarity_aux1}, in {parameter}")
			if similarity_aux > similarity:
				similarity = similarity_aux
				parameter_asked = parameter

	print("La similaridad de la pregunta con el parámetro escogido", parameter_asked, "es:", similarity)
	return parameter_asked

def get_pokemon(question):
	tmp = question.replace('¿', '').replace('?', '').replace(',', '').replace('.', '')
	for word in tmp.split():
		if word in pokemons:
			return word

def get_answer(parameter_asked, pokemon):
	if parameter_asked == 'Ratio_de_Captura':
		if pokemons[pokemon][parameter_asked] >= 20:
			return 'media'
		elif pokemons[pokemon][parameter_asked] >= 100:
			return 'alta'
		else: 
			return 'baja'
	return pokemons[pokemon][parameter_asked]


def get_elaborated_answer(parameter_asked, pokemon):
	if parameter_asked == 'N_Pokedex':
		simply_answer = get_answer(parameter_asked, pokemon)
		return f"El número de la Pokedex del pokemon {pokemon} es {simply_answer}."
	if parameter_asked == 'Descripcion':
		simply_answer = get_answer(parameter_asked, pokemon)
		return f"La descripción del pokemon {pokemon} es {simply_answer}."
	if parameter_asked == 'Tipo':
		simply_answer = get_answer(parameter_asked, pokemon)
		return f"El tipo del pokemon {pokemon} es {simply_answer}."
	if parameter_asked == 'Debilidades':
		simply_answer = get_answer(parameter_asked, pokemon)
		return f"El pokemon {pokemon} es débil a {simply_answer}."
	if parameter_asked == 'Peso':
		simply_answer = get_answer(parameter_asked, pokemon)
		return f"El pokemon {pokemon} pesa {simply_answer}."
	if parameter_asked == 'Altura':
		simply_answer = get_answer(parameter_asked, pokemon)
		return f"El pokemon {pokemon} mide {simply_answer}."
	if parameter_asked == 'Legendario':
		simply_answer = get_answer(parameter_asked, pokemon)
		return f"El pokemon {pokemon} {simply_answer} es legendario."
	if parameter_asked == 'Habilidades':
		simply_answer = get_answer(parameter_asked, pokemon)
		return f"Las habilidades del pokemon {pokemon}: {simply_answer}."
	if parameter_asked == 'Habilidad_Oculta':
		simply_answer = get_answer(parameter_asked, pokemon)
		return f"La habilidad oculta del pokemon {pokemon}: {simply_answer}."
	if parameter_asked == 'Generacion':
		simply_answer = get_answer(parameter_asked, pokemon)
		return f"El pokemon {pokemon} es de la generación {simply_answer}."
	if parameter_asked == 'Habitat':
		simply_answer = get_answer(parameter_asked, pokemon)
		return f"El pokemon {pokemon} habita en {simply_answer}."
	if parameter_asked == 'Cadena_Evolutiva':
		simply_answer = get_answer(parameter_asked, pokemon)
		return f"La cadena evolutiva del pokemon {pokemon} es {simply_answer}."
	if parameter_asked == 'Obtencion':
		simply_answer = get_answer(parameter_asked, pokemon)
		return f"El pokemon {pokemon} se obtiene {simply_answer}."
	if parameter_asked == 'Ratio_de_Captura':
		simply_answer = get_answer(parameter_asked, pokemon)
		return f"El pokemon {pokemon} tiene una probabilidad {simply_answer} de captura."
	if parameter_asked == 'Movimientos':
		simply_answer = get_answer(parameter_asked, pokemon)
		return f"El pokemon {pokemon} puede aprender los siguientes movimientos {simply_answer}."
	return 'Lo siento no he podido obtener la respuesta a la pregunta.'


#while(True):
def qa(query):
	print()
	#DEBILIDAD -> QUE TIPO HACE MAS DAÑO A POKEMON
	#query = "Que ataques aprende Psyduck"
	query = query.lower()
	print(query)
	print()
	if query.lower() == '--help':
		return"""La información disponible para cada pokemon es la siguiente:
			Número Pokedex. Por ej. ¿Qué número de la Pokedex es Charizard?
			Descripción. Por ej. ¿Cuál es la descripción de Charizard?
			Tipo. Por ej. ¿De qué tipo es Charizard?
			Debilidades. Por ej. ¿A que es débil Charizard?
			Peso. Por ej. ¿Cuánto pesa Charizard?
			Altura. Por ej. ¿Cuánto mide Charizard?
			Legendario. Por ej. ¿Es Charizard legendario?
			Habilidades. Por ej. ¿Qué habilidades tiene Charizard?
			Habilidades Ocultas. Por ej. ¿Qué habilidades ocultas tiene Charizard?
			Generación. Por ej. ¿En qué generación apareció Charizard?
			Hábitat. Por ej. ¿Cuál es el hábitat de Charizard?
			Cadena Evolutiva. Por ej. ¿Cuál es la cadena evolutiva de Charizard?
			Obtención. Por ej. ¿Cómo se obtiene a Charizard?
			Ratio de captura. Por ej.  ¿Cuál es el ratio de captura de Charizard?
			Movientos. Por ej. ¿Qué movimientos aprende Charizard?
			"""

	else:
		#remove puntcuation
		query = remove_accents(query)
		pokemon = get_pokemon(query)
		if pokemon != None:
			print(f"El pokemon preguntado es {pokemon}")
			#print(parameter_list)
			#POKEMON si esta en mayus se pasa a minus
			#Procesar texto
			#Hacer respuestas medianamnte coherentes
			#Handle errors
			parameter = define_parameter_asked(query)
			return get_elaborated_answer(parameter, pokemon)

		else:
			return f"El pokemon {pokemon} no se encuentra en la base de datos."
