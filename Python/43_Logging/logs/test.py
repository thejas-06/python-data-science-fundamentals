from logger import logging

def div(a,b):

    logging.debug("The division is taking place")
    return a/b

logging.debug("the function is called")
div(4,2)