import pandas as pd
import os

# Read the data from the file
current_dir = os.path.dirname(__file__)
data = pd.read_csv(current_dir + "/dataset/online-retail.csv")

for column in data.select_dtypes(include=['object']).columns:
    data[column] = data[column].astype('string')

# Print Number of missing values in each column
missing_val = data.isnull().sum()
print("\nMissing values in the dataframe:")
print(missing_val)

# Drop Description column
data_drop = data.drop(columns=['Description'])

# remove rows with missing values in any column
data_drop = data_drop.dropna()

# Print Number of missing values in each column after imputing CustomerID column
print("\nMissing values in the dataframe after removal: ")
missing_val = data_drop.isnull().sum()
print(missing_val)

# Print the number of duplicate rows in the dataframe
dup_rows = data_drop.duplicated().sum()
print("\nNumber of duplicate rows in the dataframe:", dup_rows)

# Remove duplicate rows from the dataframe
data_drop_dup = data_drop.drop_duplicates()

# Print the number of duplicate rows in the dataframe after removing duplicates
dup_rows = data_drop_dup.duplicated().sum()
print("\nNumber of duplicate rows in the dataframe after removing duplicates: ", dup_rows)

# Remove non-numeric columns
data_drop_dup_num_only = data_drop.select_dtypes(include=['number'])

# Detect and print the outliers in the dataframe
Q1 = data_drop_dup_num_only.quantile(0.25)
Q3 = data_drop_dup_num_only.quantile(0.75)
IQR = Q3 - Q1
outliersNum = ((data_drop_dup_num_only < (Q1 - 1.5 * IQR)) | (data_drop_dup_num_only > (Q3 + 1.5 * IQR))).sum()
print("\nOutliers in the dataframe:")
print(outliersNum)

# Remove the outliers from the dataframe
data_no_outliers = data_drop_dup_num_only[~((data_drop_dup_num_only < (Q1 - 1.5 * IQR)) | (data_drop_dup_num_only > (Q3 + 1.5 * IQR))).any(axis=1)]

# Generate summary statistics of the dataframe
summary_statistics = data_no_outliers.describe()
print("\nSummary statistics of the dataframe:")
print(summary_statistics)

# export data_no_outliers to a new csv file
data_no_outliers.to_csv("cleaned_dataset", index=False)

# Plot histogram for numerical features and bar plot for categorical features
import matplotlib.pyplot as plt

# Plot histogram for numerical features
data_no_outliers.hist()
plt.show()

# Plot bar plot for categorical features
cat_cols = data_drop_dup.select_dtypes(include=['string']).columns
for column in cat_cols:
    plt.figure(figsize=(15, 10))
    data_drop_dup[column].value_counts().plot(kind='bar')
    plt.title(column)
    plt.show()
