# hashumkh gamil id : b3d3d1da69msh07c6984268c8693p112945jsn43abebdc67cf

from flask import Flask ,render_template ,request ,redirect ,session
import mysql.connector
from datetime import datetime
from flask_bcrypt import Bcrypt

import requests
import numpy as np
import pandas as pd
import os

import tensorflow as tf
import math

from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM


headers = {
	"X-RapidAPI-Key": "08f1541678msh2a4747804150020p1237efjsn27b025299ffd",
	"X-RapidAPI-Host": "yahoo-finance15.p.rapidapi.com"
}

app = Flask(__name__)   # Creation of the flask application 
bcrypt = Bcrypt(app)

# For connection with Mysql database

conn = mysql.connector.connect(host="localhost", user="root" ,password="", database="stock_predictor")

cursor = conn.cursor()    # This is used for represent database

# Secret Key for session
app.secret_key=os.urandom(24)     

# Funcation for the compare the two company

def compare_companys(d1 ,d2 ,d1_2 ,d2_2):
    comp1_score = 0
    comp2_score = 0
    insights_record = []
    
    indicators = ["forwardPE" ,"priceToBook"  ,"returnOnEquity" ,"enterpriseValue" ,"totalRevenue" ,"beta" ,"profitMargins" ,"numberOfAnalystOpinions"]
    scores = [5 ,4 ,5 ,3 ,5 ,3 ,3 ,4]
    
    for ind ,scores in zip(indicators, scores):
            if(ind in ["forwardPE" ,"priceToBook" ,"beta"]):
                if((type(d1["body"][ind]) is dict) and (type(d2["body"][ind]) is dict)):
                    if(d1["body"][ind]["raw"] < d2["body"][ind]["raw"]):
                        insights_record.append({ind:d1["meta"]["symbol"],"comp1":d1["body"][ind]["fmt"] ,"comp2":d2["body"][ind]["fmt"]})
                        comp1_score = comp1_score + scores
                    else:
                        insights_record.append({ind:d2["meta"]["symbol"],"comp1":d1["body"][ind]["fmt"] ,"comp2":d2["body"][ind]["fmt"]})
                        comp2_score = comp2_score + scores
                else:
                    insights_record.append({ind:"-","comp1":"-" ,"comp2":"-"})
                    continue
            else:
                if(ind in ["totalRevenue" ,"profitMargins" ,"numberOfAnalystOpinions" ,"returnOnEquity"]):
                    if((type(d1_2["body"][ind]) is dict) and (type(d2_2["body"][ind]) is dict)):
                        if(d1_2["body"][ind]["raw"]> d2_2["body"][ind]["raw"]):
                            insights_record.append({ind:d1_2["meta"]["symbol"],"comp1":d1_2["body"][ind]["fmt"] ,"comp2":d2_2["body"][ind]["fmt"]})
                            comp1_score = comp1_score + scores
                        else:
                            insights_record.append({ind:d2_2["meta"]["symbol"],"comp1":d1_2["body"][ind]["fmt"] ,"comp2":d2_2["body"][ind]["fmt"]})
                            comp2_score = comp2_score + scores
                    else:
                        insights_record.append({ind:"-","comp1":"-" ,"comp2":"-"})
                        continue
                else:
                    if((type(d1["body"][ind]) is dict) and (type(d2["body"][ind]) is dict)):
                        if(d1["body"][ind]["raw"] > d2["body"][ind]["raw"]):
                            insights_record.append({ind:d1["meta"]["symbol"],"comp1":d1["body"][ind]["fmt"] ,"comp2":d2["body"][ind]["fmt"]})
                            comp1_score = comp1_score + scores
                        else:
                            insights_record.append({ind:d2["meta"]["symbol"],"comp1":d1["body"][ind]["fmt"] ,"comp2":d2["body"][ind]["fmt"]})
                            comp2_score = comp2_score + scores
                    else:
                        insights_record.append({ind:"-","comp1":"-" ,"comp2":"-"})
                        continue
 
                        
    if(comp1_score > comp2_score):
        return {"win" :d1["meta"]["symbol"] ,"loss":d2["meta"]["symbol"]} ,insights_record
    else:
        return {"win":d2["meta"]["symbol"] ,"loss":d1["meta"]["symbol"]} ,insights_record

# For creation of dataset

def create_dataset(dataset ,time_stemp):
    x_data = []
    y_data = []
    
    for i in range(len(dataset)-time_stemp-1):
        a = dataset[i:i+time_stemp ,0]
        x_data.append(a)
        y_data.append(dataset[i+time_stemp ,0])
        
    return np.array(x_data) ,np.array(y_data)

# ********************************************* Routes for URL *********************************************

@app.route("/home")
def home():
    if 'user_id' in session:
        return render_template("index.html")
    else:
        return redirect("/")


