
import matplotlib.pyplot as plt
import subprocess
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler,normalize
from mpl_toolkits.mplot3d import Axes3D 
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier,BaggingClassifier
from sklearn.metrics import hamming_loss,make_scorer,f1_score
from sklearn import tree
from sklearn.decomposition import PCA
from scipy import stats
from sklearn.feature_selection import f_classif, SelectPercentile,SelectKBest,GenericUnivariateSelect,chi2
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_classification
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
import random

scaler = MinMaxScaler()
def get_data(file_name):
    df=pd.read_csv(file_name)
    # df.drop(["State","City"],axis=1,inplace=True)
    df=df.sample(frac=1,random_state=22)
    
    df = df[df.iloc[:, -1] != -1]
    print(df.shape) 
    df.drop(["State","Name"],axis=1,inplace=True)
     #for some reason you must put a random state for it to not be awfull nut any num works
    features = df.iloc[:, :7] 
    print(df.head())
    #change based on what file, wind=6 solar=7
    labels = df.iloc[:, -1]

    labeled_indices = labels != -1
    X = features[labeled_indices]
    y= labels[labeled_indices]

    return X,y



# maybe use unsupervised to filter for both and then use supervised to filter individually solar and wind (different criteria)
#could aslo just go strait into supervised filtering of solar and wind
#they both have same number of suitable and not suitable now

def filter(file_name):
    

    X_labeled = get_data(file_name)[0]
    y_labeled = get_data(file_name)[1]

    print(X_labeled.shape,y_labeled.shape)
    # print(X_labeled.head,y_labeled.head)
    
    fs = SelectKBest(score_func=chi2 ,k='all')
    fit = fs.fit(X=X_labeled,y=y_labeled)

    features_score = pd.DataFrame(fit.scores_)
    features = pd.DataFrame(X_labeled.columns)
    feature_score = pd.concat([features,features_score],axis=1)
    # Assigning column names
    feature_score.columns = ["Input_Features","Chi2_score"]
    print(feature_score.nlargest(10,columns="Chi2_score"))

def eh():
    pass
    # variables = ["Temperature", "Dew_Point", "GHI", "Relative_Humidity", "Surface_Albedo", "Pressure", "Precipitable_Water", "Wind_Speed"]
    # df=pd.read_csv("AVG_Data copy.csv")
    # b=0
    # for i in range(0,len(variables)):
    #     for j in range(i+1,len(variables)):
    #         correlation = df[variables[i]].corr(df[variables[j]],"spearman")
    #         print(f"correlation between {variables[i]}  and {variables[j]}: {correlation}")
    #         b+=1
    #         if(correlation>0.7):
    #             print(f"HIGH CORRELATION AT {variables[i]} and {variables[j]}")
    # print(b)

    # correlation = df["Relative_Humidity"].corr(df["Dew_Point"],"spearman")
    # print(f"correlation between Precipitable water and Dew Point: {correlation}")

        


    # filter("solar+all_label copy.csv")
    # filter("wind+all_label copy.csv")


def pipeline(file_name):

   
    X = get_data(file_name)[0]
    y = get_data(file_name)[1]

    clf = Pipeline(
    [   
        
        ("anova", SelectPercentile(chi2,percentile=100)),
        ("Bagging", RandomForestClassifier()),
    ]
        )   


    score_means = list()
    score_stds = list()
    # percentiles = (1, 3, 6, 10, 15, 20, 30, 40, 60, 80,90, 100)
    # percentiles = tuple(range(10, 101, 10))
    percentiles = np.arange(14.2857142857, 101, 14.2857142857)

    for percentile in percentiles:
        clf.set_params(anova__percentile=percentile)
        this_scores = cross_val_score(clf, X, y,cv=10) # k fold cross validation to bypass overfitting 
        print(this_scores)
        score_means.append(this_scores.mean())
        score_stds.append(this_scores.std())

    plt.errorbar(percentiles, score_means, np.array(score_stds),barsabove=True)  #bars = Standard deviation
    plt.title("Performance of the RFC varying the percentile of features selected")
    plt.xticks(np.arange(14.2857142857, 101, 14.2857142857))
    plt.xlabel("Percentile")
    plt.ylabel("Accuracy Score")
    plt.axis("tight")
    plt.show()
pipeline('solar+all_label copy.csv')
filter('solar+all_label copy.csv')



#Dew point removed from both

#Solar remove SA, precipitable water, wind speed
#Wind remove GHI, SA, Precipitable water
