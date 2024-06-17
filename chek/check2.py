import requests
from datetime import datetime ,timedelta

# url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/qu/quote/IBM/default-key-statistics"

# headers = {
# 	"X-RapidAPI-Key": "c763a1ff3dmsh6a56a980225e75cp16acbbjsn058a0a2dbc7f",
# 	"X-RapidAPI-Host": "yahoo-finance15.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers).json()

# print(response)
# print(response["body"]["forwardPE"]["fmt"])


# url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/qu/quote/{}/default-key-statistics".format("TATAPOWER.NS")


# headers = {
# 	"X-RapidAPI-Key": "c763a1ff3dmsh6a56a980225e75cp16acbbjsn058a0a2dbc7f",
# 	"X-RapidAPI-Host": "yahoo-finance15.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers).json()

# print(response)
# print(type(response["body"]["forwardPE"]))

# url = "https://yahoo-finance15.p.rapidapi.com/api/v1/markets/stock/modules"

# querystring = {"ticker":"AAPL","module":"asset-profile"}

# headers = {
# 	"X-RapidAPI-Key": "b3d3d1da69msh07c6984268c8693p112945jsn43abebdc67cf",
# 	"X-RapidAPI-Host": "yahoo-finance15.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)

# print(response.json())


# ******************************** Request for profile

# # import requests

# url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/ne/news/AAPL"

# headers = {
# 	"X-RapidAPI-Key": "b3d3d1da69msh07c6984268c8693p112945jsn43abebdc67cf",
# 	"X-RapidAPI-Host": "yahoo-finance15.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers)

# print(response.json())



# ******************* Request for News for particular company stock


# import requests

# url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/ne/news/AAPL"

# headers = {
# 	"X-RapidAPI-Key": "b3d3d1da69msh07c6984268c8693p112945jsn43abebdc67cf",
# 	"X-RapidAPI-Host": "yahoo-finance15.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers)

# print(response.json())

# ******************************** Check the data for the chart

# import pandas as pd
# import numpy as np


# res = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&outputsize=full&apikey={}".format("AAPL","6V8HYZYHGF4V86E6"))
# data = res.json()

# # Convert json formate into the dataframe

# df = pd.DataFrame(data["Time Series (Daily)"]).T  

# df = df.iloc[::-1, :].reset_index()

# df.rename(columns = {"index":"date" ,"1. open":"open" ,"2. high" :"high" ,"3. low" : "low" ,"4. close":"close" ,"5. volume":"volume" }, inplace = True)

# df = df.astype({
# 'open': float,
# 'high': float,
# 'low': float,
# 'close': float,
# 'volume': int
# })

# df1 = df["close"].tolist()

# print(df1)


print(datetime.now().date())


current_date = datetime.now().date()

    # Generate a list of dates starting from the current date
start_date = current_date
end_date = start_date + timedelta(days=30)  # Generate dates for a week
dates = [(start_date + timedelta(days=i)).strftime('%Y-%m-%d') for i in range((end_date - start_date).days + 1)]

print(dates)