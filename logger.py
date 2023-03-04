import logging

# Function for append logs throughout the code``
def log(filename:str,msg:str):
    """
    This Function appends all logs in provided log file
    filename  : log file name
    msg : log message that want to append 
    =====================================
    Logging Purpose Only....
    """
    logging.basicConfig(filename=filename + ".log", filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S',level=logging.INFO)
    logging.info(msg)
