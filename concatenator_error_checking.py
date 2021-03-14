'''find files which have problems with the data.
   - One had /r which caused a problem
   - One had a number cell formatted as a date
   program aims to import all csv files in the directory and
   concatenate them''' 

import pandas as pd
import glob
import os
import traceback

cwd = os.getcwd()
mod = cwd + '/Modified'

'''read all filenames'''
all_filenames = [i for i in glob.glob('*.csv')]

'''extract root name of files'''
names = [file[:-4] for file in all_filenames]

"""add the filename to a column in each file and save the result as
   'Modified\namemod.csv'"""
for f in names:
    try:
        print(f'trying {f}')
        df = pd.read_csv(f+'.csv')
        df['filename'] = f+'.csv'
        os.chdir(mod)
        df.to_csv(f+'mod.csv')
        os.chdir(cwd)
    except:
        print(f'error with {f}')
        traceback.print_exc()
    

