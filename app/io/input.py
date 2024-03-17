from os import path
from pandas import read_csv

def console_in(prompt_message):
    '''
    Prompts the user to input data from the console. 
    The input is expected to be in string format.

    Args:
        prompt_message (string): message to prompt the user for input.

    Returns:
        string: data that was given from the console.
    '''
    input_data = input(prompt_message)
    return input_data


def read_file(file_path):
    '''
    Reads a data from a file and returns it in a string format.

    Args:
        file_path (string): path to a file to read.
    
    Raises:
        FileNotFoundError: if there is no file by given path.
        TypeError: one of the arguments has a wrong type. 
    
    Returns:
        list of str: data from a file located in `file_path`.
                     Each element in a list represents a separate line.
    '''
    if not isinstance(file_path, str):
        raise TypeError("type of a file_path is not string")

    if not path.exists(file_path):
        raise FileNotFoundError(f"there is no file by given path: {file_path}")
    
    file_to_read = open(file_path)
    list_of_lines = file_to_read.readlines()
    file_to_read.close()

    return list_of_lines


def pandas_read_file(file_path):
    '''
    Reads a data from a .csv file and returns it in a string format.

    This functions uses a 'pandas' package to read a file in `file_path`.

    Raises:
        FileNotFoundError: if there is no file by given path.
        TypeError: if one of the arguments has a wrong type.
        ValueError: if the file_path does not have a .csv extension.

    Args:
        file_path (string): path to a file to read.
    
    Returns:
        list of str: data from a file located in `file_path`.
                     Each element in a list represents a separate line.
    '''
    if not isinstance(file_path, str):
        raise TypeError("type of a file_path is not string")
    
    if not path.exists(file_path):
        raise FileNotFoundError(f"there is no file by given path: {file_path}")
    
    if not file_path[-4:]=='.csv':
        raise ValueError("the file must have a .csv extension.")
    
    pd_file = read_csv(file_path)
    return pd_file.to_string
