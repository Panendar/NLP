# using python version 3.12 since gensim package is not available for python 3.13

import gensim.downloader as api
import sys

model_name = 'glove-wiki-gigaword-100'
print(f"Loading model: {model_name}")
sys.stdout.flush()

model = api.load(model_name)
print("Model loaded successfully!")
sys.stdout.flush()

word = input("Enter your word: ").strip().lower()

if word in model.key_to_index:
    synonyms = model.most_similar(positive=[word], topn=5)
    print(f"The synonyms of '{word}' are:")
    for synonym, similarity in synonyms:
        print(f"  {synonym}: {similarity:.4f}")
    sys.stdout.flush()
else:
    print(f"The word '{word}' is not found in the vocabulary.")
    sys.stdout.flush()