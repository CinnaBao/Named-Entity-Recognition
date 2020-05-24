
# coding: utf-8
# Author: Bao Wan-Yun

import numpy as np
import spacy
import random
import time
from spacy.gold import GoldParse
import Data_preprocessing as p

class TrainingSpaCy():
    def __init__(self):
        self.author = 'WY Bao'
    
    def Recognizer(self, data): 
        print('Training dataset : %s' %str(np.shape(data)))
        nlp = spacy.blank('en')  ## create blank Language class ##
        Ori_nlp_vocab = list(nlp.vocab.strings)
        num_Ori_nlp_vocab = len(Ori_nlp_vocab)

        ## create the built-in pipeline components and add them to the pipeline ##
        if 'ner' not in nlp.pipe_names:
            ner = nlp.create_pipe('ner')
            nlp.add_pipe(ner, last=True)  ## the last piece of the pipeline ##

        ## Add labels to 'spaCy's pipeline'
        for ID, candidate, Resume, entities in data:
            for entity in entities.get('entities'): 
                # Add named entities to text recognizer ( ex. ner.add_label("POSITIVE") ; ner..add_label("NEGATIVE") )
                ner.add_label(entity[2]) 
                '''
                'ROOT', 'Graduation Year', 'College Name', 'Degree', 'Location', 'Companies worked at', 
                'Designation', 'Years of Experience', 'Email Address', 'Name', 'Skills', 'UNKNOWN'
                '''
        New_nlp_vocab = list(nlp.vocab.strings)
        num_New_nlp_vocab = len(New_nlp_vocab)

        num_Entity = num_New_nlp_vocab - num_Ori_nlp_vocab
        Entities_list = New_nlp_vocab[::-1][:num_Entity][::-1] ; 
        print('Named entities : %s ' %Entities_list)

        # get names of other pipes to disable them during training
        other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
        with nlp.disable_pipes(*other_pipes):  # only train NER
            optimizer = nlp.begin_training()
            for iteration in range(10):
                print("\n Start iteration : %s"  %str(iteration))
                Start = time.time() 
                random.shuffle(data)  ## <class 'list'>
                losses = {}
                for ID, candidate, Resume, entities in data:
                    nlp.update(
                        [Resume],  # batch of texts
                        [entities],  # batch of annotations
                        drop = 0.2,  # dropout (aviod model overfitting)
                        sgd = optimizer,  # callable to update weights
                        losses=losses)
                End = time.time() 
                print('     It take %s secs' %str(round(End - Start,2)))
                print(losses)
        return nlp
