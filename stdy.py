import spacy

# create an blank english NLP object
# nlp = spacy.blank("en")
# doc = nlp("This is a sentence.")

# for token in doc:
#     print(token.text, token.idx)  # print token text and its character offset   
# token = doc[2]
# print(token)

# # span 
# span = doc[2:4]
# print(span)


# docs = nlp("This costs of $ 50.")
# print("Index :" ,[token.i for token in docs])
# print("Text :", [token.text for token in docs])
# print("is_alpha :", [token.is_alpha for token in docs])
# print("is_punct :", [token.is_punct for token in docs])
# print("like_num :", [token.like_num for token in docs])


# Check whether the next token’s text attribute is a percent sign ”%“.
# doc = nlp(
#     "In 1990, more than 60% of people in East Asia were in extreme poverty. "
#     "Now less than 4% are."
# )
# for token in doc:
#     if token.like_num:
#         next_token = doc[token.i+1]
#         if next_token.text == "%":
#             print(f"Found a percentage: {token.text}{next_token.text}")


nlp = spacy.load("en_core_web_lg")
# doc = nlp("She ate the pizza with extra cheese.")
# whether a word is the subject of the sentence or an object.
# The .dep_ attribute returns the predicted dependency label.
# The .head attribute returns the syntactic head token. You can also think of it as the parent token this word is attached to.

# for token in doc:
#     print(f"{token.text:<12}-->{token.pos_:<10}--> {token.dep_:<10}--> {token.head.text:<10}")

# Lemmatization is the process of reducing a word to its base or root form.
# from nltk.tokenize import word_tokenize
# from nltk.stem import WordNetLemmatizer
# lemmatizer = WordNetLemmatizer()

# doc = "The cats were running faster than the dogs."
# token_words = word_tokenize(doc)
# token_lower = [word.lower() for word in token_words]
# lemmatized_words = [lemmatizer.lemmatize(word) for word in token_lower]
# print("Lemmatized Words : ", lemmatized_words)

# using spacy
doc = nlp("The cats were running faster than the dogs.")
for token in doc:
    print(f"{token.text:<12}--> {token.lemma_:<10}")

# sentence tokenization
# text = "Apple is looking at buying a U.K. startup for $1 billion. This is a second sentence!"
# doc = nlp(text)
# for sent in doc.sents:
#     print(f"Sentence: {sent.text}")

# stop words removal
# from spacy.lang.en.stop_words import STOP_WORDS
# stop_words = list(STOP_WORDS)
# doc_len = []
# for token in doc:
#     if token.text.lower() not in stop_words:
#         doc_len.append(token.text)
# print("Original Length :", len(doc))
# print("After Stop Words Removal Length :", len(doc_len))
# for word in doc:
#     if word.text.lower() not in stop_words:
#         print(word.text)

# Named Entity object
# from spacy import displacy
# doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
# for ent in doc.ents:
#     print(f"{ent.text} --> {ent.label_}")
# displacy.render(doc, style="ent")


# from spacy.matcher import Matcher
# matcher = Matcher(nlp.vocab)
# pattern = [{"TEXT": "iPhone"}, {"TEXT": "X"}]
# matcher.add("IPHONE_PATTERN", [pattern])
# doc = nlp("The new iPhone X was released last week. Another iPhone X is expected next year.")
# matches = matcher(doc)
# for match_id, start, end in matches:
#     span = doc[start:end]
#     print(f"Matched span: {span.text}")

# pattern = [
#     {"IS_DIGIT": True},
#     {"LOWER": "fifa"},
#     {"LOWER": "world"},
#     {"LOWER": "cup"},
#     {"IS_PUNCT": True}
# ]
# matcher.add("FIFA_WORLD_CUP_PATTERN", [pattern])
# doc = nlp("2018 FIFA World Cup: France won!")
# matches = matcher(doc)
# for match_id, start, end in matches:
#     span = doc[start:end]
#     print(f"Matched span: {span.text}")

