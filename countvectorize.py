# coding: utf-8
import scikit-learn
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
corpus = ['This is the first document', 'This document is the second document', 'And this is third one', 'Is this the first document']
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(corpus)
print("Ensemble du vocabulaire : ", vectorizer.get_feature_names())
