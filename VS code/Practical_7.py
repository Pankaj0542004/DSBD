#Perform the following operations using Python on any open source
#dataset


#1. Import all the required Python Libraries.
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

#2. Load the Dataset into the pandas data frame.
df = pd.read_csv('train1.csv')
df.head()

#3. Display the initial statistics.
df.info()
df.describe()

#4. Scan all variables for missing values and inconsistencies. If there are
#missing values and/or inconsistencies, use any of the suitable techniques to deal with them.
df.isnull().sum()
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])


#5. Scan all numeric variables for outliers. If there are outliers, use any of
#the suitable techniques to deal with them.
numerical_cols = df.select_dtypes(include=np.number).columns

for col in numerical_cols:
	Q1 = df[col].quantile(0.25)
	Q3 = df[col].quantile(0.75)
    
# Calculate IQR and identify outliers for a given column
IQR = Q3 - Q1
lowerBound = Q1 - 1.5 * IQR
upperBound = Q3 + 1.5 * IQR  # Note: The upper bound should be based on Q3, not Q1

outliers = df[(df[col] < lowerBound) | (df[col] > upperBound)]

if not outliers.empty:
    print(f"Outliers in '{col}': ")
    print(outliers[[col]])
    print("\n")

# Apply data transformations on at least one of the variables
scaler = MinMaxScaler()
df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])
df.head()

# Turn categorical variables into quantitative variables in Python
df = pd.get_dummies(df, columns=['Sex', 'Embarked'], dtype=int)
df.head()

# Save the modified DataFrame
df.to_csv('modified_titanic_dataset.csv', index=False)
