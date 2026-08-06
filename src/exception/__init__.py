"""in this module we will estb how the errors and exceptions can be catched and 
    tracked in a readable and trackable manner. 
    Whenever thee xception occurs then this module will log what kind of exception has occured,
    in which module it has occured, in which line it has occured and at what time it has 
    occured.
"""

import sys
import logging

def error_message_detail(error:Exception, error_detail:sys)->str:
    """Extracts detailed error information including file name, line number, and the 
    error message. 

    Args:
        error (Exception): the exception that occured
        error_details (sys): the sys moduule to access traceback details

    Returns:
        str: A formatted error message string
    """

    #extract the traceback details (exception information
    #here we are unfoding a tuple
    #first val is exception type 
    #second val is the error message
    #third val is the traceback obj
    _,_,exc_tb = error_detail.exc_info()

    #get the file name where the exception occured 
    file_name = exc_tb.tb_frame.f_code.co_filename

    #create a formatted error message string with file_name, line_number, and the actual error
    line_number = exc_tb.tb_lineno
    error_message = f"Error occured in python script: [{file_name}] at line number [{line_number}]: {str(error)}"

    #log the error for better tracking 
    logging.error(error_message)


class MyException(Exception):
    """it is a custom exception class for handling errors"""
    def __init__(self, error_message:str, error_detail: sys):
        """Initializes the exception with a detailed error message

        Args:
            error_message (str): A string describing the error
            error_details (sys): The sys module to access the tarceback details
        """
        #call the base class constructor with the error message
        super().__init__(error_message)
        #format the detailed error message using the error_message_detail function
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self)->str:
        """returns the string representation of the error message
        """
        return self.error_message
