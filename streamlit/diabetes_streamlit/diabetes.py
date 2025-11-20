import streamlit
import pandas
import numpy
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

streamlit.title("Prediction of Diabetes")

data = pandas.read_csv("C:/Users/Neema P Eldho/OneDrive/Desktop/numpy works/diabetes_streamlit/diabetes.csv")
df = pandas.DataFrame(data)
print(df) 


print(df.isna().sum())

X = df.iloc[:,:-1]
Y = df.iloc[:,-1]

print(df.dtypes)

x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.3)


scaler = StandardScaler()
scaler.fit_transform(x_train)
scaler.transform(x_test)

knn = KNeighborsClassifier()
knn = knn.fit(x_train,y_train)

y_pred = knn.predict(x_test)

print(accuracy_score(y_pred,y_test))

#========================================

def input_features():

    Pregnancies = streamlit.number_input("enter the Pregnancies : ",0,20,1)
    Glucose = streamlit.number_input("enter the Glucose : ",0,300,120)
    BloodPressure = streamlit.number_input("enter the BloodPressure : ",0,122,70)
    SkinThickness = streamlit.number_input("enter the SkinThickness : ",0,100,20)
    Insulin  = streamlit.number_input("enter the Insulin  : ",0,900,80)
    BMI = streamlit.number_input("enter the BMI : ",0,70,25)
    DiabetesPedigreeFunction = streamlit.number_input("enter the DiabetesPedigreeFunction : ",0,3,1)
    Age = streamlit.number_input("enter the Age : ",1,120,33)
    

    data1 = {
        "Pregnancies" :Pregnancies,
        "Glucose" : Glucose,
        "BloodPressure" : BloodPressure,
        "SkinThickness" :  SkinThickness,
        "Insulin" : Insulin,
        "BMI" : BMI,
        "DiabetesPedigreeFunction" : DiabetesPedigreeFunction,
        "Age" : Age
    }

    features = pandas.DataFrame(data1,index=[0])
    return features
        
input_df = input_features()
input_scaled = scaler.transform(input_df)
result = knn.predict(input_scaled)

if streamlit.button("show result"):

    final_result = "Diabetic" if result[0] == 0 else "Not Diabetic" # single row [0]

    streamlit.success(final_result)