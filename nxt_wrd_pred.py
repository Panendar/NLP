text = "I love cats. I love dogs. I love programming."
punctuations = "!()-[]{};:'\"\\,<>./?@#$%^&*_~"
words = ''.join([char for char in text if char not in punctuations]).lower().split()

unigrams = []
for i in range(len(words)):
    unigrams.append((words[i],))

bigrams = []
for i in range(len(words) -1):
    bigrams.append((words[i], words[i+1]))

from collections import Counter
unigram_counts = Counter(unigrams)
bigram_counts = Counter(bigrams)
# print("Unigram Counts :", unigram_counts)
# print("Bigram Counts: ", bigram_counts)
total_bigrams = len(bigrams)
print("Total Bigrams: ", total_bigrams)
# print(unigram_counts.items())

print("===============Probabilities==============")

# fix: use total unigrams (total tokens) as denominator for unigram probabilities
total_unigrams = sum(unigram_counts.values())  # or len(words)

unigram_prob = {}
for word, count in unigram_counts.items():
    # guard against division by zero if corpus is empty
    prob = (count / total_unigrams) if total_unigrams != 0 else 0.0
    unigram_prob[word] = prob
print("Unigram Probabilities: ")
for word, prob in unigram_prob.items():
    print(f"  {word[0]}: {prob:.4f}")

print("================================\n")

bigram_prob = {}
# unpack bigram as (prev, next) — consistent with how bigrams were created above
for (prev, nxt), count in bigram_counts.items():
    prev_count = unigram_counts.get((prev,), 0)
    prob = (count / prev_count) # if prev_count != 0 else 0.0
    bigram_prob[(prev, nxt)] = prob

print("Bigram Probabilities: ")
for (prev,next), prob in bigram_prob.items():
    print(f"({prev}, {next})-> {prob:.4f}")

print("================================\n")

# Function for predicting the next word
def pred_next_word(previous_word):
    fit_words = {next_word: prob for (prev, next_word), prob in bigram_prob.items() if prev == previous_word}

    ranking_fit = sorted(fit_words.items(), key = lambda x:x [1], reverse = True)
    return ranking_fit[:3]

next_word = input("Enter a word to predict its next word: ").strip().lower()
predictions = pred_next_word(next_word)
if predictions:
    print(f"Predictions for '{next_word}': ")
    for word, prob in predictions:
        print(f"  {word} ({prob:.4f})")