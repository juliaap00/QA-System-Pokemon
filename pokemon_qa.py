import nltk
import string
import re
import os

import spacy
from nltk.corpus import stopwords

from queries_database import queries_df, parameter_list, queries_dict
from pokemon_database import pokemons as pokemons
from tf_idf import calculate_similarity,calculate_similarity2


def define_parameter_asked(query):
	similarity = -1
	parameter_asked = ''
	for parameter in parameter_list:
		for sample_query in queries_dict[parameter]:
			similarity_aux = calculate_similarity(query, sample_query)
			similarity_aux1 = calculate_similarity2(query, sample_query)


			#print(f"Similarity: {similarity_aux}, in {parameter}")
			#print(f"Similarity2 : {similarity_aux1}, in {parameter}")
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
		if pokemons[pokemon][parameter_asked] >= 20:
			return 'Medio'
		elif pokemons[pokemon][parameter_asked] >= 100:
			return 'Alto'
		else: 
			return 'Bajo'
	return pokemons[pokemon][parameter_asked]


def get_elaborated_answer(parameter_asked, pokemon):
	if parameter_asked == 'N_Pokedex':
		simply_answer = get_answer(parameter_asked, pokemon)
		return f"El número de la Pokédex del pokemon {pokemon} es {simply_answer}."
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
		return f"El pokemon {pokemon} pesa {simply_answer} kg."
	if parameter_asked == 'Altura':
		simply_answer = get_answer(parameter_asked, pokemon)
		return f"El pokemon {pokemon} mide {simply_answer}."
	if parameter_asked == 'Legendario':
		simply_answer = get_answer(parameter_asked, pokemon)
		return f"El pokemon {pokemon} {simply_answer} es legendario."
	if parameter_asked == 'Habilidades':
		simply_answer = get_answer(parameter_asked, pokemon)
		return f"Las habilidades del pokemon {pokemon} son {simply_answer}."
	if parameter_asked == 'Habilidad_Oculta':
		simply_answer = get_answer(parameter_asked, pokemon)
		return f"La habilidad oculta del pokemon {pokemon} son {simply_answer}."
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
#DEBILIDAD -> QUE TIPO HACE MAS DAÑO A POKEMON
	#query = "Que ataques aprende Psyduck"
	query = query.lower()
	print(query)
	if query.lower() == '--help':
		return"""La información disponible para cada pokemon es la siguiente:
			1.Numero Pokedex. Por ej. ¿Qué Número de la Pokédex es Charizard?
			2.Descripción. Por ej. ¿Cuál es la descripción de Charizard?
			3.Tipo. Por ej. ¿De qué tipo es Charizard?
			4.Debilidades. Por ej. ¿A que es débil Charizard? 
			5.Peso. Por ej. ¿Cuánto pesa Charizard?
			6.Altura. Por ej. ¿Cuánto mide Charizard?
			7.Legendario. Por ej. ¿Es Charizard legendario?
			8.Habilidades. Por ej. ¿Qué habilidades tiene Charizard?
			9.Habilidades Ocultas. Por ej. ¿Qué habilidades ocultas tiene Charizard?
			10.Generación. Por ej. ¿En qué generación apareció Charizard?
			11.Hábitat. Por ej. ¿Cuál es el hábitat de Charizard?
			13.Cadena Evolutiva. Por ej. ¿Cuál es la cadena evolutiva de Charizard?
			14.Obtención. Por ej. ¿Cómo se obtiene a Charizard?
			15.Ratio de captura. Por ej.  ¿Cuál es el ratio de captura de Charizard?
			16.Movientos. Por ej. ¿Qué movimientos aprende Charizard?"""

	else:
		#remove puntcuation
		pokemon = get_pokemon(query)
		if pokemon != None:
			print(f"El Pokémon preguntado es {pokemon}")
			print(parameter_list)
			#POKEMON si esta en mayus se pasa a minus
			#Procesar texto
			#Hacer respuestas medianamnte coherentes
			#Handle errors
			parameter = define_parameter_asked(query)
			return get_elaborated_answer(parameter, pokemon)

		else:
			return f"El Pokémon {pokemon} no se encuentra en la base de datos."