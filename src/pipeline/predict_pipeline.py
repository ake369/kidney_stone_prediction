import os
import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)

class CustomData:
    def __init__(self,
        specific_gravity: float,
        ph_level:float,
        osmolality: float,
        conductivity: float,
        urea_concentration: float,
        calcium_concentration: float,
        ):

        self.specific_gravity=specific_gravity        
        self.ph_level=ph_level
        self.osmolality=osmolality
        self.conductivity=conductivity
        self.urea_concentration=urea_concentration
        self.calcium_concentration=calcium_concentration

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "specific_gravity": [self.specific_gravity],
                "ph_level": [self.ph_level],
                "osmolality": [self.osmolality],
                "conductivity": [self.conductivity],
                "urea_concentration": [self.urea_concentration],
                "calcium_concentration":[self.calcium_concentration]
            }
            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)