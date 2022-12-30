from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from Levenshtein import distance

def calculate_similarity(sentence1, sentence2):
	# Calculate the TF-IDF of each word in the sentences
	vectorizer = TfidfVectorizer()
	tfidf = vectorizer.fit_transform([sentence1, sentence2])

	# Calculate the cosine similarity between the vectors of weights
	similarity = cosine_similarity(tfidf[0], tfidf[1])[0][0]

	# Calculate the Levenshtein distance between the sentences
	distance_calculated = distance(sentence1, sentence2)

	# Return a combined measure of similarity
	return similarity * (1 - distance_calculated / max(len(sentence1), len(sentence2)))


def calculate_similarity2(sentence1, sentence2):
  # Calculate the Levenshtein distance between the sentences
  distance_calculated = distance(sentence1, sentence2)

  # Calculate the length of the longest sentence
  max_length = max(len(sentence1), len(sentence2))

  # Return a measure of similarity based on the distance
  return 1 - (distance_calculated / max_length)