# Login and Singup Routes

@app.route("/") 
def login_signup():
    if 'user_id' in session:   
        return redirect("/home")
    else:
        return render_template("login_signup.html")


@app.route("/login" ,methods=["POST"])
def login_validation():
    Email = request.form.get("Lemail")
    Password = request.form.get("Lpassword")
    
    cursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}'""".format(Email))    # All database data is store into the cursor
    users = cursor.fetchall()
    
    print(users)
    if (len(users)>0):
        if(bcrypt.check_password_hash(users[0][3],Password)):
            session['user_id'] = users[0][0]    # We are add loged in user id into the session 
            return redirect("/home")
        else:
            return redirect("/") 
    else:
        return redirect("/")


@app.route("/signup" ,methods=["POST"])
def signup_validation():
    
    Uname = request.form.get("Susername")
    Email = request.form.get("Semail")
    Password = request.form.get("Spassword")
    
    cursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}'""".format(Email))
    users = cursor.fetchall()
    
    if(len(users) > 0):
        return redirect("/")
    else:
        hashed_password = bcrypt.generate_password_hash(Password).decode('utf-8')
        
        cursor.execute("""INSERT INTO `users` (`id` ,`username` ,`email` ,`password` ,`join_date`) VALUES (NULL,'{}','{}','{}','{}')""".format(Uname ,Email ,hashed_password ,datetime.now()))
        conn.commit()     # After Insert Data Commit is Importent

        cursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}'""".format(Email))
        user = cursor.fetchall()
        
        session['user_id'] = user[0][0]

        return redirect("/home")


@app.route("/logout" ,methods=["GET"])
def logout():
    session.pop('user_id')
    return redirect("/")
    

@app.route("/companyinfo" ,methods=["GET", "POST"])
def search_company():
    if 'user_id' in session:
        if(request.method == "POST"):
            query = request.form.get("searchbar")

            return redirect("/companyinfo/"+query)
    else:
        return redirect("/")


@app.route("/companyinfo/<string:ticker>" ,methods=["GET"])
def compnayinfo(ticker):
    
        if 'user_id' in session:
            
            # Company Overview Data

            url_p = "https://yahoo-finance15.p.rapidapi.com/api/v1/markets/stock/modules"
            url_s = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/qu/quote/{}/default-key-statistics".format(ticker)    # [BookValue ,enterpriseValue ,]
            url_f = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/qu/quote/{}/financial-data".format(ticker)  # [ebitda ,]
            url_n = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/ne/news/{}".format(ticker)

            querystring = {"ticker":ticker,"module":"asset-profile"}

            res_p = requests.get(url_p, headers=headers, params=querystring).json()
            res_s = requests.get(url_s , headers=headers).json()
            res_f = requests.get(url_f ,headers=headers).json()
            res_n = requests.get(url_n ,headers=headers).json()

            return render_template("companyinfo.html" ,d_p=res_p ,d_s=res_s ,d_f=res_f ,d_n=res_n)

        else:
            return redirect("/")
            

@app.route("/companyMoreDetails/<string:ticker>" ,methods=["GET"]) 
def companyMoreDetails(ticker):
    
    if 'user_id' in session:
        # Company Overview Data

        res = requests.get("https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey=demo".format(ticker))
        data = res.json()
        
        return render_template("companyinfo.html" ,data=data)
    
    else:
        return redirect("/")
        

@app.route("/compare" ,methods=["GET", "POST"])
def compare():
    
    if 'user_id' in session:
        
        if(request.method == "POST"):

            comp1 = request.form.get("comp1_inp")
            comp2 = request.form.get("comp2_inp")

            url1 = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/qu/quote/{}/default-key-statistics".format(comp1)
            url2 = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/qu/quote/{}/default-key-statistics".format(comp2)

            # totalRevenue  ,profitMargins ,numberOfAnalystOpinions ,returnOnEquity  from below url

            url1_2 = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/qu/quote/{}/financial-data".format(comp1)
            url2_2 = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/qu/quote/{}/financial-data".format(comp2)


            data1 = requests.get(url1, headers=headers).json()
            data2 = requests.get(url2,headers=headers).json()

            data1_2 = requests.get(url1_2, headers=headers).json()
            data2_2 = requests.get(url2_2,headers=headers).json()

            result ,insights_record = compare_companys(data1 ,data2 ,data1_2 ,data2_2)

            return render_template("compare_result.html" , result=result ,ins_record=insights_record ,cs_1=data1["meta"]["symbol"] ,cs_2=data2["meta"]["symbol"])      # Compare_result.html is similar to the compare file only add company information table and at the end give the result of the compare { For the write both company informatio you can used the table for the both company}

        return render_template("compare.html")  # compare.html is contain only two input column where user enter the company name
    else:
        return redirect("/")
            
        
