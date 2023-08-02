
'''
Author: ittigoon
Date: 220802
'''

import logging
import pandas as pd

logging.basicConfig(
    filename='./production_ready_code/3_logging/results_screencast.log',
    level=logging.INFO,
    filemode='w',
    format='%(name)s -%(levelname)s -%(message)s'
)

def read_data(file_path):
    '''
    Read csv file from file_path
    Args:
        file_path: (str) reading file_path
    Return:
        df: (Dataframe) 
    '''
    try:
        df = pd.read_csv(file_path)
        logging.info('SUCCESS: thier shape are {}'.format(df.shape))
        return df
    except FileNotFoundError:
        logging.error("ERROR: We were not able to find that file")
        return None
if __name__ == "__main__":
    read_df = read_data('./data/winequality-red.csv') #SUCCESS
    read_df = read_data('./data/abc.csv') #ERROR
