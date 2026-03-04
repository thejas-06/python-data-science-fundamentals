import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("main-app.log"),
        logging.StreamHandler()
    ]
    )

logger=logging.getLogger("ArithmeticApp")

def add(a,b):
    result=a+b
    logger.debug(f"Adding {a}+{b}={result}")
    return result

def sub(a,b):
    result=a-b
    logger.debug(f"Adding {a}-{b}={result}")
    return result

def mul(a,b):
    result=a*b
    logger.debug(f"Adding {a}*{b}={result}")
    return result

def div(a,b):
    try:
        result=a/b
        logger.debug(f"Adding {a}/{b}={result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None
    
add(10,15)
sub(15,10)
mul(4,2)
div(20,0)