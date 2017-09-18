import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


data = pd.read_csv('./weather/daily_weather.csv')

data[data.isnull().any(axis=1)]

del data['number']

before_rows = data.shape[0]
print(before_rows)

data = data.dropna()

after_rows = data.shape[0]


print(after_rows)

clean_data = data.copy()
clean_data['high_humidity_label'] = (clean_data['relative_humidity_3pm'] > 24.99)*1
#print(clean_data['high_humidity_label'])


y=clean_data[['high_humidity_label']].copy()


#clean_data['relative_humidity_3pm'].head()


morning_features = ['air_pressure_9am','air_temp_9am','avg_wind_direction_9am','avg_wind_speed_9am',\
        'max_wind_direction_9am','max_wind_speed_9am','rain_accumulation_9am',\
        'rain_duration_9am']
X = clean_data[morning_features].copy()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=324)
humidity_classifier = DecisionTreeClassifier(max_leaf_nodes=10, random_state=0)
humidity_classifier.fit(X_train, y_train)
#type(humidity_classifier)

predictions = humidity_classifier.predict(X_test)
#predictions[:10]
print "shape:",X_test.shape


X_test1=X_test.iloc[0].reshape(1,8)
print X_test1
#print "W_test:", X_test[0,...], X_test1.shape

predictions1=humidity_classifier.predict(X_test1)
print "predict", predictions1

#y_test['high_humidity_label'][:10]

#accuracy_score(y_true = y_test, y_pred = predictions)
