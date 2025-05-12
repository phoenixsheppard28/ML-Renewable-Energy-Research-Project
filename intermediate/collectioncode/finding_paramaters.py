# import semi_sup_solar as solar
# import semi_sup_wind as wind
# import matplotlib.pyplot as plt
# import subprocess
# from sklearn.semi_supervised import SelfTrainingClassifier
# import requests
# import json
# import numpy as np
# import io
# import time
# import os
# import matplotlib.pyplot as plt
# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.preprocessing import MinMaxScaler
# from sklearn.cluster import KMeans
# from sklearn.preprocessing import normalize
# import csv
# from sklearn.metrics import silhouette_samples, silhouette_score
# from sklearn.preprocessing import StandardScaler
# from sklearn.cluster import HDBSCAN 
# from mpl_toolkits.mplot3d import Axes3D 
# from scipy.spatial.distance import cdist
# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split
# from sklearn import datasets
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import hamming_loss
# import graphviz 
# from sklearn import tree
# def wind_param_finder(n_estimators,min_samples_split=2,):
    

#     def see_tree(model):
        
#         tree.plot_tree(model) #need to fix



#     df=pd.read_csv('wind+all_label copy.csv')
#     state=df["State"]
#     name=df["Name"]
#     df.drop(["State","Name"], axis=1, inplace=True)
#     save=df.iloc[:,:8]
#     # df.iloc[:,:8]=normalize(df.iloc[:,:8],axis=0)  #experiment between not normalizing and normalizing with axis 0 and 1

#     print(df.head())



#     def prepare_semi_supervised_data(data_frame,count):
#         # Assuming the first 8 columns are features and the last column is the label
#         features = data_frame.iloc[:, :8]
#         labels = data_frame.iloc[:, -1]
        
#         # Split data into labeled and unknown based on labels
#         labeled_indices = labels != -1
#         X_labeled = features[labeled_indices]
#         y_labeled = labels[labeled_indices]
#         X_unknown = features[~labeled_indices].iloc[:100,:]


#         print(f"length of {len(X_unknown)}") #df Iloc allows you to index by row and column in that order.

#         #because its getting smaller and your increacing the indeices each time you run the code

#         return X_labeled, y_labeled, X_unknown
        
#     def add_psudo_label(df, labels):
#         i=0
        
#         while(i<df.shape[0] and len(labels)!=0):
#             if(df.loc[i,"Suitability"]== -1):
#                 df.loc[i,"Suitability"]=labels[0]
#                 labels=labels[1:] 
#             i+=1


#     accuracy_list=[]
#     hamming_loss_list=[]
#     #maybe I will make my own semi supervised model by iterating over the model to predict the labels and train off of them
#     # IF this doesent work just do the first iteration using the given data and run w that
#     count=0
#     while(count<8):
#         model=RandomForestClassifier(min_samples_split=min_samples_split,n_estimators=n_estimators,n_jobs=-1)  #leave inside

#         X_labeled,y_labeled,X_unknown=prepare_semi_supervised_data(df,count)

#         X_train_labeled, X_test, y_train_labeled, y_test = train_test_split(X_labeled, y_labeled, test_size=0.2, random_state=42) #0.2 or

#         model.fit(X_train_labeled, y_train_labeled)
#         accuracy = model.score(X_test, y_test)
#         hamming_loss_list.append(hamming_loss(y_test, model.predict(X_test)))
#         print(accuracy)
#         accuracy_list.append(accuracy)
#         if(len(X_unknown)>0):
#             labels=model.predict(X_unknown)
#             add_psudo_label(df,labels)

#         print(len(labels))

#         print(count)

#         count+=1
        


#     print(f"accuracy list{accuracy_list}")
#     print(f"hamming_loss_list: {hamming_loss_list}")

#     # return sum(accuracy_list)/len(accuracy_list), sum(hamming_loss_list)/len(hamming_loss_list) #then to graph it and mind the best params
#     return accuracy_list[0],hamming_loss_list[0]

#     # df.insert(0,"Name",name)
#     # df.insert(0,"State",state)
#     # df.to_csv("All_labels_Wind.csv",index=False)
# def solar_param_finder(n_estimators,min_samples_split=2,):
#     def see_tree(model):
        
#         tree.plot_tree(model) #need to fix



