from sklearn.semi_supervised import SelfTrainingClassifier
import requests
import json
import numpy as np
import io
import time
import os
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from sklearn.preprocessing import normalize
import csv
from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import HDBSCAN 
from mpl_toolkits.mplot3d import Axes3D 
from scipy.spatial.distance import cdist
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import hamming_loss,f1_score
import graphviz 
from sklearn.tree import plot_tree
from sklearn.naive_bayes import GaussianNB




df=pd.read_csv('wind+all_label copy.csv')
state=df["State"]
name=df["Name"]
df.drop(["State","Name","Surface_Albedo","Precipitable_Water","GHI"], axis=1, inplace=True) #could also leave in other variables
# save=df.iloc[:,:4]
# df.iloc[:,:4]=normalize(df.iloc[:,:8],axis=0)  #experiment between not normalizing and normalizing with axis 0 and 1

# print(df.head())



def prepare_semi_supervised_data(data_frame,count):
    
    final_features=["Temperature",	"Wind_Speed",	"Relative_Humidity",	"Pressure"]
    features = data_frame[final_features]
  #NEED TO ACCOIUNT FOR FEATURE SELECTION
    print(features.head())    
    labels = data_frame.iloc[:, -1]
    
    labeled_indices = labels != -1
    X_labeled = (features[labeled_indices])
    y_labeled = labels[labeled_indices]
    X_unknown = features[~labeled_indices].iloc[:100,:]
    if(len(X_unknown)>0):
        X_unknown=(X_unknown)
    print(f"len X_lableed {len(X_labeled)}")


    print(f"length of unknown {len(X_unknown)}") #df Iloc allows you to index by row and column in that order.

    #because its getting smaller and your increacing the indeices each time you run the code

    return X_labeled, y_labeled, X_unknown
    
def add_psudo_label(df, labels):
    i=0
    
    while(i<df.shape[0] and len(labels)!=0):
        if(df.loc[i,"Suitability"]== -1):
            df.loc[i,"Suitability"]=labels[0]
            labels=labels[1:] 
        i+=1


########################### variables #########################


results_dic = {
    'Accuracy': [],
    'F1-Score': [],
    'Hamming Loss': []
}
#maybe I will make my own semi supervised model by iterating over the model to predict the labels and train off of them
# IF this doesent work just do the first iteration using the given data and run w that
count=0

params={
   'n_estimators': 300, 'min_samples_split': 4, 'min_samples_leaf': 2, 'max_leaf_nodes': 27, 'criterion': 'gini','max_depth':5 #5 or 7 max depth
}
while(count<9):  
    model=RandomForestClassifier(**params)    #leave inside loop experiment wiht bootstrap=False
    X_labeled,y_labeled,X_unknown=prepare_semi_supervised_data(df,count)

    X_train_labeled, X_test, y_train_labeled, y_test = train_test_split(X_labeled, y_labeled, test_size=0.2,shuffle=True) #0.2 or

    model.fit(X_train_labeled, y_train_labeled)
    y_pred= model.predict(X_test)  #predicted
     

    accuracy = model.score(X_test, y_test)
    f1 = f1_score(y_test, y_pred)
    hamming_loss_value = hamming_loss(y_test, y_pred)
        
        # Collect results for this iteration
    result = {
        'Accuracy': accuracy,
        'F1-Score': f1,
        'Hamming Loss': hamming_loss_value
    }
    results_dic["Accuracy"].append(accuracy)
    results_dic["F1-Score"].append(f1)
    results_dic["Hamming Loss"].append(hamming_loss_value)
    print(accuracy)
    
    if(len(X_unknown)>0):
        labels=model.predict(X_unknown)
        add_psudo_label(df,labels)

    # print(len(labels))

    # print(count
    # )

    count+=1


print(f"accuracy list { results_dic['Accuracy'] }")
# print(f"hamming_loss_list: {hamming_loss_list}")

#least important feature

def plot_iterations_scores(f1_scores, accuracy_scores):
    iterations = range(1, len(f1_scores) + 1)

    plt.figure(figsize=(10, 6))  
    plt.plot(iterations, f1_scores, marker='o', linestyle='-', label='F1-Score')
    plt.plot(iterations, accuracy_scores, marker='s', linestyle='-', label='Accuracy')

    plt.xlabel("Iterations")
    plt.ylabel("Score")
    plt.title("F1-Score and Accuracy vs. Iterations for the Wind RFC Model")
    plt.ylim(0.9, 1)
    plt.grid(True)
    plt.legend()
    
    plt.show()

def show_tree(model,num_tree):
    plt.figure(figsize=(20, 8))
    plot_tree(model.estimators_[num_tree], feature_names=['Temperature', 'Wind_Speed', 'Relative_Humidity',  'Pressure'], class_names=['Not Suitable', 'Suitable'], filled=True)
    plt.show()

# for i in range (0,5):
#     show_tree(model,num_tree=i)
# f1_std=np.std(results_dic["F1-Score"])
# acc_std=np.std(results_dic["Accuracy"])
# f1_mean=np.mean(results_dic["F1-Score"])
# acc_mean=np.mean(results_dic["Accuracy"])
# print("F1 Score and acc std: ",f1_std,"   ",acc_std)
# print("F1 score and acc mean: ",f1_mean,"   ",acc_mean)

# plot_iterations_scores(results_dic["F1-Score"],results_dic["Accuracy"])

df.insert(0,"Name",name)
df.insert(0,"State",state)
df.to_csv("All_labels_Wind.csv",index=False)
