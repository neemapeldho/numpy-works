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

print(df["News"].max())
print(df["Price or Not"].max())
print(df["Direction Up"].max())
print(df["Direction Constant"].max())
print(df["Direction Down"].max())
print(df["PastPrice"].max())
print(df["PastNews"].max())

#======================================

le = LabelEncoder()

df["News"] = le.fit_transform(df["News"])

print(df)

print(df.dtypes)
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


#========================================

# max,min needed to find 

def input_features():

    news = streamlit.text_input("enter the news :  ",)
    price = streamlit.number_input("enter the price : ")
    direction_up = streamlit.number_input("enter the direction up : ")
    direction_constant = streamlit.number_input("enter the direction constant : ")
    direction_down = streamlit.number_input("enter the direction down : ")
    past_price = streamlit.number_input("enter the past_price : ")
    past_news = streamlit.number_input("enter the past news : ")


    data1 = {
        "News " :news,
        "Price or Not" : price,
        "Direction Up" : direction_up,
        "Direction Constant" :  direction_constant,
        "Direction Down" : direction_down,
        "PastPrice" : past_price,
        "PastNews" : past_news,
    }

    features = pandas.DataFrame(data1,index=[0])
    return features
        
input_df = input_features()
input_scaled = scaler.transform(input_df)
result = knn.predict(input_scaled)

if streamlit.button("show result"):

    final_result = "Asset Comparision is there" if result[0] == 0 else "Not Asset Comparision" # single row [0]

    streamlit.success(final_result)