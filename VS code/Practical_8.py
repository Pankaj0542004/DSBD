import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import StratifiedKFold,cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

penguins_data = pd.read_csv('penguins.csv')
penguins_data.head()

penguins_data.info()

penguins_data.species.value_counts()

penguins_data.isnull().sum()


for column_name in penguins_data.select_dtypes(include='float', exclude='object'):
    penguins_data[column_name] = penguins_data[column_name].fillna(penguins_data[column_name].mean())

penguins_data['sex'] = penguins_data['sex'].ffill()

sns.scatterplot(x='bill_length_mm', y='bill_depth_mm', hue='species', data=penguins_data, style='species')
from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()
for col in ['sex', 'island']:
    penguins_data[col] = label_encoder.fit_transform(penguins_data[col])

# Standardize numerical columns
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
for col in ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']:
    penguins_data[col] = scaler.fit_transform(penguins_data[[col]])

from sklearn.decomposition import PCA

X = penguins_data.drop('species',axis=1)
Y = penguins_data['species']

PCA_TR = PCA(n_components=3)
X_train = PCA_TR.fit_transform(X)
PCA_TR.explained_variance_ratio_

PCA_TR.components_

pd.DataFrame(PCA_TR.components_,columns=X.columns,index = ['PC-1','PC-2','PC-3'])


LRM = LogisticRegression()
DTC = DecisionTreeClassifier()
RFC = RandomForestClassifier()
KNC = KNeighborsClassifier()
NBC = GaussianNB()

SKF = StratifiedKFold(n_splits = 10, shuffle =True, random_state=10)

print(f'LogisticRegression : {round(cross_val_score(LRM,X_train,Y,cv=SKF,scoring="accuracy").mean()*100,2)}%')
print(f'DecisionTreeClassifier : {round(cross_val_score(DTC,X_train,Y,cv=SKF,scoring="accuracy").mean()*100,2)}%')
print(f'RandomForestClassifier : {round(cross_val_score(RFC,X_train,Y,cv=SKF,scoring="accuracy").mean()*100,2)}%')
print(f'KNeighborsClassifier : {round(cross_val_score(KNC,X_train,Y,cv=SKF,scoring="accuracy").mean()*100,2)}%')
print(f'GaussianNB : {round(cross_val_score(NBC,X_train,Y,cv=SKF,scoring="accuracy").mean()*100,2)}%')