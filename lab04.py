import math
import re
import os

################### IMPLEMENTATION REGION ########################

# tokenize text into words
def tokenize(text):
    return re.findall(r'\b\w+\b', text.lower())

# train a Naive Bayes classifier with Laplace smoothing
# Laplace smoothing helps avoid zero probabilities for words that don't appear in the training data for a particular class. 
def train_naive_bayes(training_data, alpha=1.0):
    spam_word_counts = {}
    ham_word_counts = {}
    spam_total_words = 0
    ham_total_words = 0
    spam_email_count = 0
    ham_email_count = 0

    vocabulary = set()  # unique words

    # bag of words using unigram
    for email, label in training_data:
        words = tokenize(email)
        if label == 'spam':
            spam_email_count += 1
            for word in words:
                spam_word_counts[word] = spam_word_counts.get(word, 0) + 1
                spam_total_words += 1
                vocabulary.add(word)
        else:
            ham_email_count += 1
            for word in words:
                ham_word_counts[word] = ham_word_counts.get(word, 0) + 1
                ham_total_words += 1
                vocabulary.add(word)

    # P(spam | w1, w2, .. wN) = P(spam)*П P(Wi | spam)
    spam_prior = spam_email_count / (spam_email_count + ham_email_count)
    # P(ham | w1, w2, ... wN) = P(ham)* П P(wi | ham) 
    ham_prior = ham_email_count / (spam_email_count + ham_email_count)

    return spam_word_counts, ham_word_counts, spam_total_words, ham_total_words, spam_prior, ham_prior, vocabulary, alpha

# classify an email as spam or ham with Laplace smoothing
def classify_naive_bayes(email, spam_word_counts, ham_word_counts, spam_total_words, ham_total_words, spam_prior, ham_prior, vocabulary, alpha):
    words = tokenize(email)
    spam_score = 0
    ham_score = 0

    for word in words:
        # P(Wi | spam) = N wi | spam + a / N spam + a * N vocab
        spam_prob = (spam_word_counts.get(word, 0) + alpha) / (spam_total_words + alpha * len(vocabulary))
        ham_prob = (ham_word_counts.get(word, 0) + alpha) / (ham_total_words + alpha * len(vocabulary))

        # using logarithms to avoid underflow
        # underflow is numerical issue of way too small probablities
        spam_score += math.log(spam_prob)
        ham_score += math.log(ham_prob)

    spam_score += math.log(spam_prior)
    ham_score += math.log(ham_prior)

    return 'spam' if spam_score > ham_score else 'ham'

################## TRAIN REGION ##################
ham_data = []
spam_data = []

ham_folder_path = 'spam_data/train/ham'
spam_folder_path = 'spam_data/train/spam'

for filename in os.listdir(ham_folder_path):
    file_path = os.path.join(ham_folder_path, filename)

    # check txt file and utf character 
    if filename.endswith('.txt'):
        with open(file_path, 'r', encoding='latin-1') as file:
            text = file.read()
            ham_data.append((text, "ham"))

for filename in os.listdir(spam_folder_path):
    file_path = os.path.join(spam_folder_path, filename)

    # check txt file and utf character 
    if filename.endswith('.txt'):
        with open(file_path, 'r', encoding='latin-1') as file:
            text = file.read()
            spam_data.append((text, "spam"))

training_data = ham_data + spam_data

# Train the Naive Bayes classifier, alpha is Laplace smoothing
spam_word_counts, ham_word_counts, spam_total_words, ham_total_words, spam_prior, ham_prior, vocabulary, alpha = train_naive_bayes(training_data)

# testing our algorithm at dev data
ham_test_data = []
ham_folder_path = 'spam_data/dev/ham'

for filename in os.listdir(ham_folder_path):
    file_path = os.path.join(ham_folder_path, filename)

    if filename.endswith('.txt'):
        with open(file_path, 'r', encoding='latin-1') as file:
            text = file.read()
            ham_test_data.append(text)

ham_count = 0
spam_count = 0

for mail in ham_test_data:
    classification = classify_naive_bayes(mail, spam_word_counts, ham_word_counts, spam_total_words, ham_total_words, spam_prior, ham_prior, vocabulary, alpha)
    if classification == 'ham':
        ham_count+=1
    else:
        spam_count+=1

print("Percentage of finding ham from ham data :" , ham_count/ (ham_count+spam_count) * 100)


spam_test_data = []
spam_folder_path = 'spam_data/dev/spam'

for filename in os.listdir(spam_folder_path):
    file_path = os.path.join(spam_folder_path, filename)

    if filename.endswith('.txt'):
        with open(file_path, 'r', encoding='latin-1') as file:
            text = file.read()
            spam_test_data.append(text)

ham_count = 0
spam_count = 0

for mail in spam_test_data:
    classification = classify_naive_bayes(mail, spam_word_counts, ham_word_counts, spam_total_words, ham_total_words, spam_prior, ham_prior, vocabulary, alpha)
    if classification == 'spam':
        spam_count+=1
    else:
        ham_count+=1

print("Percentage of finding spam from spam data :" , spam_count/ (ham_count+spam_count) * 100)


