
''' =====================================================================================
    CategorizeBook_v2.py
    Author: Donnette Bowler
    copyright: copyright ©Donnette Bowler. All rights reserved. No part of this document may be reproduced or distributed.
    ===================================================================================
    
    A command-line program that gets a text file from a user, processes the file, uses
    a trained classifier to categorize the data, and returns the category to the user.
    
    The program categorizes the manuscript as "emergent reader" or "other".
    
    
    
    ==================================================================================
    
    '''



#import files

import CreateData
from sklearn.externals import joblib
from numpy import *
import numpy as np




#program function
def categorizerApplication():
    startCategorizer()
    answer=raw_input("would you like to classify another manuscript? Y or N: ")
    if (answer=='Y')| (answer=='y'):
        categorizerApplication()
    else:
        print "You quit the program"
        return

#function to get user input, parse file, classify the data, and return result to user
def startCategorizer():
    result_list=['emergent reader','other']
    book_filename=raw_input('manuscript file name: ')
    freq,avg_dis=CreateData.createData(book_filename)
    X=zeros((1,2))
    X[0]=[freq,avg_dis]
   
    #classify unknown data with our model
    clf=joblib.load('model_svm.pkl')
    result=clf.predict(X[0])
    
    
    print 'the book category is: ',result_list[(int(result[0]))-1]
