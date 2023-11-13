import sys  #The sys module in Python provides various functions and variables that are used to manipulate different parts of the Python runtime environment.



def error_message_detail(error, error_detail:sys):
    #exc_tb  will stored all the information like which file, and line number and might be reason of excpetion is stored in this variable
    _,_,exc_tb = error_detail.exc_info() # here first two info of exception is not consider as you can see'_'


    file_name= exc_tb.tb_frame.f_code.co_filename # here file name is retrieved from error details
    error_message= "Error occured in python script name[{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)


       return error_message 
    ) 


class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super.__init__(error_message)