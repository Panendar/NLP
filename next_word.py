# Simple Language Model Demonstration
# sentence = "The weather today is"
# possible_next_words = {
    # "sunny": 0.4,    # 40% probability
    # "rainy": 0.3,    # 30% probability  
    # "cloudy": 0.2,   # 20% probability
    # "snowy": 0.1     # 10% probability
# }

# Most likely prediction
# predicted = max(possible_next_words, key = possible_next_words.get)
# print(f"Input: '{sentence}'")
# print(f"Prediction: '{predicted}' ({possible_next_words[predicted] * 100}% confidence)")

# import math
# 
# word_prob = {
    # "I": 0.1,
    # "love|I": 0.3,
    # "Cats|love": 0.15
# }
# sentence_probs = word_prob["I"] * word_prob["love|I"] * word_prob["Cats|love"]
# print(f"P(I Love Cats) = {sentence_probs:.4f}")
# print(f"Log Probability: {math.log(sentence_probs):.2f}")

# N-GRAM MODEL # BIGRAM
# text = "I love cats. I love dogs. I love programming."
# words = text.replace(".", "").lower().split()
# print(words)
# bigram = []
# for i in range(len(words)-1):
#     bigram.append((words[i], words[i+1]))
# print(f"Bigrams Found: {bigram}")
# print("================================\n")

# from collections import Counter
# bigram_counts = Counter(bigram)
# print("Most common bigrams:", bigram_counts.most_common(3))
# print("================================\n")

# Before smoothing: unseen bigrams get 0 probability
bigram_counts = {"I love": 5, "love cats": 3, "cats are": 2}
vocab_size = 1000

# Add-one smoothing
def smooth_probability(count, total_bigrams, vocab_size):
    return (count + 1) / (total_bigrams + vocab_size)

# Now even unseen bigrams get small probability > 0
unseen_prob = smooth_probability(0, 10, vocab_size)
seen_prob = smooth_probability(5, 10, vocab_size)

print(f"Unseen bigram probability: {unseen_prob:.6f}")
print(f"Seen bigram probability: {seen_prob:.6f}")