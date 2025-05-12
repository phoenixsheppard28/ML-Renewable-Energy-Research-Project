from sklearn.experimental import enable_halving_search_cv
import requests
import json
import numpy as np
import io
import time
import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler,normalize
from scipy.spatial.distance import cdist
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, KFold,cross_validate,cross_val_score,HalvingGridSearchCV,GridSearchCV,RandomizedSearchCV
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier,BaggingClassifier,GradientBoostingClassifier
#all the ones to test
from sklearn.metrics import hamming_loss,f1_score,make_scorer,roc_auc_score
from sklearn.tree import plot_tree,DecisionTreeClassifier
from scipy.stats import loguniform, randint,uniform

#and this one
def prep_data(file_name):
    df=pd.read_csv(file_name)
    # df.drop(["State","City"],axis=1,inplace=True)

    
    df = df[df.iloc[:, -1] != -1]
    print(df.shape) 
    df.drop(["State","Name"],axis=1,inplace=True)
    df=df.sample(frac=1) #shuffle it dont use random state 
    print(df.head())
    final_features = ["Temperature", "GHI", "Dew_Point", "Pressure"] #replace wind speed with GHI for solar


    features=df[final_features]
   
    labels = df.iloc[:, -1]

    labeled_indices = labels != -1
    X = features[labeled_indices]
    print(X.head())
    y= labels[labeled_indices]

    return X,y

model=RandomForestClassifier(n_jobs=-1)
def grid_search(file_name):
    X,y=prep_data(file_name)
    
   
    param_grid = {
    'n_estimators': np.arange(50, 1001, 50),          # Number of trees in the forest
    'min_samples_split': np.arange(2, 21),          # Minimum number of samples required to split an internal node
    'min_samples_leaf': np.arange(1, 21),           # Minimum number of samples required at each leaf node
    'criterion': ['gini'],              # Function to measure the quality of a split
    'max_leaf_nodes':np.arange(10,51),
    'max_depth':np.arange(3,10)


    }


    search = RandomizedSearchCV(model, param_grid,n_iter=500,n_jobs=-1, cv=10, scoring=make_scorer(f1_score),verbose=2)

    search.fit(X,y)
    print(search.best_estimator_)
    print(search.best_score_)
    print(search.best_params_)
    frame=pd.DataFrame(search.cv_results_)
    print(f'best_index in csv: {search.best_index_}')
    frame.to_csv("hyperparameter_solar.csv")

grid_search('All_labels_Solar.csv')   

