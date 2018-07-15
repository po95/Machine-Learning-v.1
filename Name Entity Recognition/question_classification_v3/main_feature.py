import pickle
from sklearn.externals import joblib
import codecs
from collections import defaultdict
import csv
import sys
import csv
import codecs
import operator
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.metrics import accuracy_score
import pickle
from sklearn.externals import joblib
from sklearn.datasets import load_files
import math
from sklearn import datasets, linear_model
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.model_selection import ShuffleSplit


import numpy as np
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

from nltk import ngrams


from sklearn import metrics
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.linear_model import LogisticRegression


from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB


from sklearn import tree



fr = open('D:\Dropbox\CSE 400\data\question_category_v3\\none\\questionv4.txt',  'r' , encoding="utf8")
ftr1 = open('D:\Dropbox\CSE 400\data\question_category_v3\\none\\wh.txt',  'r' , encoding="utf8")
ftr2 = open('D:\Dropbox\CSE 400\data\question_category_v3\\none\\features.txt',  'r' , encoding="utf8")
ftr3 = open('D:\Dropbox\CSE 400\data\question_category_v3\\none\\featurev1.txt',  'r' , encoding="utf8")
fw = open('D:\Dropbox\CSE 400\data\question_category_v3\\none\\feature1.txt',  'w' , encoding="utf8")
fw2 = open('D:\Dropbox\CSE 400\data\question_category_v3\\none\\test.txt',  'w' , encoding="utf8")


category_list = []
line_list = []
freq = dict()

for line in fr:
	line_list.append(line)

for line_no in range(0,1160):
	if(line_no < 34):
		category_list.append("DEF")
	elif(line_no < 105):
		category_list.append("GRO")
	elif(line_no < 318):
		category_list.append("LOC")
	elif(line_no < 334):
		category_list.append("METH")
	# elif(line_no < 412):
	# 	category_list.append("MISC1")
	elif(line_no < 486):
		category_list.append("MISC2")
	elif(line_no < 676):
		category_list.append("NUM")
	elif(line_no < 927):
		category_list.append("PER")
	elif(line_no < 954):
		category_list.append("REA")
	elif(line_no < 1160):
		category_list.append("TIME")


feature = []

for line in ftr1:
	words = line.split();
	for item in words:
		feature.append(item)

for line in ftr2:
	words = line.split();
	for item in words:
		feature.append(item)

# for line in ftr3:
# 	words = line.split();
# 	for item in words:
# 		feature.append(item)



def func(algo):

	num_row = 1160
	num_col = len(feature) + 3

	if(algo == 3):
		num_col += 1

	feature_matrix = [[0 for x in range(num_col)] for y in range(num_row)]
	feature_matrix_shuffle = [[0 for x in range(num_col)] for y in range(num_row)]

	for i in range(0,num_row):
		for j in range(0,num_col-4):
			# if(algo == 2 and j == num_col - 1):
			# 	feature_matrix[i][j] = feature[i]
			# 	continue

			word_list = line_list[i].split();
			for item in word_list:
				if item==feature[j]:
					feature_matrix[i][j] = 1
				if(item in freq):
					freq[item] += 1;
				else:
					freq[item] = 1;
	
		f = 0
		'''
		for k in range(0,18):
			if(word_list[0]==feature[k]):
				feature_matrix[i][num_col - 1] = 1
				fw2.write("first \n");
				f = 1
				break
			# elif(word_list[1]==feature[k]):
			# 	fw2.write("after first \n");
			# 	f = 1
			# 	break
			elif(word_list[-1]==feature[k]):
				feature_matrix[i][num_col - 2] = 1
				fw2.write("last \n");
				f = 1
				break
			elif(word_list[-2]==feature[k]):
				feature_matrix[i][num_col - 3] = 1
				fw2.write("before last \n");
				f = 1
				break

		if(f == 0):
			#feature_matrix[i][num_col - 1] = 4
			fw2.write("none\n");
		'''
	#feature_matrix[i][num_col - 4] = len(word_list)

	#sorted_x = sorted(freq.items(), key=operator.itemgetter(1))
	#print(type(sorted_x))
	#print(type(freq))
	#for item in sorted_x:
	#	fw.write(item)


	#for key, value in sorted(freq.items(), key=lambda kv: (-kv[1], kv[0])):
	#	fw.write(key+"\n")

	if(algo == 1):
		svm_model = svm.SVC(kernel='linear', C=1)
		cv = ShuffleSplit(n_splits=5, test_size=0.1, random_state=0)
		scores = cross_val_score(svm_model, feature_matrix, category_list, cv=cv)
		#predicted = cross_val_predict(svm_model, feature_matrix, category_list, cv=cv)
		#acc_score = metrics.accuracy_score(category_list, predicted)
		#print(acc_score)
		print(scores)
		avg = 0.0;
		for item in scores:
			avg += item
		avg = avg/5.0
		print(avg) 

	
	if(algo == 2):
		logreg_model = LogisticRegression(C=1e5)
		cv = ShuffleSplit(n_splits=5, test_size=0.3, random_state=0)
		scores = cross_val_score(logreg_model, feature_matrix, category_list, cv=cv)
		print(scores)

		avg = 0.0;
		for item in scores:
			avg += item
		avg = avg/5.0
		print(avg) 

	if(algo == 3):
		nb = GaussianNB()
		cv = ShuffleSplit(n_splits=5, test_size=0.3, random_state=0)
		scores = cross_val_score(nb, feature_matrix, category_list, cv=cv)
		print(scores)

		avg = 0.0;
		for item in scores:
			avg += item
		avg = avg/5.0
		print(avg) 

	if(algo == 4):
		tr = tree.DecisionTreeClassifier()
		cv = ShuffleSplit(n_splits=5, test_size=0.3, random_state=0)
		scores = cross_val_score(tr, feature_matrix, category_list, cv=cv)
		print(scores)

		avg = 0.0;
		for item in scores:
			avg += item
		avg = avg/5.0
		print(avg) 

	if(algo == 6):
		feature_matrix_shuffle = feature_matrix
		np.random.shuffle(feature_matrix_shuffle)
		train = 1960
		language_list_shuffle = []

		for i in range(0,num_row_word):
			language_list_shuffle.append(feature_matrix_shuffle[i][num_col - 1])

		for row in feature_matrix_shuffle:
			del row[num_col - 1]

		trainMatrix = feature_matrix_shuffle[:train]
		testMatrix = feature_matrix_shuffle[train:]
		trainLabel = language_list_shuffle[:train]
		testLabel = language_list_shuffle[train:]
		

		clf = GaussianNB()
		clf.fit(trainMatrix, trainLabel)
		predicted = clf.predict(testMatrix)
		print(accuracy_score(testLabel,predicted))
		print(predicted)

func(4)

#func_character_gram(1,200,2)