import csv
import pandas as pd
import numpy as np

spam_or_ham = pd.read_csv("spam.csv", encoding='latin-1')[["v1", "v2"]]
spam_or_ham.columns = ["label", "text"]
print(spam_or_ham.head())

print(spam_or_ham["label"].value_counts())


import string
punctuation = set(string.punctuation)
def tokenize(sentence):
    tokens = []
    for token in sentence.split():
        new_token = []
        for character in token:
            if character not in punctuation:
                new_token.append(character.lower())
        if new_token:
            tokens.append("".join(new_token))
    return tokens

spam_or_ham.head()["text"].apply(tokenize)
from sklearn.feature_extraction.text import CountVectorizer
demo_vectorizer = CountVectorizer(
    tokenizer = tokenize,
    binary = True
)

from sklearn.model_selection import train_test_split
train_text, test_text, train_labels, test_labels = train_test_split(spam_or_ham["text"], spam_or_ham["label"], stratify=spam_or_ham["label"])
print(f"Training examples: {len(train_text)}, testing examples {len(test_text)}")

real_vectorizer = CountVectorizer(tokenizer = tokenize, binary=True)
train_X = real_vectorizer.fit_transform(train_text)
test_X = real_vectorizer.transform(test_text)

from sklearn.svm import LinearSVC
classifier = LinearSVC()
classifier.fit(train_X, train_labels)
LinearSVC(C=1.0, class_weight=None, dual=True, fit_intercept=True,
          intercept_scaling=1, loss='squared_hinge', max_iter=1000,
          multi_class='ovr', penalty='l2', random_state=None, tol=0.0001,
          verbose=0)

from sklearn.metrics import accuracy_score
predicciones = classifier.predict(test_X)
accuracy = accuracy_score(test_labels, predicciones)
print(f"Accuracy: {accuracy:.4%}")

frases = [
  'Ha ha ha good joke. Girls are situation seekers',
  'Its a part of checking IQ',
  'Did you hear about the new \Divorce Barbie',
  'Your free ringtone is waiting to be collected. Simply text the password \MIX',
  'i see. When we finish we have loads of loans to pay',
  'How would my ip address test that considering my computer isnt a minecraft server',
  'What is the plural of the noun research?'
]

frases_X = real_vectorizer.transform(frases)
predicciones = classifier.predict(frases_X)

frases_X = real_vectorizer.transform(frases)
predicciones = classifier.predict(frases_X)