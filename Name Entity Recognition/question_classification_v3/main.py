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
from sklearn.linear_model import LogisticRegression


from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB

from sklearn import tree



fr = open('D:\Dropbox\CSE 400\data\question_category_v3\\none\\questionv4.txt',  'r' , encoding="utf8")
ftr1 = open('D:\Dropbox\CSE 400\data\question_category_v3\\none\\wh.txt',  'r' , encoding="utf8")
ftr2 = open('D:\Dropbox\CSE 400\data\question_category_v3\\none\\features.txt',  'r' , encoding="utf8")
ftr3 = open('D:\Dropbox\CSE 400\data\question_category_v3\\none\\featurev1.txt',  'r' , encoding="utf8")
#fw = open('D:\Dropbox\CSE 400\data\question_category_v3\\none\\feature1.txt',  'w' , encoding="utf8")
fw2 = open('D:\Dropbox\CSE 400\data\question_category_v3\\none\\test.txt',  'w' , encoding="utf8")
fwr = open('D:\Dropbox\CSE 400\data\question_category_v3\\none\\result_decision_tree.txt',  'w' , encoding="utf8")


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
	elif(line_no < 486):
		category_list.append("MISC")
	elif(line_no < 676):
		category_list.append("NUM")
	elif(line_no < 927):
		category_list.append("PER")
	elif(line_no < 954):
		category_list.append("REA")
	elif(line_no < 1160):
		category_list.append("TIME")

feature = []




def func(algo):
	num_row = 1160
	fnum = 0

	for line in ftr3:
		fnum = fnum + 1
		words = line.split();
		for item in words:
			feature.append(item)

		#if fnum<=1836:
			#continue

		num_col = len(feature) + 3

		if(algo == 3):
			num_col += 1

		feature_matrix = [[0 for x in range(num_col)] for y in range(num_row)]
		feature_matrix_shuffle = [[0 for x in range(num_col)] for y in range(num_row)]

		for i in range(0,num_row):
			for j in range(0,num_col-4):

				word_list = line_list[i].split();
				for item in word_list:
					if item==feature[j]:
						feature_matrix[i][j] = 1
					if(item in freq):
						freq[item] += 1;
					else:
						freq[item] = 1;

		# for key, value in sorted(freq.items(), key=lambda kv: (-kv[1], kv[0])):
		# 	fw.write(key+"\n")

		if(algo == 1):
			svm_model = svm.SVC(kernel='poly', C=1)
			cv = ShuffleSplit(n_splits=5, test_size=0.1, random_state=0)
			scores = cross_val_score(svm_model, feature_matrix, category_list, cv=cv)
			predicted = cross_val_predict(svm_model, feature_matrix, category_list, cv=cv)
			acc_score = metrics.accuracy_score(category_list, predicted)
			print(acc_score)
			#print(type(scores))
			fwr.write(str(fnum))
			avg = 0.0;
			best = 0;
			worst = 100;

			for item in scores:
				percent = item*100
				if percent>best:
					best = percent
				if percent<worst:
					worst = percent

				avg = avg + percent
				fwr.write(" "+str(percent))

			avg = avg/5.0
			fwr.write(" "+str(worst)+" "+str(best)+" "+str(avg)+"\n")

		
		if(algo == 2):
			logreg_model = LogisticRegression(C=1e5)
			cv = ShuffleSplit(n_splits=5, test_size=0.3, random_state=0)
			scores = cross_val_score(logreg_model, feature_matrix, category_list, cv=cv)
			#print(scores)
			#print(type(scores))
			fwr.write(str(fnum))
			avg = 0.0;
			best = 0;
			worst = 100;

			for item in scores:
				percent = item*100
				if percent>best:
					best = percent
				if percent<worst:
					worst = percent

				avg = avg + percent
				fwr.write(" "+str(percent))

			avg = avg/5.0
			fwr.write(" "+str(worst)+" "+str(best)+" "+str(avg)+"\n")

		if(algo == 3):
			nb_model = GaussianNB()
			cv = ShuffleSplit(n_splits=5, test_size=0.3, random_state=0)
			scores = cross_val_score(nb_model, feature_matrix, category_list, cv=cv)
			#print(scores)
			#print(type(scores))
			fwr.write(str(fnum))
			avg = 0.0;
			best = 0;
			worst = 100;

			for item in scores:
				percent = item*100
				if percent>best:
					best = percent
				if percent<worst:
					worst = percent

				avg = avg + percent
				fwr.write(" "+str(percent))

			avg = avg/5.0
			fwr.write(" "+str(worst)+" "+str(best)+" "+str(avg)+"\n")


		if(algo == 4):
			dec_tree = tree.DecisionTreeClassifier()
			cv = ShuffleSplit(n_splits=5, test_size=0.3, random_state=0)
			scores = cross_val_score(dec_tree, feature_matrix, category_list, cv=cv)
			#print(scores)
			#print(type(scores))
			fwr.write(str(fnum))
			avg = 0.0;
			best = 0;
			worst = 100;

			for item in scores:
				percent = item*100
				if percent>best:
					best = percent
				if percent<worst:
					worst = percent

				avg = avg + percent
				fwr.write(" "+str(percent))

			avg = avg/5.0
			fwr.write(" "+str(worst)+" "+str(best)+" "+str(avg)+"\n")


		if(algo == 5):
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

