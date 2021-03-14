'''imports all csv files in the directory, adds a column with the
   filename, saves each file, then re-imports and concatenates them
   ''' 

import pandas as pd
import glob
import os

cwd = os.getcwd()
mod = cwd + '/Modified'

'''read all filenames'''
all_filenames = [i for i in glob.glob('*.csv')]

'''extract root name of files'''
names = [file[:-4] for file in all_filenames]

"""add the filename to a column in each file and save the result as
   'Modified\namemod.csv'"""
for f in names:
        print(f'trying {f}')
        df = pd.read_csv(f+'.csv')
        df['filename'] = f+'.csv'
        os.chdir(mod)
        df.to_csv(f+'mod.csv')
        os.chdir(cwd)
    
'''combine all files in the list; the pd.concat method concatenates
   the files based on the column names'''
os.chdir(mod)
mod_filenames = [i for i in glob.glob('*.csv')]
combined = pd.concat([pd.read_csv(f) for f in mod_filenames ])

'''export to csv; index=True is default, means write row names,
   I've set to False as I don't have row names'''
combined.to_csv("combined.csv", index=False)
