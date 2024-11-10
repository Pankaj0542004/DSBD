import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load the dataset
df = pd.read_csv("sales_data_sample.csv", encoding='latin')
print(df.head())  # Display first few rows of the dataset

# Check the data types of columns
print(df.dtypes)

# Selecting columns for clustering
X = df.iloc[:, [3,4]].values  # Adjust columns to fit your data structure

# Initializing WCSS (within-cluster sum of squares)
wcss = []   

# Applying K-Means for different k values to use the elbow method
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init="k-means++", random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
    
# Plotting the Elbow Method graph
ks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
plt.plot(ks, wcss, 'bx-')
plt.title("Elbow Method")
plt.xlabel("K value")
plt.ylabel("WCSS")
plt.show()  # To display the plot

# Statistical summary of the dataset
print(df.describe())

# Feature scaling
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
scaled = ss.fit_transform(X)

# Recalculating WCSS for scaled data
wcss = []
for i in range(1, 11):
    clustering = KMeans(n_clusters=i, init="k-means++", random_state=42)
    clustering.fit(scaled)
    wcss.append(clustering.inertia_)
    
# Plotting the Elbow Method graph for scaled data
plt.plot(ks, wcss, 'bx-')
plt.title("Elbow Method (Scaled Data)")
plt.xlabel("K value")
plt.ylabel("WCSS")
plt.show()  # To display the plot