#     df=pd.read_csv('All_labels_Wind.csv')
#     state=df["State"]
#     name=df["Name"]
#     df.drop(["State","Name"], axis=1, inplace=True)
#     save=df.iloc[:,:8]
#     # df.iloc[:,:8]=normalize(df.iloc[:,:8],axis=0)  #experiment between not normalizing and normalizing with axis 0 and 1

#     print(df.head())



#     def prepare_semi_supervised_data(data_frame,count):
#         # Assuming the first 8 columns are features and the last column is the label
#         features = data_frame.iloc[:, :8]
#         labels = data_frame.iloc[:, -1]
        
#         # Split data into labeled and unknown based on labels
#         labeled_indices = labels != -1
#         X_labeled = features[labeled_indices]
#         y_labeled = labels[labeled_indices]
#         X_unknown = features[~labeled_indices].iloc[:100,:]


#         print(f"length of {len(X_unknown)}") #df Iloc allows you to index by row and column in that order.

#         #because its getting smaller and your increacing the indeices each time you run the code

#         return X_labeled, y_labeled, X_unknown
        
#     def add_psudo_label(df, labels):
#         i=0
        
#         while(i<df.shape[0] and len(labels)!=0):
#             if(df.loc[i,"Suitability"]== -1):
#                 df.loc[i,"Suitability"]=labels[0]
#                 labels=labels[1:] 
#             i+=1


#     accuracy_list=[]
#     hamming_loss_list=[]
#     #maybe I will make my own semi supervised model by iterating over the model to predict the labels and train off of them
#     # IF this doesent work just do the first iteration using the given data and run w that
#     count=0
#     while(count<8):
#         model=RandomForestClassifier(min_samples_split=min_samples_split,n_estimators=n_estimators,n_jobs=-1)  #leave inside

#         X_labeled,y_labeled,X_unknown=prepare_semi_supervised_data(df,count)

#         X_train_labeled, X_test, y_train_labeled, y_test = train_test_split(X_labeled, y_labeled, test_size=0.2, random_state=42) #0.2 or

#         model.fit(X_train_labeled, y_train_labeled)
#         accuracy = model.score(X_test, y_test)
#         hamming_loss_list.append(hamming_loss(y_test, model.predict(X_test)))
#         print(accuracy)
#         accuracy_list.append(accuracy)
#         if(len(X_unknown)>0):
#             labels=model.predict(X_unknown)
#             add_psudo_label(df,labels)


#         print(count)

#         count+=1
        


#     print(f"accuracy list{accuracy_list}")
#     print(f"hamming_loss_list: {hamming_loss_list}")

#     return sum(accuracy_list)/len(accuracy_list), sum(hamming_loss_list)/len(hamming_loss_list) #then to graph it and mind the best params


#     # df.insert(0,"Name",name)
#     # df.insert(0,"State",state)
#     # df.to_csv("All_labels_Wind.csv",index=False)


# acc_list=[]
# ham_list=[]
# var_split_values = list(range(100, 105))
# for i in range(100,105):
#     arr=wind_param_finder(n_estimators=i)
#     acc_list.append(arr[0])
#     ham_list.append(arr[1])
    
# def plot_acc_ham():
#     plt.figure(figsize=(10, 6))
    
#     plt.plot(var_split_values, acc_list, label='Accuracy', marker='o')
#     plt.plot(var_split_values, ham_list, label='Hamming Loss', marker='x')

#     plt.xlabel('n_estimators')
#     plt.ylabel('Value')
#     plt.title('Accuracy and Hamming Loss vs. min_samples_split')
#     plt.legend()
#     plt.grid(True)
#     plt.show()

# optimal_min_samples_split = np.argmax(acc_list)
# optimal_min_samples_split_vales = acc_list[optimal_min_samples_split]
# print(f"{optimal_min_samples_split}\n{+optimal_min_samples_split_vales}")
# plot_acc_ham()

# 2= best min_samples_split for both
# n_estimators best for both = probably just default (100) for both 
#f1 score 
#recall
#look into length
#self enforcing

#1
#feature selection/ engineering correlation score plot 
#D0NE

#2
# model selection : Bagging, DT,RandomForest, GradientBoost
# : 
#paralell-homogenous ensemble method 
#sequential 
#D0NE 

#3
#hyperparameter tuning: grid search , bayesian search for hyperparamater tuning
#D0NE

# 4
# metric: f1 score for hyperparamater tuning
#D0NE

