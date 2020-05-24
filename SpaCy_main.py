
# coding: utf-8
# Author: Bao Wan-Yun

import Data_preprocessing as Factory
import TrainingSpaCy as Factory2

P = Factory.Data_preprocessing()
T = Factory2.TrainingSpaCy()
Training_data = P.Preprocessing('Resumes.json')  
Recognizer = T.Recognizer(Training_data)
Entities_list = Recognizer[1]
Recognizer = Recognizer[0]
