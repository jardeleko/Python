import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#%matplotlib inline

USAhousing = pd.read_csv('USA_Housing.csv')
type(USAhousing)
USAhousing.head()
USAhousing.describe()
USAhousing.columns
#sns.distplot(USAhousing['Price'], color='black')
#plt.show()
X = USAhousing[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
               'Avg. Area Number of Bedrooms', 'Area Population']]
y = USAhousing['Price']
#sns.pairplot(USAhousing)
#plt.show()
#sns.heatmap(USAhousing.corr())
#plt.show()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=101)

lm = LinearRegression()
lm.fit(X_train,y_train)

coeff_df = pd.DataFrame(lm.coef_,X.columns,columns=['Coefficient'])
#print(coeff_df)

predictions = lm.predict(X_test)

#plt.scatter(y_test,predictions)
#plt.xlabel('Price')
#plt.ylabel('Predictions')
#plt.show()

from sklearn import metrics

MAE = metrics.mean_absolute_error(y_test, predictions)

print('MAE_NORMALIZADO:', MAE/y.mean())
print('MSE_NORMALIZADO:', metrics.mean_squared_error(y_test, predictions)/y.mean())
print('RMSE_NORMALIZADO:', np.sqrt(metrics.mean_squared_error(y_test, predictions))/y.mean())

print("\n\n")

from sklearn.model_selection import KFold
from sklearn import metrics
from sklearn.model_selection import cross_val_score

scores = []
best_lm = LinearRegression()
kf = KFold(n_splits=5, random_state=30, shuffle=True)

print ("Tamanho de X:",len(X), "\n")

for train_index, test_index in kf.split(X):
    #print("Train Index: ", train_index,len(train_index))
    #print("Test Index: ", test_index, len(test_index),"\n")
    
    X_train, X_test = X.loc[train_index], X.loc[test_index]
    y_train, y_test = y.loc[train_index], y.loc[test_index]
    
    best_lm.fit(X_train,y_train)
    predictions = best_lm.predict(X_test)
     
    MAE = metrics.mean_absolute_error(y_test, predictions)
    print("MAE: ",MAE)
    print('MAE_NORMALIZADO:', MAE/y.mean())
    
    resultado = cross_val_score(best_lm, X_test, y_test, cv = 5)
    print("SCORE: ",resultado.mean())
    
    coeff_df = pd.DataFrame(best_lm.coef_,X.columns,columns=['Coefficient'])
    print(coeff_df,"\n\n\n\n\n ")