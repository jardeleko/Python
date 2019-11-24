import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
import py_compile 
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.linear_model import LinearRegression

data_UShouse = pd.read_csv('USA_Housing.csv')
data_UShouse.head()
data_UShouse.describe()
data_UShouse.columns
#sns.distplot(data_UShouse['Price'], color='black')
#plt.show() verificação da distribuição da variavel resposta, disponivel em grafico
X = data_UShouse[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
   				  'Avg. Area Number of Bedrooms', 'Area Population']]
y = data_UShouse['Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=101)
#sns.pairplot(data_UShouse)
#plt.show() graficos de dispersão dos clusters

#sns.heatmap(data_UShouse.corr())
#plt.show() mapa de calor, onde as cores mais claras representam maoir relação na tabela

lm = LinearRegression()
lm.fit(X_train, y_train)
coeff_df = pd.DataFrame(lm.coef_, X.columns, columns=['Coefficient'])
coeff_df
predictions = lm.predict(X_test)
plt.scatter(y_test, predictions)
plt.xlabel('Price')
plt.ylabel('Predictions')
plt.show() #grafico da avaliação das previsçoes dos testes
print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))
print("Visite o site www.kaggle.com e poste o seu notebook com a solução para o Dataset 'USA_Housing.csv'.")

