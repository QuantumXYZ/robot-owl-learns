''' ===========================================================================================================
    CreateData.py
    Author: Donnette Bowler
    copyright: copyright © Donnette Bowler 2016. All rights reserved. No part of this document may be reproduced or distributed.
    ==================================================================================================
    
    I wrote functions to collect data from text files of manuscripts.
    The manuscripts are text files in string format. Essentially these functions load
    all manuscript or book files in a directory, open and read into a string. break string into a list.
    
    I wrote a function to categorize books based on a threshold ratio of average
    frequency of repeating words to average distance between each repeating word.
    I used this function to categorize the books. Each books average frequency and
    average distance, and book category was output to a text file.
    ========================================================================================================================
    
'''



#scientific Python imports
import numpy as np
import pandas as pd
import os


#dependent Python imports
import MyLinguisticAnalysis_2 as MLA




def createTestData():
    input_dir='./textBooks/'
    files=os.listdir(input_dir)
    test_input_dir='./testData/'
    test_files=os.listdir(test_input_dir)
    freq_result_list=[]
    avg_dis_result_list=[]
    category_book_result_list=[]
    for f in files:
        str_list=[]
        print 'thses are the files in your directory: ', f
        full_name=os.path.join(input_dir,f )
        fr=open(full_name)#open and read files
        str=fr.read()
        #get substring
        
        str_list=str.split()
        print "text: ", str_list
        #perform a binary map creation on each files that maps word repeats
        analysis=MLA.gatherAnalysis(str_list)
        
        #print " this is the analysis on the text file: ", analysis
        # print "this is frequency: ",analysis['frequencies']
        #print "this is average distance: ", analysis['average_distance']
        
        freq =analysis['total_frequency']
        avg_dis=analysis['total_average_distance']
        #get category of book
        if avg_dis==0:
            category_book=1
        else:
            category_book=compareThreshValue(freq,avg_dis)
        print 'this is the book category: ',category_book
        freq_result_list.append(freq)
        avg_dis_result_list.append(avg_dis)
        category_book_result_list.append(category_book)

        #create a pandas table to hold analytics (frequency, average distance)

        #output that analysis to testData.txt file
        #get data from testData.txt file, categorize based on threshold value, and append to testData.txt
    s=pd.DataFrame.from_items([('',freq_result_list),('',avg_dis_result_list),('',category_book_result_list)])
    s.to_csv(os.path.join(test_input_dir,'testData.txt'),index=False,sep='\t')




def createData(filename):
    input_dir='./tbooks/'
    full_name=os.path.join(input_dir,filename)
    fr=open(full_name)
    str=fr.read()
    str_list=str.split()
    print 'text: ', str_list
    #perform a binary map creation on each files that maps word repeats
    analysis=MLA.gatherAnalysis(str_list)
    #print " this is the analysis on the text file: ", analysis
    # print "this is frequency: ",analysis['frequencies']
    #print "this is average distance: ", analysis['average_distance']
    freq =analysis['total_frequency']
    avg_dis=analysis['total_average_distance']
    return freq,avg_dis



def compareThreshValue(freq,dis): #threshold value is 1.6. higher the frequency and lesser the distance the value increases
    value= freq/dis
    print 'this is the value: ',value
    if value >0.6 :
        return 1
    if value <0.6:
        return 2
    if value ==0.6:
        return 1



def mla():
    analysis=MLA.testDefinitions()
    print 'this is the result of the test: ', analysis





