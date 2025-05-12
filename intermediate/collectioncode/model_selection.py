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
from sklearn.model_selection import train_test_split, KFold,cross_validate,cross_val_score
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier,BaggingClassifier,GradientBoostingClassifier
#all the ones to test
from sklearn.metrics import hamming_loss,f1_score,make_scorer,roc_auc_score
from sklearn.tree import plot_tree,DecisionTreeClassifier
#and this one
import seaborn as sns
from sklearn.naive_bayes import GaussianNB
def prep_data(file_name):
    df=pd.read_csv(file_name)
    # df.drop(["State","City"],axis=1,inplace=True)

    
    df = df[df.iloc[:, -1] != -1]
    print(df.shape) 
    df.drop(["State","Name"],axis=1,inplace=True)
    df=df.sample(frac=1)  #shuffle it dont use random state 
    print(df.head())

    features=df.iloc[:, :4]  
    #change based on what file, wind=6 solar=7
    labels = df.iloc[:, -1]

    labeled_indices = labels != -1
    X = normalize(features[labeled_indices],axis=0)
    y= labels[labeled_indices]

    return X,y

# X,y = datasets.load_iris(return_X_y=True,as_frame=True)
# print(X,y)

def find_avgs(file_name):
    X,y=prep_data(file_name)
    # print(X,y)

    model_list=[RandomForestClassifier(),BaggingClassifier(random_state=None),GradientBoostingClassifier(random_state=None),DecisionTreeClassifier(random_state=None)]
    name_list=["RandomForestClassifier","BaggingClassifier","GradientBoostingClassifier","DecisionTreeClassifier"]
    # print(model_list)

    score_means = list()
    score_stds = list()

    for model in model_list:
        
        this_scores = cross_val_score(model, X, y,scoring=make_scorer(f1_score),cv=10) #cv = k fold cross val look chatgpt
        score_means.append(this_scores.mean())
        score_stds.append(this_scores.std())
        print(f"{model}\n{this_scores}")
        print(f"\n{this_scores.mean()}")


    data = pd.DataFrame({"Model": name_list, "F1 Score": score_means})
    sns.set(style="whitegrid")
    g= sns.catplot(x="Model", y="F1 Score", data=data, kind="bar", height=6, aspect=2)
    plt.title("F1 Scores for Different Models Applied to the Wind Dataset")
    plt.xlabel("Model")
    plt.ylabel("F1 Score")
    
    for i, ax in enumerate(g.axes.flat):
        for p, std in zip(ax.patches, score_stds):
            ax.text(p.get_x() + p.get_width() / 2., p.get_height(), f"{std:.2f}", ha="center", va="bottom")
   
    plt.ylim(0.9,1) #changes shown range
    plt.show()

    

    
   
    
    



    #changing cv makes it more or less averages I think

    


#clearly, the random forest classifier has the highest f1 score and lowest standard deviation

find_avgs("wind+label_features.csv")

#solar =200  use 10
#wind = 239  use 10
