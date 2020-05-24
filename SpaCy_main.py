
# coding: utf-8

# In[ ]:


import Data_preprocessing as Factory
import TrainingSpaCy as Factory2

P = Factory.Data_preprocessing()
T = Factory2.TrainingSpaCy()
Training_data = P.Preprocessing('Resumes.json')  
Recognizer = T.Recognizer(Training_data)

