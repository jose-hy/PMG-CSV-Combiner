import sys
import pandas as pd
from pathlib import Path

NUM_CSV_ARGS = len(sys.argv) - 1



# function: command_line_grab():
    # i. Checks if there is a correct amount of .csv files to combine
    # ii. Silently continues if a .csv file in sys.argv does not exist
    # iii. Returns a dictionary of pandas read_csv objects as values, and
        # their filename as keys
def command_line_grab():
    
    if (NUM_CSV_ARGS <= 1):
        sys.exit("Must include at least two .csv files in command line "
                "argument")

    pd_csv = {}
    
    for files in sys.argv:
        if len(files) <= 4:
            sys.exit("Command Line arguments must contain .csv")
    
        if '.csv' in files:
            filename = files[ (files.index('/') + 1):files.index('.') ]
            
            try:
                pd_csv[filename] = pd.read_csv(files)
            except FileNotFoundError:
                continue

    return pd_csv

# function: add_filename_column():
    # i. Requires a dictionary of panda dataframe objects
    # ii. Creates the new 'filename' column and set all values to the
        # name of the .csv file
    # iii. Returns the same dictionary with edited dataframe objects
def add_filename_column(csv_dict):

    for name, obj in csv_dict.items():
        obj['filename'] = name
    return csv_dict

# function: the_big_merge():
    # i. Requires a dictionary of panda dataframe objects
    # ii. Merge all the objects in the dictionary to a new bigger dataframe
    # iii. Returns the big dataframe
def the_big_merge(csv_dict):

    csv_list = []
    for vals in csv_dict.values():
        csv_list.append(vals)
        
    first_merge = csv_list[0]
    
    for val in csv_dict.values():
        if ( first_merge.equals(val) ):
            continue
        
        first_merge = first_merge.merge(val, how='outer')

    return first_merge

# function: write_out():
    # i. Requires a dataframe object that contains all the .csv files' data
    # ii. Saves the dataframe to a new .csv file, 'combiner.csv'
    # iii. Returns an output of the .csv file as a dataframe object
def write_out(big_merge):

    combiner_path = Path('fixtures/combiner.csv')
    big_merge.to_csv(combiner_path, index=False)

    return print(big_merge)



csv_obj = command_line_grab()
csv_obj = add_filename_column(csv_obj)
all_df = the_big_merge(csv_obj)
write_out(all_df)
