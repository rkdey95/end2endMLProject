import sys
import os
sys.path.append(os.path.abspath(os.curdir))
from src.logger import logging

def error_message_detail(error,error_detail:sys):
    """
    Returns error message of any file execution
    takes in the error and error_detail:sys - from system environment error. Data error of type sys
    """
    # Gives you the execution error
    # Which file and line error / exception occured. 
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename      # Read from custom exception handling in python documentation
    error_message = "Error occured in Python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

# Custom exception class. "Exception" with capital E is inherited from the Global Exception
class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys): 
        super().__init__(error_message)     # Class to inherit the attributes of the global Exception error message? 
        self.error_message = error_message_detail(error_message,error_detail = error_detail)

    def __str__(self):
        return self.error_message
    

    

    

    

    
