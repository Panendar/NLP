# using thepython 3.

import gensim.downloader as api
import sys
import re

model_name = 'glove-wiki-gigaword-100'
print(f"Loading model: {model_name} (128MB)")
sys.stdout.flush()

model = api.load(model_name)
print("Model loaded successfully!")
sys.stdout.flush()

word = input("Enter your word: ").strip().lower()

def is_valid_synonym(word_candidate, original_word):
    """Filter out contractions, single letters, and non-alphabetic words"""
    # Must be all letters and more than 2 characters
    if not re.match(r'^[a-zA-Z]{3,}$', word_candidate):
        return False
    # Don't include the original word
    if word_candidate.lower() == original_word.lower():
        return False
    # Filter out common non-synonyms
    common_words = {'the', 'and', 'but', 'for', 'are', 'you', 'all', 'any', 'can', 'had', 'her', 'was', 'one', 'our', 'out', 'day', 'get', 'has', 'him', 'his', 'how', 'man', 'new', 'now', 'old', 'see', 'two', 'way', 'who', 'boy', 'did', 'its', 'let', 'put', 'say', 'she', 'too', 'use'}
    if word_candidate.lower() in common_words:
        return False
    return True

if word in model.key_to_index:
    # Get more candidates to filter from
    candidates = model.most_similar(positive=[word], topn=50)
    
    # Filter for valid synonyms
    valid_synonyms = []
    for synonym, similarity in candidates:
        if is_valid_synonym(synonym, word):
            valid_synonyms.append((synonym, similarity))
        if len(valid_synonyms) >= 10:  # Get 10 good synonyms
            break
    
    if valid_synonyms:
        print(f"The synonyms of '{word}' are:")
        for synonym, similarity in valid_synonyms:
            print(f"  {synonym}: {similarity:.4f}")
        sys.stdout.flush()
    else:
        print(f"No clear synonyms found for '{word}'")
        sys.stdout.flush()
else:
    print(f"The word '{word}' is not found in the vocabulary.")
    sys.stdout.flush()