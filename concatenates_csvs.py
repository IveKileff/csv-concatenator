'''imports all csv files in the directory into dataframes, adds the
   filename to each dataframe, then concatenates them''' 

import pandas as pd
import glob

# read all filenames
all_filenames = [i for i in glob.glob('*.csv')]

# extract root name of files
names = [file[:-4] for file in all_filenames]

'''read the file into a dataframe, add the filename to the dataframe,
   create a list of these dataframes'''
df_list = []
for f in names:
    df_name = f+'_df'
    print(f'Processing {f}')
    df_name = pd.read_csv(f + '.csv')
    df_name['filename'] = f + '.csv'
    df_list.append(df_name)
   
'''concatenates dataframes into combined_new (pd.concat method
   concatenates the files based on the column names)'''
combined_new = pd.concat(df for df in df_list)

'''export to csv; index=True is default, means write row names,
   I've set to False as I don't have row names'''
combined_new.to_csv("combined_new.csv", index=False)
print('Created combined_new.csv')
