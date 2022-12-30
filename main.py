import nltk
import string
import re
import os

import spacy


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from queries_databse import queries_df, parameter_list
from pokemon_databse import pokemon_df



def define_parameter_asked(query):
	similarity = -1
	parameter_asked = ''
	query_nlp = nlp(query)
	for parameter in parameter_list:
		for sample_query in query_df[parameter]
			sample_query_nlp = nlp(sample_query)
			similarity_aux = query_nlp.similarity(sample_query_nlp)
			if similarity_aux > similarity:
				similarity = similarity_aux
				parameter_asked = parameter
	return parameter_asked
