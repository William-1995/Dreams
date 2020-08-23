import numpy as np
import pandas as pd
data = pd.read_csv('C:/Users/willl/Downloads/t2.csv')
data.head()
y = data.loc[:,'SalePrice']
X_multi = data.drop(['SalePrice'],axis=1)
from sklearn.linear_model import LinearRegression
# set up 2nd linear model
LR_multi = LinearRegression()
# tran the model
LR_multi.fit(X_multi, y)
# make pre
y_predict_multi = LR_multi.predict(X_multi)
print(y_predict_multi)

# make pre

#evalute the model
from sklearn.metrics import mean_squared_error,r2_score
mean_squared_error_multi = mean_squared_error(y,y_predict_multi)
r2_score_multi= r2_score(y, y_predict_multi)
print (mean_squared_error_multi, r2_score_multi)

fig7 = plt.figure(figsize=(8,8))
plt.scatter(y,y_predict_multi)
plt.show()

X_test = [20, 8246,1968, 1060, 0]
X_test = np.array(X_test).reshape(1,-1)
print(X_test)
y_test_predict = LR_multi.predict(X_test)
print(y_test_predict)