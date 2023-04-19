# creating a prediction pipeline 
import sys
import os 
sys.path.append(os.path.abspath(os.curdir))
import pandas as pd 
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object

class PredictPipeline: 
    def __init__(self):
        pass 

    def predict(self,features ):
        try: 
            model_path = "artifacts\model.pkl"
            preprocessor_path = "artifacts\preprocessor.pkl"
            model = load_object(file_path = model_path)
            preprocessor = load_object(file_path = preprocessor_path)
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds
        except Exception as e: 
            raise CustomException(e,sys)

class CustomData: 
    # Responsible for mapping input values from html to backend 
    def __init__(self,
                 gender: str,
                 race_ethnicity: int,
                 parental_level_of_education: str,
                 lunch: str,
                 test_preparation_course: str,
                 reading_score: int,
                 writing_score:int): 
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    def get_data_as_data_frame(self): 
        try:
            # Function to return all the inputs from html in the form of a dataframe for model to ingest
            # This is because our model ingest the data in the form of a dataframe
            custom_data_input_dict = {
                "gender":[self.gender],
                "race_ethnicity":[self.race_ethnicity],
                "parental_level_of_education":[self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": self.reading_score,
                "writing_score":self.writing_score
            }

            return pd.DataFrame(custom_data_input_dict)
        except Exception as e: 
            raise CustomException(e,sys)
