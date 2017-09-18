import sqlite3
import pandas as pd 
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from math import sqrt


# Create your connection.
cnx = sqlite3.connect('database.sqlite')
df = pd.read_sql_query("SELECT * FROM Player_Attributes", cnx)


features = [
       'potential', 'crossing', 'finishing', 'heading_accuracy',
       'short_passing', 'volleys', 'dribbling', 'curve', 'free_kick_accuracy',
       'long_passing', 'ball_control', 'acceleration', 'sprint_speed',
       'agility', 'reactions', 'balance', 'shot_power', 'jumping', 'stamina',
       'strength', 'long_shots', 'aggression', 'interceptions', 'positioning',
       'vision', 'penalties', 'marking', 'standing_tackle', 'sliding_tackle',
       'gk_diving', 'gk_handling', 'gk_kicking', 'gk_positioning',
       'gk_reflexes']


target = ['overall_rating']

df = df.dropna()

print df.iloc[2]

X = df[features]

y = df[target]

print X.iloc[2]

print y.iloc[2]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=324)

regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_prediction = regressor.predict(X_test)
#y_prediction

print y_test.describe()

Xtest1=X_test.iloc[5].reshape(1,34)

print "Xtest1=", Xtest1

y1=regressor.predict(Xtest1)

print "y1=", y1
RMSE = sqrt(mean_squared_error(y_true = y_test, y_pred = y_prediction))

print(RMSE)