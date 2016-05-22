# -*- coding: utf-8 -*-
"""
Created on Tue May 17 20:34:04 2016

@author: Michael Pastorino
"""
import preprocessing
import calculations # calculations.py imports kaggle.py
from datetime import datetime # for printing execution time of various stages of the program

listenersTotalPlays = {} # keys are listenerIDs, values are total play count for corresponding listener
listenersSongs = {} # keys are listenerIDs, values are dictionaries of songs : play counts per each that this listener listened to
songsListeners = {} # kes are songIDs, valus are dictionaries of listener : play counts per each listener that listened to this song
# basically, listenersSongs and songsListeners are 2 ways of looking at the same data -- need to store both for impact on MUCH simplying
# later similarity calculations

print "Populating training data @", datetime.now()
preprocessing.populateTrainStorage("../train_triplets.txt", listenersTotalPlays, listenersSongs, songsListeners)

print "Populating test data @", datetime.now()
# returns set of TEST listeners' IDs
testListeners = preprocessing.populateTestStorage("../year1_test_triplets_visible-test.txt", listenersTotalPlays, listenersSongs, songsListeners)

print "Making recommendations @", datetime.now()
listenersRecs = calculations.calcSimsAndRecommend(testListeners, listenersTotalPlays, listenersSongs, songsListeners, .3)

print "Populating answers data @", datetime.now()
listenersAnswersLists = preprocessing.populateAnswersStorage("../year1_test_triplets_visible-hidden.txt")

print "Calculating MAP @", datetime.now()
print calculations.calcMeanAveragePrecision(listenersRecs, listenersAnswersLists)