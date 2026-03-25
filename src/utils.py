# have the common thing that we are going to or try to import 
## common functionality which the entire project csn use
import os
import sys
import pandas as pd 
import dill
# we can do train test split here to make the code cleaner
import numpy as np
from src.exception import CustomException
from sklearn.metrics import r2_score

def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,"wb") as file_obj:
            dill.dump(obj, file_obj) # dill have to create pickle file

    except Exception as e:
        raise CustomException(e, sys)

def evaluate_models(X_train,y_train,X_test,y_test,models):
    try:
        report ={}

        for i in range(len(list(models))):
            model = list(models.values())[i]

            model.fit(X_train, y_train) # train model

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train,y_train_pred)

            test_model_score = r2_score(y_test,y_test_pred)

            report[list(models.keys())[i]] = test_model_score
        return report

    except Exception as e:
        raise CustomException(e,sys)