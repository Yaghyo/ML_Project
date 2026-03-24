# have the common thing that we are going to or try to import 
## common functionality which the entire project csn use
import os
import sys
import pandas as pd 
import dill
# we can do train test split here to make the code cleaner
import numpy as np
from src.exception import CustomException

def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,"wb") as file_obj:
            dill.dump(obj, file_obj) # dill have to create pickle file

    except Exception as e:
        raise CustomException(e, sys)
