
''' ===================================================================================================================
    MyLinguisticAnalysis.py
    Author: Donnette Bowler
    copyright: copyright © Donnette Bowler 2016. All rights resevered. No part of this document may be reproduced or distributed.
    ==================================================================================================================
    
    This contains helper functions to perform linguisitic analysis of text files.
    
    
    Create a binary map of words in the string. Calculate frequency of each word (of course,
    here I could have used  libraries eg. nltk- natural language toolkit,
    and other scientific libraries to get word frequencies, but I thought it would be fun to create my own.
    I also wrote a reverse mapping function to recreate the original string.
    I used the binary map to calculate word frequencies and word distances).
    
    ===================================================================================================================
    
    '''



"""this contains functions to perform linguistic analysis of interests."""



def items_same(m,n):
    """compares two items and returns a list"""
    if m==n:
        return True



def thenAddToList(n,aList):
    """returns appended list"""
    blist=aList.append(n)
    return blist



def makeDict(aList):
    
    #if list is empty
    if len(aList)== 0:
        return None #return none
    
    #else create a dictionary to store values
    else:
        aDict={}
        for item in aList:
            if item not in aDict: #if the item is not in the dictionary
                aDict[item]=[]
    
        return aDict





def findMatches(alist,aDict):
    """counts the number of times a key in a dictionary, aDict, appear in a list, alist"""
    bDict=aDict
    #if the list, alist or the dictionary, aDict is empty, then return none
    if len(alist)==0 | len(bDict)==0:
        return None

    else:
        word_loc=[] #initialize list to store word location of each item (binary)
        v=0

        #count the number of times a key appears in alist and append it to aDict[key]
        counter=0
        for key in bDict:
            counter=0
            v=0
            for item in alist:
                
                #print "comparing key:, %s and item:, %s " %(key,item)
                if key==item:
                    counter=counter+1
                    v=counter
                    
                    #print "match found, %d", v
                else:
                    e=1
                    #print "no match found. counter is still: %d" % (v )
                    #v+=counter
            bDict[key]=v
            rDict=bDict

    return rDict



def keyMap(alist,aDict):
    '''this function takes a list and a map of unique items. the function creates a binary map of list to dictionary.
        this will make analysis easier. Each key contains its own binary map'''

    bDict=aDict
    #if the list, alist or the dictionary, aDict is empty, then return none
    if len(alist)==0 | len(bDict)==0:
        return None

    else:
        word_loc=[] #initialize list to store word location of each item (binary)
        v=0
        
        loc=0
        
        #count the number of times a key appears in alist and append it to aDict[key]
        counter=0
        for key in bDict:
            counter=0
            v=0
            word_loc=[]
            
            for item in alist:
                
                # print "comparing key:, %s and item:, %s " %(key,item)
                if key==item:
                    counter=counter+1
                    v=counter
                    # print "match found, %d", v
                    loc=1
                    word_loc.append(loc)
                else:
                    
                    #print "no match found. counter is still: %d" % (v )
                    loc=0
                    word_loc.append(loc)
                #add v to word_loc list
                
                
            bDict[key]=word_loc
            rDict=bDict

        return rDict


def lengthDictItem(rDict):
    count=0

    for key in rDict:
        
        alist=rDict[key]
        for item in alist:
            count=count+1

        return count




def reverseKeyMap(rDict):
    '''this is a function to reverse or translate the keyMap with a dictionary. used for translation and also to verify that the mapping function
        was correct'''
    fx=rDict
    slist=[""]*lengthDictItem(fx)
    rlist=[]
    if len(fx)==0:
        return None
    else:
        #for every key in fx, for every item in list
        for key in fx:
            counter=0 #keeps track of location in list
            alist=[]
            blist=slist
            alist=fx[key]
            loc_index=0
            for item in alist:
                #print "finding: ", key
                
            #find where item equals 1, and return its position as value of loc_index
                if item==1:
                    loc_index=counter
                    # print "location: ",loc_index
                
                
                
                    if loc_index==0:
                        blist[0]=key
                    # print blist
                    else:
                        # print "loc_index-1: ",loc_index-1
                        blist[loc_index]=key
                #print blist
                counter=counter+1
                #print "counter: ",counter
            rlist=blist

    return rlist





def calculateKeyFreq(aDict):
    '''this function keeps a count of the instances it encounters a '1' for each list in 
        the key in the dictionary. it returns a new dictionary with this count for each key'''

    bDict=aDict
    rDict={}
    if len(bDict)==0:
        #print "returning none. length of bDict: ", len(bDict)
        return None
    else:
        for key in bDict:
            alist=[]
            alist=bDict[key]
            # print "alist: ",alist
            counter=0 #initialize the counter to 0
            #for every item in the list, when item==1, increase counter
            for item in alist:
                # print "item: ",item
                if item==1:
                    counter=counter+1 #increment the counter by 1
            rDict[key]=counter #store the counter value in the dictionary at the key
        return rDict




