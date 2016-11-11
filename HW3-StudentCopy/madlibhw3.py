# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text
import nltk 
import random
from nltk.book import text2 #importing text2 from nltk book corpa

print("START*******")

#nltk.download('punkt')

from nltk import word_tokenize,sent_tokenize

debug = False

tokens = []
for x in text2[:151]: #getting 150 tokens
	tokens.append(x)

print("TOKENS")
print (tokens)
#print (len(tokens))

tagged_tokens = nltk.pos_tag(tokens) # gives us a tagged list of tuples
#print("TAGGED TOKENS")
#print(tagged_tokens)

if debug:
	print ("First few tagged tokens are:")
	for tup in tagged_tokens[:151]:
		print (tup)

tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective", "NNP":"a proper noun"}
substitution_probabilities = {"NN":.15,"NNS":0.1,"VB":0.1,"JJ":0.1, "NNP":0.1} #assigns percentages to noun, plural nouns, verbs, etc. Added NNP proper noun

def spaced(word):
	if word in [",", ".", "?", "!", ":"]:
		return word
	else:
		return " " + word

final_words = []

for (word, tag) in tagged_tokens:
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
		final_words.append(spaced(word))
	else:
		new_word = input("Please enter %s:\n" % (tagmap[tag]))
		final_words.append(spaced(new_word))

print ("".join(final_words))

print("\n\nEND*******")
