from nltk import pos_tag, RegexpParser
from tokenize_words import word_sentence_tokenize
from chunk_counters import np_chunk_counter, vp_chunk_counter

'''
This was a project i developped in my Codecademy's Natural language processing course.
In the project folder your will find two texts: Oscar Wilde’s The Picture of Dorian
Gray or Homer’s The Iliad!
I chose to perform syntax analysis in the latter, but feel free to change the text and see
what insights these nlp tools can provide us
'''

# import text of choice here
text = open('the_iliad.txt', encoding='utf-8').read().lower()

# sentence and word tokenize text here
word_tokenized_text = word_sentence_tokenize(text)


# store and print any word tokenized sentence here
single_word_tokenized_sentence = word_tokenized_text[100]


# create a list to hold part-of-speech tagged sentences here
pos_tag_text = []

# create a for loop through each word tokenized sentence here
for tokenized_sentence in word_tokenized_text:
  # part-of-speech tag each sentence and append to list of pos-tagged sentences here
  pos_tag_text.append(pos_tag(tokenized_sentence))

# store and print any part-of-speech tagged sentence here
single_pos_sentence = pos_tag_text[100]
print(single_pos_sentence)


# define noun phrase chunk grammar here
np_chunk_grammar = 'NP: {<DT>?<JJ>*<NN>}'

# create noun phrase RegexpParser object here
np_chunk_parser = RegexpParser(np_chunk_grammar)

# define verb phrase chunk grammar here
vp_chunk_grammar = 'VP: {<DT>?<JJ>*<NN><VB.*><RB.?>?}'

# create verb phrase RegexpParser object here
vp_chunk_parser = RegexpParser(vp_chunk_grammar)

# create a list to hold noun phrase chunked sentences and a list to hold verb phrase chunked sentences here
np_chunk_text = []
vp_chunk_text = []



# create a for loop through each pos-tagged sentence here
for tagged_sentence in pos_tag_text:
  # chunk each sentence and append to lists here
  np_chunk_text.append(np_chunk_parser.parse(tagged_sentence))
  vp_chunk_text.append(vp_chunk_parser.parse(tagged_sentence))
  

# store and print the most common NP-chunks here
most_common_np_chunks = np_chunk_counter(np_chunk_text)
print(most_common_np_chunks)

# store and print the most common VP-chunks here
most_common_vp_chunks = vp_chunk_counter(vp_chunk_text)
print(most_common_vp_chunks)