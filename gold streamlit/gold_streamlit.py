import streamlit
import pandas
import numpy
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

streamlit.title("GOLD PRICE AND ASSET COMPARISON DASHBOARD")

data = pandas.read_csv("C:/Users/Neema P Eldho/OneDrive/Desktop/numpy works/gold streamlit/finalDataset_0208.csv")
df = pandas.DataFrame(data)
print(df)

print(df.isna().sum())

#=====================================

df = df.drop(columns=["Dates","URL","FuturePrice","FutureNews"],axis=1)
print(df)

print(df.dtypes)

#======================================

le = LabelEncoder()

df["News"] = le.fit_transform(df["News"])

print(df)

#=======================================

X = df.iloc[:,:-1]
Y = df.iloc[:,-1]

x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.3)


scaler = StandardScaler()
scaler.fit_transform(x_train)
scaler.transform(x_test)

knn = KNeighborsClassifier()
knn = knn.fit(x_train,y_train)

y_pred = knn.predict(x_test)

print(accuracy_score(y_pred,y_test))

print(df.describe)

#========================================


# def input_features():

#     price = streamlit.number_input("enter the price : ")
#     direction_up = streamlit.number_input("enter the direction up : ")
#     direction_constant = streamlit.number_input("enter the direction constant : ")
#     direction_down = streamlit.number_input("enter the direction down : ")
#     past_price = streamlit.number_input("enter the past_price : ")
#     past_news = streamlit.number_input("enter the past news : ")


