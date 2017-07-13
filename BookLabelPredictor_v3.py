''' ======================================================================================================
    BookLabelPredictor_v3.py
    Author: Donnette Bowler
    copyright: copyright © Donnette Bowler 2016. All rights reserved. No part of this document may be reproduced or distributed.
    ===================================================================================
    
    The data that we are interested in is stored in a text file.
    First we load the data into numpy array of form (n-samples,features),
    where features are a 2D numpy array, and n-samples is the number of lines
    in the file. The last column of the file represents the target labels of the data.
    
    This predictor uses k-nearest neighbours to predict a label
    on a new book.
    
    
    
    
    =============================================================================================
'''


#standard scientific Python imports
import matplotlib.pyplot as plt
from numpy import *
import numpy as np


#import classifiers and performance metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn import linear_model,neighbors,svm
from sklearn.externals import joblib


import os



# a function that loads the data from a text file into arrays
def loadData():
    
    input_dir="./testData"
    filename="testData.txt"
    full_name=os.path.join(input_dir,filename)
    fr=open(full_name)
    number_of_lines=len(fr.readlines()) #get the number of lines in text file for the number of observations
    book_X=zeros((number_of_lines,2)) # initialize an 2D array and fill with zeros
    book_Y=zeros((number_of_lines,)) #initialize a 1D array and fill with zeroes
    
    index=0
    fr=open(full_name)
    for line in fr.readlines():
        
        line=line.strip()
        list_from_line=line.split('\t')
        book_X[index,:]=list_from_line[0:2] #array of features
        
        book_Y[index:,]=list_from_line[-1] #array of category or target values
        
        index+=1
   
    return book_X,book_Y



# a function to create an array of randomly ordered indices
def permutateData(input_list):
    np.random.seed(0) #set the random seed
    indices=np.random.permutation(len(input_list)) #randomly order the indices
    return indices


#create a classifier: nearest-neighbor classifier
def classify0():
    bookX,bookY=loadData()
    
    book_indices=permutateData(bookX) #create a random list of indices
    
    
    n_samples=len(bookX)
    
    #take a subset of the data for training the classifier
    book_X_train=bookX[:0.5*n_samples]
    book_Y_train=bookY[:0.5*n_samples]
    #take a subset of the data for testing the classifier
    book_X_test=bookX[0.5*n_samples:]
    book_Y_test=bookY[0.5*n_samples:]
   
    
    #create a classifier
    knn=KNeighborsClassifier(n_neighbors=5)
    
    #train the classifier with training data
    v=knn.fit(book_X_train,book_Y_train)
    #use the trained classifier on the test data set to predict target values
    prediction=knn.predict(book_X_test)
    actual=book_Y_test

    #compare the predicted target values with the actual target values of the data
    print "predicted values: ", prediction
    print "actual values: ", actual
    print v
    #score the performance of the KNN classifier
    print ('KNN score: %f' %knn.fit(book_X_train,book_Y_train).score(book_X_test,book_Y_test))
    #pickle the trained classifier
    joblib.dump(v,'model_knn.plk')







def modelBook_Regression():
    bookX,bookY=loadData() #load the data
    
    book_indices=permutateData(bookX) #create a random list of indices
    
    
    n_samples=len(bookX)
    
    #take a subset of the data for training the classifier
    book_X_train=bookX[:0.5*n_samples]
    book_Y_train=bookY[:0.5*n_samples]
    #take a subset of the data for testing the classifier
    book_X_test=bookX[0.5*n_samples:]
    book_Y_test=bookY[0.5*n_samples:]
    
    #create a classifier
    logistic=linear_model.LogisticRegression()
        #fit the data to the regression line and score its performance.
    print ('logisticsRegression score: %f' % logistic.fit(book_X_train,book_Y_train).score(book_X_test,book_Y_test))
    
    #linear regression on data
    regr=linear_model.LinearRegression()
    
    #fit training data
    regr.fit(book_X_train,book_Y_train)

    #score the performance of classifier and print the result to the screen
    print "regression score: (note a variance score of 1 is perfect prediction and 0 means no linear relationship): ", regr.score(book_X_test,book_Y_test)

    #pickle the trained classifier
    joblib.dump(regr,'model_regression.pkl')


def modelBook():

    bookX,bookY=loadData()
    
    book_indices=permutateData(bookX)
    print book_indices,len(bookX),len(bookY)
    
    n_samples=len(bookX)
    
    #take 50% of data for training classifier
    book_X_train=bookX[:0.5*n_samples]
    
    book_Y_train=bookY[:0.5*n_samples]
    
    #take 50% of data for testing classifier
    book_X_test=bookX[0.5*n_samples:]
    
    book_Y_test=bookY[0.5*n_samples:]
    
    #create a classifier
    clf=svm.SVC()
    #train the classifier
    clf.fit(book_X_train,book_Y_train)
    
    
       #pickle the trained classifier
    joblib.dump(clf,'model_svm.pkl')




# a function that outputs graphs for visual inspection of classified data based on support vector machines
def dataViz_SVM():

    bookX,bookY=loadData()
    
    book_indices=permutateData(bookX)
    print book_indices,len(bookX),len(bookY)
    
    n_samples=len(bookX)
    
    #take 50% of data for training classifier
    book_X_train=bookX[:0.5*n_samples]
    
    book_Y_train=bookY[:0.5*n_samples]
    
    #take 50% of data for testing classifier
    book_X_test=bookX[0.5*n_samples:]
    
    book_Y_test=bookY[0.5*n_samples:]
    
    #fit the model
    for fig_num,kernel in enumerate(('linear','rbf','poly')):
        clf=svm.SVC(kernel=kernel,gamma=10)
        clf.fit(book_X_train,book_Y_train)

        plt.figure(fig_num)
        plt.clf()
        plt.scatter(bookX[:,0],bookX[:,1],c=bookY,zorder=10,cmap=plt.cm.Paired)

#circle out the test data
        plt.scatter(book_X_test[:,0],book_X_test[:,1],s=80,facecolors='none',zorder=10)

        plt.axis('tight')
        x_min=bookX[:,0].min()
        x_max=bookX[:,0].max()
        y_min=bookX[:,1].min()
        y_max=bookX[:,1].max()

        XX,YY=np.mgrid[x_min:x_max:200j,y_min:y_max:200j]
        Z =clf.decision_function(np.c_[XX.ravel(),YY.ravel()])

#put the result into a color plot
        Z =Z .reshape(XX.shape)
        plt.pcolormesh(XX,YY,Z >0,cmap=plt.cm.Paired)
        plt.contour(XX,YY,Z,colors=['k','k','k'],linestyles=['--','-','--'],level=[-0.5,0,0.5])
        plt.title(kernel)
    plt.show()









