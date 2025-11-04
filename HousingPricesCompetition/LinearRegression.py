import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


train_data = pd.read_csv('./data/train.csv')
test_data = pd.read_csv('./data/test.csv')

train_features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']

X = train_data[train_features]
y = train_data['SalePrice']

model = LinearRegression()
model.fit(X, y)

print(f"Model {model}")

test_X = test_data[train_features]
predictions = model.predict(test_X)

output = pd.DataFrame({'Id': test_data.Id, 'SalePrice': predictions})
output.to_csv('LinearRegressionSubmission.csv', index=False)
print("Submission file created: LinearRegressionSubmission.csv")