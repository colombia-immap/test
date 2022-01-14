import os
import glob
import pandas as pd

all_filenames = ['dataframe_collected_finished_00p.csv',\
'dataframe_collected_finished_01p.csv', 'dataframe_collected_finished_02p.csv']

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "dataframe_collected_finished_peru_cities_jan15.csv", index=False, encoding='utf-8-sig')