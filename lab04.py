import math
import re

# Define a function to tokenize text into words
def tokenize(text):
    return re.findall(r'\b\w+\b', text.lower())

# Define a function to train a Naive Bayes classifier
def train_naive_bayes(training_data):
    spam_word_counts = {}
    ham_word_counts = {}
    spam_total_words = 0
    ham_total_words = 0
    spam_email_count = 0
    ham_email_count = 0

    for email, label in training_data:
        words = tokenize(email)
        if label == 'spam':
            spam_email_count += 1
            for word in words:
                spam_word_counts[word] = spam_word_counts.get(word, 0) + 1
                spam_total_words += 1
        else:
            ham_email_count += 1
            for word in words:
                ham_word_counts[word] = ham_word_counts.get(word, 0) + 1
                ham_total_words += 1

    # Calculate prior probabilities
    spam_prior = spam_email_count / (spam_email_count + ham_email_count)
    ham_prior = ham_email_count / (spam_email_count + ham_email_count)

    return spam_word_counts, ham_word_counts, spam_total_words, ham_total_words, spam_prior, ham_prior

# Define a function to classify an email as spam or ham
def classify_naive_bayes(email, spam_word_counts, ham_word_counts, spam_total_words, ham_total_words, spam_prior, ham_prior):
    words = tokenize(email)
    spam_score = 0
    ham_score = 0

    for word in words:
        # Calculate the conditional probabilities using Laplace smoothing
        spam_prob = (spam_word_counts.get(word, 0) + 1) / (spam_total_words + len(spam_word_counts))
        ham_prob = (ham_word_counts.get(word, 0) + 1) / (ham_total_words + len(ham_word_counts))
        
        # Use logarithms to avoid underflow
        spam_score += math.log(spam_prob)
        ham_score += math.log(ham_prob)

    # Apply the priors
    spam_score += math.log(spam_prior)
    ham_score += math.log(ham_prior)

    return 'spam' if spam_score > ham_score else 'ham'

# Sample training data (you should replace this with your own data)
training_data = [
    ("Buy our new product!", "spam"),
    ("Hi, how are you?", "ham"),
    ("You've won a prize!", "spam"),
    ("Meeting tomorrow at 10 AM.", "ham"),
]

# Train the Naive Bayes classifier
spam_word_counts, ham_word_counts, spam_total_words, ham_total_words, spam_prior, ham_prior = train_naive_bayes(training_data)

# Sample email to classify
sample_email = "Congratulations! You've won a million dollars! Claim your prize now!"

# Classify the sample email
classification = classify_naive_bayes(sample_email, spam_word_counts, ham_word_counts, spam_total_words, ham_total_words, spam_prior, ham_prior)
print(f"Classification: {classification}")