@app.route("/compare_result" ,methods=["GET"])
def compare_result():
    if 'user_id' in session:
        return render_template("compare_result.html")    
    else:
        return redirect("/")


@app.route("/predict" ,methods=["GET" ,"POST"])
def predict():

    if 'user_id' in session:
        
        if(request.method=="POST"):
            ticker = request.form.get("search_comp")
            return redirect("/predict/" + ticker)

        return render_template("predict.html")
    else:
        return redirect("/")


@app.route("/predict/<string:ticker>")
def predict_result(ticker):
    if 'user_id' in session:
        # Write a code for the featch data from the api and write code for the prediction on data .
        # You can send the predicted value into the prediction _result for the draw a graph.
        res = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&outputsize=full&apikey={}".format(ticker,"6V8HYZYHGF4V86E6"))
        data = res.json()

        # Convert json formate into the dataframe

        df = pd.DataFrame(data["Time Series (Daily)"]).T  

        df = df.iloc[::-1, :].reset_index()

        df.rename(columns = {"index":"date" ,"1. open":"open" ,"2. high" :"high" ,"3. low" : "low" ,"4. close":"close" ,"5. volume":"volume" }, inplace = True)

        df = df.astype({
        'open': float,
        'high': float,
        'low': float,
        'close': float,
        'volume': int
        })

        df1 = df[["close"]]

        # doing Scaling on data 

        scaler = MinMaxScaler(feature_range =(0,1))
        df1 = scaler.fit_transform(df1)

        # Perform Train Test Split

        train_size = int(len(df1)*0.65)
        test_size = len(df1)-train_size

        train_data = df1[:train_size ,:]
        test_data = df1[train_size: ,:]

        time_stemp = 100

        x_train ,y_train = create_dataset(train_data ,time_stemp)
        x_test ,y_test = create_dataset(test_data ,time_stemp)

        # Now Reshape dataset which is requierd for the LSTM

        x_train = x_train.reshape(x_train.shape[0] ,x_train.shape[1] ,1)    # Here we are convert 2D to 3D for LSTM
        x_test = x_test.reshape(x_test.shape[0] ,x_test.shape[1] ,1)

        # Now train LSTM model on over dataset
        model = Sequential()

        model.add(LSTM(50 ,return_sequences=True ,input_shape=(x_train.shape[1] ,x_train.shape[2])))
        model.add(LSTM(50 ,return_sequences=True))
        model.add(LSTM(50))

        model.add(Dense(1))

        model.compile(loss='mean_squared_error',optimizer='adam')

        model.fit(x_train ,y_train ,validation_data=(x_test ,y_test) ,epochs=10 ,batch_size=64 ,verbose=1)

        # Predict for Future 30+ day

        train_predict = model.predict(x_train)
        test_predict = model.predict(x_test)

        train_pred = scaler.inverse_transform(train_predict)
        test_pred = scaler.inverse_transform(test_predict)

        # Now we are predict future 30 days

        x_input = test_data[-100:].reshape(1,-1)

        temp_input = list(x_input)

        temp_input = temp_input[0].tolist()

        lst_output = []
        n_steps = 100
        i=0

        while(i<30):

            if(len(temp_input) >x_input.shape[1]):
                x_input = np.array(temp_input[1:])
                x_input=x_input.reshape(1,-1)
                x_input = x_input.reshape((1, n_steps, 1))

                y_pred = model.predict(x_input ,verbose=0)

                temp_input.extend(y_pred[0].tolist())
                temp_input=temp_input[1:]

                lst_output.extend(y_pred.tolist())
                i=i+1

            else:
                x_input = x_input.reshape((1, n_steps,1))
                y_pred = model.predict(x_input, verbose=0)

                temp_input.extend(y_pred[0].tolist())

                lst_output.extend(y_pred.tolist())
                i=i+1

        day_new = np.arange(1,x_input.shape[1]+1)    # This is index for the previews days
        day_pred = np.arange(x_input.shape[1]+1,x_input.shape[1]+1+30) # this is is index for prediction day

        df1_trf = scaler.inverse_transform(df1)
        lst_output_trf = scaler.inverse_transform(lst_output)

        df1_list = df1_trf.reshape(-1).tolist()
        out_lst = lst_output_trf.reshape(-1).tolist()

        pred_data = df1_list + out_lst

        dates = df["date"].tolist()

        return render_template("predict_result.html" ,pd=pred_data ,out_lst=out_lst,dates=dates)

    else:
        return redirect("/")
    

if (__name__ == "__main__"):
    app.run(debug=True)




# Source for the request ===>  https://tedboy.github.io/flask/generated/generated/flask.Request.html