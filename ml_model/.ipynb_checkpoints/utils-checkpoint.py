def check_shape(data):
    '''
    An util function to check data shape
    
    Args:
        df (pandas.DataFrame): Input DataFrame.
    '''
    shape = data.shape
    print(f"The data has {shape[0]} rows and {shape[1]} columns")
    
def print_unique_values(df, columns):
    """
    Utility function to print unique values of specified columns in a DataFrame.

    Args:
        df (pandas.DataFrame): Input DataFrame.
        columns (list): List of column names.
    """
    for column in columns:
        unique_values = df[column].unique().tolist()
        print(f"Unique values in column '{column}': {unique_values}")