def calDist(a_sublist):
    
    length=len(a_sublist)
    dist=0
    val=0
    rlist=[]
    #print "length of sublist: ", len(a_sublist)
    if len(a_sublist)==1:
        val=0
        rlist.append(val)
        return rlist

    for item in a_sublist:
        counter=0
        if counter!=len(a_sublist):
            val=(a_sublist[counter+1]-a_sublist[counter])-1
            rlist.append(val)
        else:
            rlist.append(val)
            return val
        counter=counter+1

    return rlist





def calculateItemDist(aDict):
    '''this function  calculates the distance between two items, where items==1'''
    bDict=aDict
    freq_list=[]
    occur_list=[]
    rDict={}
    rm=0
    rn=0
    if len(aDict)==0:
        return None
    else:
        #for key in bDict, get the frequency of 1's, and create a list of length frequency-1
        fDict={}
        fDict=calculateKeyFreq(bDict)
        for key in bDict:
            alist=[]
            alist=bDict[key]
            # print "key: ",key
            
            if fDict[key]==1:
                freq_list=[]
                freq_list.append(0)
        
            
            
            else:
                acounter=0
                bcounter=0
                m =0
                n=0
                dist=0
                #print "fdict[key]: ",fDict[key]
                val=fDict[key]
                freq_list=[]  #create a frequency list
                #print "freq list: ",len(freq_list)
                #calculate distance
                for item in alist:
                   
                    m=0
                    n=0
                    
                    if item==1 :
                        m=acounter
                            
                        rm=m
                        # print "acounter: ",acounter
                            
                            #print "rm: ",rm
                            
                        freq_list.append(rm)
                            
                            #print " the same"
                    acounter=acounter+1
                    #print "bcounter: ",bcounter
                    
                    
                    #print "acounter: ",acounter
                    
                   
                   
            rDict[key]=freq_list
            rDict[key]=calDist(freq_list)
        return rDict






        
        
        
        







def calculateAvgDist(aDict):
    '''this function calculates the average distance between repeating words'''
    bDict=aDict
    length_list=0
    item_distance=0
    if len(bDict)==0:
        return None

    else:
        #for key in bDict, get the length of the list, and add the items (integers) in the list
        for key in bDict:
            alist=[]
            alist=bDict[key]
            length_list+=len(bDict[key])
            for item in alist:
                get_item=item
                item_distance+=get_item
        average_distance=item_distance/length_list
        return average_distance







def avgDist(aDict):
    rDict={}
    for key in aDict:
        counter=0
        item=0
        num=0
        alist=aDict[key]
        for item in alist:
            num=num+item
            counter=counter+1
        rDict[key]=num/counter
    return rDict











def gatherAnalysis(alist):
    #calls methods to gather analysis, and returns a dictionary containing all analysis
    
    blist=alist
    
    summary_analysis={}
    a=makeDict(blist)
    b=findMatches(blist,a)
    c=keyMap(alist,b)
    # print "map: ", c
    
    
   
    d=calculateKeyFreq(c)
    #print "frequencies: ",d
    e=calculateItemDist(c )
    #print "word distances: ",e
    f=avgDist(e)
    summary_analysis['map']=c
    summary_analysis['frequencies']=d
    summary_analysis['distances']=e
    summary_analysis['average_distance']=f
    
    sumthis=0
    sumDist=0
    count_1=0
    count_2=0
    #print "before loop in dict"
    
    sumanl=summary_analysis['frequencies']
    for key in sumanl:
        
        val=sumanl.get(key,0)
        #print "this is the value: ",val
        sumthis+=val
        count_1+=1
    
    for key in summary_analysis['average_distance']:
        val=summary_analysis['average_distance'].get(key,0)
        #print "this is the value for average distance: ",val
        sumDist+=val
        count_2+=1
    
# print "sumthis: ",sumthis
# print "count: ",count_1
#print "sumdis: ",sumDist

    eval_1=float(sumthis)/float(count_1)
    eval_2=float(sumDist/count_2)
    summary_analysis['total_frequency']=eval_1
    summary_analysis['total_average_distance']=eval_2


    
   
    
    #summary_analysis= reverseKeyMap(c)
    
    return summary_analysis
















def testDefinitions():
    T=['hello','are','you','okay','you','okay']
    analysis=gatherAnalysis(T)
    
    return analysis
            
