#test_gender.py
import os
import pickle
import numpy as np
from scipy.io.wavfile import read
from speakerfeatures import extract_features
import warnings
warnings.filterwarnings("ignore")
import time
cwd = os.getcwd()


#path to training data
source   = cwd+"/development_set/"  

modelpath = cwd+"/speaker_models/"

test_file = "2.txt"        

file_paths = open(test_file,'r')


gmm_files = [os.path.join(modelpath,fname) for fname in 
              os.listdir(modelpath) if fname.endswith('.gmm')]

#Load the Gaussian gender Models
models    = [pickle.load(open(fname,'rb')) for fname in gmm_files]
speakers   = [fname.split("\\")[-1].split(".gmm")[0] for fname 
              in gmm_files]

# Read the test directory and get the list of test audio files 
for path in file_paths:   
    
    path = path.strip()   
    print (path)
    sr,audio = read(source + path)
    vector   = extract_features(audio,sr)
    
    log_likelihood = np.zeros(len(models)) 
    #l_score=[]
    for i in range(len(models)):
        gmm    = models[i]         #checking with each model one by one
        scores = np.array(gmm.score(vector))
        max_score = np.amax(scores)
        log_likelihood[i] = scores.sum()
        #l_score[i].append(scores)

    #candidate_probability = (np.exp(candidate_score)/np.exp(max_score)) * 100
    
    winner = np.argmax(log_likelihood)
    print ("\tdetected as - ", speakers[winner])
    #print("Score of ->> ",candidate_probability)
    time.sleep(1.0)


