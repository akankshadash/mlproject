import sys
import pandas as pd
import numpy as np
from dataclasses import dataclass
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

from source.exceptions import CustomException
from source.loggers import logging
import os

from source.utils import save_object
@dataclass
class DataTranformationconfig:
    '''
    this function is responsible for data transformation
    '''
    preprocess_obj_file_path = os.path.join('artifacts', 'preprocess.pkl')
    
class DataTransformation:
    def __init__(self):
        self.config = DataTranformationconfig()

    def get_data_transformer_object(self):
        try:
            numerical_features = ['reading_score', 'writing_score']
            categorical_features = [
                'gender',
                'race_ethnicity',
                'parental_level_of_education',
                'lunch',
                'test_preparation_course'
            ]
        
            num_pipeline = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='mean')),
                ('scaler', StandardScaler())
            ])
            
            cat_pipeline = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='most_frequent')),
                ('one_hot_encoder', OneHotEncoder(handle_unknown='ignore')),
                ('scaler', StandardScaler(with_mean=False))  # with_mean=False for sparse matrix
            ])
            
            logging.info("Numerical and categorical pipelines created successfully.")   
                
            preprocessor = ColumnTransformer(
                transformers=[
                    ('numerical_pipeline', num_pipeline, numerical_features),
                    ('categorical_pipeline', cat_pipeline, categorical_features)
                ]
            )
            
            return preprocessor
        except Exception as e:
            raise CustomException(e, sys) 
    
    def initiate_data_transformation(self, train_path, test_path):
        try:
            logging.info("Data Transformation initiated.")
            
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            
            logging.info("Train and test data loaded successfully.")
            
            preprocessor_obj = self.get_data_transformer_object()
            
            target_column_name = 'math_score'
            numerical_features = ['reading_score', 'writing_score']
            
            input_feature_train_df = train_df.drop(columns=[target_column_name], axis=1)
            target_feature_train_df = train_df[target_column_name]
            
            test_feature_test_df = test_df.drop(columns=[target_column_name], axis=1)
            target_feature_test_df = test_df[target_column_name]
            
            logging.info("applying preprocessing object on train and test dataframes.")
            
            train_input_features_arr = preprocessor_obj.fit_transform(input_feature_train_df)
            test_input_features_arr = preprocessor_obj.transform(test_feature_test_df)
            logging.info("Preprocessing completed successfully.")
            
            train_arr = np.c_[train_input_features_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[test_input_features_arr, np.array(target_feature_test_df)]
            logging.info("Saved Preprocessing successfully.")   
            
            save_object(
                file_path=self.config.preprocess_obj_file_path,
                obj=preprocessor_obj
            )
            return (
                train_arr,
                test_arr,
                self.config.preprocess_obj_file_path
            )
        except Exception as e:
            raise CustomException(e, sys)
        
if __name__ == "__main__":
    try:
        obj = DataTransformation()
        train_path = os.path.join('artifacts', 'train.csv')
        test_path = os.path.join('artifacts', 'test.csv')
        obj.initiate_data_transformation(train_path, test_path)
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        raise CustomException(e, sys)