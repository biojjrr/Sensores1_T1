import logging
import azure.functions as func
import pyodbc
import pandas as pd
import json
import pickle
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB


def main(req: func.HttpRequest) -> func.HttpResponse:
    req_body = req.get_json()
    variable1 = req_body.get('variable1')
    driverAzure = "ODBC Driver 17 for SQL Server"
    serverAzure = "servidor-sens1.database.windows.net"
    databaseAzure = "matrix"
    usernameAzure = "admin_sens1"
    passwordAzure = "ITM_s1jj"
    conStringAzure = "DRIVER={{{}}};SERVER={};DATABASE={};UID={};PWD={}".format(driverAzure,serverAzure,databaseAzure,usernameAzure,passwordAzure)
    sql = "SELECT * FROM Proteins1"
    conn = pyodbc.connect(conStringAzure)
    df = pd.read_sql(sql,conn)
    Datos = df.to_numpy(dtype='float64')
    x = Datos[:,0:119]
    y = Datos[:,119:120]
    X_train, X_test, Y_train, Y_test = train_test_split(x,y,test_size=0.3,random_state=50)
    #####     SVM     #####
    algoritmo_svm = SVC(gamma='auto')
    algoritmo_svm.fit(X_train, Y_train)
    predicciones = algoritmo_svm.predict(X_test)
    S = classification_report(Y_test, predicciones)
    json_response = json.dumps(S,indent=2)
    #####     KNN     #####
    algoritmo_KNN = KNeighborsClassifier(n_neighbors = 10, metric = 'minkowski', p = 2)
    algoritmo_KNN.fit(X_train, Y_train)
    predicciones1 = algoritmo_KNN.predict(X_test)
    K = classification_report(Y_test, predicciones1)
    json_response1 = json.dumps(K,indent=2)
    #####     Naive Bayes     #####
    algoritmo_NB = GaussianNB()
    algoritmo_NB.fit(X_train, Y_train)
    predicciones2 = algoritmo_NB.predict(X_test)
    N = classification_report(Y_test, predicciones2)
    json_response2 = json.dumps(N,indent=2)
    json_responseT = json_response + json_response1 + json_response2
    if variable1 < 10:
        return func.HttpResponse(json_responseT)
    else:
        return func.HttpResponse("Valor invalido en el Postman!-- Función ejecutada correctamente :)",status_code=200)