
''' ===================================================================================
    
    dataBookViz.py
    Author: Donnette Bowler
    copyright: copyright ©Donnette Bowler 2016. All rights reserved. No part of this document may be reproduced or distributed.
    ===================================================================================
    
    Use pandas dataframe to store data. We create a scatter plot with Matplotlib to
    analyze our data.
    
    
    
    
    =======================================================
    
    '''




#scientific Python imports
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

def createViz():
    
    input_dir="./testData/"
    filename="testData.txt"
   
    full_name=os.path.join(input_dir,filename)
    df=pd.read_csv(full_name,'\t')
    print df
    print type(df)
    df.columns=['freq','distance','category']
    
    
    df.plot(kind="scatter",x='freq',y='distance',c='category',s=50)
    plt.show()
