# Perceptron learning algorithm 
# sepal_labels = ["sepal_length","sepal_width","petal_length","petal_width"]

label_mapping = {"Iris-setosa": 0, "Iris-versicolor": 1}

# Train data
data = []

with open('IRIS.txt', 'r') as file:
    for line in file:
        line = line.strip().split(',')
        features = [float(x) for x in line[:-1]]
        label = line[-1]
        data.append((features, label))

# Perceptron training algorithm
num_features = len(data[0][0])
weights = [0.0] * num_features
bias = 0.0
learning_rate = 0.01
num_epochs = 2

for epoch in range(num_epochs):
    correct_predictions = 0

    for features, label in data:
        weighted_sum = sum(w * x for w, x in zip(weights, features)) + bias
        predicted = 1 if weighted_sum > 0 else 0
        error = label_mapping[label] - predicted

        if error == 0:
            correct_predictions += 1
        else:
            weights = [w + learning_rate * error * x for w, x in zip(weights, features)]
            bias += learning_rate * error

    if correct_predictions == len(data):
        break

# Test data
test_data = []

with open('IRISTest.txt', 'r') as file:
    for line in file:
        line = line.strip().split(',')
        features = [float(x) for x in line[:-1]]
        label = line[-1]
        test_data.append((features, label))

correct_predictions = 0

for features, label in test_data:
    weighted_sum = sum(w * x for w, x in zip(weights, features)) + bias
    predicted = 1 if weighted_sum > 0 else 0
    if predicted == label_mapping[label]:
        correct_predictions += 1

accuracy = correct_predictions / len(test_data)
print(f"Accuracy: {accuracy * 100}%")
