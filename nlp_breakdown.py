from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from spacy import load
from nltk.stem import PorterStemmer, WordNetLemmatizer

nlp = load("en_core_web_sm")
sentence = input("Enter your text: ")

# using Spacy
print("Using Spacy...\n")
doc = nlp(sentence)

for word in doc:
    print(f"{word.text} -> {word.lemma_} -> {word.pos_}")
print("================================\n")

print("Using NLTK...\n")

word_length = len(sentence)

#sentence tokenization
new_sent = sent_tokenize(sentence)

#word tokenization
new_word_sent = word_tokenize(sentence)

# stop_word removal
stop_words = set(stopwords.words('english'))

filtered_sentence = [w.lower() for w in new_word_sent if w.lower() not in stop_words and w.isalpha()]
filtered_word_length = len(filtered_sentence)

analysis = []
for w in filtered_sentence:
    if w not in analysis:  
        analysis.append(w)
count = len(analysis)

removed_words = []
for w in new_word_sent:
    if w.lower() not in [word.lower() for word in filtered_sentence]:
        removed_words.append(w)

print("\nOriginal Sentence :", sentence)
print("\nSentence Tokenization: ", new_sent)
print("\nWord Tokenization: ", new_word_sent)
print("\nFiltered Sentence: ", filtered_sentence)
print(f"\nAnalysis (unique words): {analysis} -> Count: {count}")
print(f"\nRemoved Words: {removed_words}")
print("================================\n")

# stemming and lemmatization

stem_word = PorterStemmer()
lem_word = WordNetLemmatizer()

print("===============Stemming==============")
word_stem = []
for w in filtered_sentence:
    stemmed = stem_word.stem(w)
    word_stem.append(stemmed)
    print(f"{w} -> {stemmed}")
# print(f"\nStemmed Words List: {word_stem}")
print("\n================================\n")

print("===============Lemmatization==============")
word_lem = []
for w in filtered_sentence:
    lemmatized = lem_word.lemmatize(w)
    word_lem.append(lemmatized)
    print(f"{w} -> {lemmatized}")
# print(f"\nLemmatized Words List: {word_lem}")
print("\n================================\n")
