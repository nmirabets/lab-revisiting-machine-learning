import pandas as pd
import numpy as np
from typing import Dict
import re

def format_column_names(df: pd.DataFrame, column_renames: Dict[str, str] = {} ) -> pd.DataFrame:
    '''

    This function takes a DataFrame and 
    (1) formats column names to lower case, adds underscores before uppercase letters that are preceded by a lowercase letter 
        or followed by a lowercase letter, and replaces white spaces with underscores, and
    (2) renames columns according to the input dictionary.
    
    Inputs:
        df: input DataFrame
        column_renames: Dictionary with column renaming
    
    Outputs:
        formatted DataFrame

    '''
    df_formatted = df.copy()

    # Regular expression pattern for uppercase letters that are preceded by a 
    # lowercase letter or followed by a lowercase letter
    pattern = r'((?<=[a-z])[A-Z]|(?<=[A-Z])[A-Z](?=[a-z]))'

    df_formatted.rename(columns = column_renames, inplace = True) # rename columns according to dictionary
    
    # Replace matched pattern with underscore and the match, also remove whitespaces & lower cased
    df_formatted.columns = [re.sub(pattern, r'_\1', col).lower().replace(' ', '_') for col in df_formatted.columns]

    return df_formatted