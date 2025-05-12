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



AVG_dic = {
        "Temperature": None,
        "Dew_Point": None,
        "GHI": None,
        "Relative_Humidity": None,
        "Solar_Zenith": None,
        "Surface_Albedo": None,
        "Pressure":None,
        "Precipitable_Water": None,
        "Wind_Speed": None
    }
key_list=list(AVG_dic.keys())
file_path = "Clean_wind+all.csv"  # Replace with the actual file path
df = pd.read_csv(file_path)
def elbow():
    

    # Preprocess the dataset
    df.drop(["State","City"], axis=1, inplace=True)
    numerical_features = ['GHI', 'Wind_Speed', 'Temperature']
    scaler = MinMaxScaler()
    df[numerical_features] = scaler.fit_transform(df[numerical_features])

    distortions = []
    inertias = []
    mapping1 = {}
    mapping2 = {}
    K = range(1, 10)

    for k in K:
        # Building and fitting the model
        kmeanModel = KMeans(n_clusters=k).fit(df)
        kmeanModel.fit(df)

        distortions.append(sum(np.min(cdist(df, kmeanModel.cluster_centers_,
                                            'euclidean'), axis=1)) / df.shape[0])
        inertias.append(kmeanModel.inertia_)

        mapping1[k] = sum(np.min(cdist(df, kmeanModel.cluster_centers_,
                                    'euclidean'), axis=1)) / df.shape[0]
        mapping2[k] = kmeanModel.inertia_
    plt.plot(K, distortions, 'bx-')
    plt.xlabel('Values of K')
    plt.ylabel('Distortion')
    plt.title('The Elbow Method using Distortion')
    plt.show()


    # Elbow method for finding optimal k
    inertia = []
    for k in range(1, 11):
        kmeans = KMeans(n_clusters=k, random_state=0)
        kmeans.fit(df)
        inertia.append(kmeans.inertia_)

    # Plot the Elbow Method
    plt.figure(figsize=(10, 5))
    plt.plot(range(1, 11), inertia, marker='o')
    plt.title('Elbow Method for Optimal k')
    plt.xlabel('Number of Clusters (k)')
    plt.ylabel('Inertia')
    plt.show()

def plot_silhouette(frame, num_clusters_range):
    # Read the CSV file into a DataFrame
    df = frame.iloc[:,2:]
    print(df)
    # Select the features you want to use for clustering
    X = df.values
    
    silhouette_scores = []
    
    for num_clusters in num_clusters_range:
        # Create a KMeans clustering model
        kmeans = KMeans(n_clusters=num_clusters, random_state=42)
        
        # Fit the model to the data
        kmeans.fit(X)
        
        # Calculate silhouette scores for each sample
        silhouette_avg = silhouette_score(X, kmeans.labels_)
        silhouette_scores.append(silhouette_avg)
        
        # Compute the silhouette scores for each sample
        sample_silhouette_values = silhouette_samples(X, kmeans.labels_)
        
        # Create a subplot with 1 row and 1 column
        plt.figure()
        ax = plt.gca()
        
        y_lower = 10
        for i in range(num_clusters):
            ith_cluster_silhouette_values = sample_silhouette_values[kmeans.labels_ == i]
            ith_cluster_silhouette_values.sort()
            
            size_cluster_i = ith_cluster_silhouette_values.shape[0]
            y_upper = y_lower + size_cluster_i
            
            color = plt.cm.get_cmap("Spectral")(float(i) / num_clusters)
            ax.fill_betweenx(np.arange(y_lower, y_upper), 0, ith_cluster_silhouette_values, facecolor=color, alpha=0.7)
            
            ax.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))
            
            y_lower = y_upper + 10
        
        ax.set_title("Silhouette plot")
        ax.set_xlabel("Silhouette coefficient values")
        ax.set_ylabel("Cluster label")
        
        ax.axvline(x=silhouette_avg, color="red", linestyle="--")
        
        plt.show()
    
#     return silhouette_scores
# num_clusters_range = [2, 3, 4, 5,6]  # You can adjust the range of cluster numbers
# silhouette_scores = plot_silhouette(df, num_clusters_range)
# print("Silhouette Scores:", silhouette_scores)



def cluster(data, num_clusters=3):
    key_list = data.columns[2:]  # Extract column names excluding the first two columns
    df_norm = normalize(data[key_list],axis=0) # Normalize the selected columns
    print(df_norm)
    #with this method of normalizing and plotting, we have the centroids that correspond to suitable for only wind, Both, Neither
    model = KMeans(n_clusters=num_clusters)
    model.fit(df_norm)

    color_theme = np.array(['darkgrey', 'lightsalmon', 'lightblue', 'red', 'black', 'purple'])

    # for i in range(len(key_list)):
    #     for j in range(i + 1, len(key_list)):  # Loop through pairs of columns without repetition
    #         plt.xlabel(key_list[i])
    #         plt.ylabel(key_list[j])
    #         plt.scatter(x=data[key_list[i]], y=data[key_list[j]], c=color_theme[model.labels_])
    #         plt.title(f'Scatter Plot: {key_list[i]} vs {key_list[j]}')
    #         plt.show()
    # centroids=model.cluster_centers_
    # print(centroids)
        # Create a 3D scatter plot

    def plot_3d():
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        cluster_centers = model.cluster_centers_
        # Extract X, Y, and Z coordinates for each cluster center
        x = [center[0] for center in cluster_centers]
        y = [center[1] for center in cluster_centers]
        z = [center[2] for center in cluster_centers]
        # Create the scatter plot
        ax.scatter(x, y, z, c='r', marker='o')
        # Set labels for the axes
        ax.set_xlabel('GHI')
        ax.set_ylabel('WIND')
        ax.set_zlabel('TEMPERATURE')
        # Set plot title
        ax.set_title('Cluster Centers in 3D Space')
        # Show the plot
        plt.show()
    def plot_kmeans_clusters_3d(kmeans_model, data):
   
        labels = kmeans_model.labels_
        cluster_centers = kmeans_model.cluster_centers_

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        for i in range(len(cluster_centers)):
            ax.scatter(data[labels == i, 0], data[labels == i, 1], data[labels == i, 2], label=f'Cluster {i+1}')

        ax.scatter(cluster_centers[:, 0], cluster_centers[:, 1], cluster_centers[:, 2], c='black', marker='X', s=200, label='Cluster Centers')

        ax.set_xlabel('GHI')
        ax.set_ylabel('WIND')
        ax.set_zlabel('TEMPERATURE')
        ax.set_title('KMeans Clustering in 3D Space')
        ax.legend()
        

        plt.show()

# Assuming you have a trained KMeans model 'kmeans' and data 'data'

    plot_kmeans_clusters_3d(model, df_norm)



cluster(df,num_clusters=3)

