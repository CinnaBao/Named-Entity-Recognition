
# coding: utf-8
# Author: Bao Wan-Yun

import json
import re
span_tokens = re.compile(r'\s')

class Data_preprocessing():
    def __init__(self):
        self.author = 'WY Bao'
        self.data_path = "C:\\Users\\baowanyun\\NamedEntityRecognition\\"
    
    ## A token can only be part of one entity, so make sure the entities you're setting don't overlap. ##
    def RemoveErrordatase(self, candidateID, data):
        NEs = []
        for i in range(1,len(data)+1): 
            ind = i ; status = 0
            while ind < len(data) :
                B = data[i-1] 
                T = data[ind] 
                B_ = range(B[0], B[1])
                T_ = range(T[0], T[1])
                B_ = set(B_)
                if len(B_.intersection(T_)) > 0 :
                    status = 1
                    break           
                ind += 1 
            if status == 0:     
                NEs.append(data[i-1])
        return candidateID, NEs

    ## the model can't be updated in a way that's valid ##
    ## make sure that none of your annotated entity spans have leading or trailing whitespace. ##
    def valid_entities(self, Resume, entity):
        valid_entities = []
        for start, end, label in entity:
            valid_start = start
            valid_end = end
            while valid_start < len(Resume) and span_tokens.match(Resume[valid_start]):
                valid_start += 1
            while valid_end > 1 and span_tokens.match(Resume[valid_end - 1]):
                valid_end -= 1
            valid_entities.append((valid_start, valid_end, label))
        return valid_entities
            
    def Preprocessing(self, Data):    
        data_path = self.data_path + Data
        with open(data_path, 'r',encoding='utf-8') as f:
            lines = f.readlines()  
            candidateID = 1 ; Resumes_entities = []
            for line in lines:
                data = json.loads(line)
                Resumes = data['content'] ; Labels = data['annotation'] ; entities = []
                for NE in Labels:
                    NamedEntity = NE['points'][0] 
                    Label = NE['label']
                    candidate = '' 
                    try:  ## remove empty label ##
                        if Label[0] == 'Name' :  
                            candidate = NamedEntity['text'].replace('\n','') 
                        entities.append((NamedEntity['start'], NamedEntity['end']  + 1 ,Label[0]))  
                    except:
                        pass
                ##print(candidateID) ; print(candidate) ; print(entities)
                entities_afterRemove = self.RemoveErrordatase(candidateID,entities)
                Valid_entities = self.valid_entities(Resumes,entities_afterRemove[1])
                Resumes_entities.append((candidateID, candidate, Resumes, {"entities" : list(set(Valid_entities))})) 
                candidateID += 1
        return Resumes_entities

