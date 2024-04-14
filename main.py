from flask import Flask ,render_template ,request
import requests

app = Flask(__name__)   # Creation of the flask application 

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/companyinfo" ,methods=["GET" ,"POST"])
def compnayinfo():
    if(request.method == "POST"):
        # Company Overview Data
        
        query = request.form.get("searchbar")
        
        res = requests.get("https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey=demo".format(query))
        data = res.json()
        
        return render_template("companyinfo.html" ,data=data)


@app.route("/companyMoreDetails/<string:ticker>" ,methods=["GET"]) 
def companyMoreDetails(ticker):
        # Company Overview Data
    
        res = requests.get("https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey=demo".format(ticker))
        data = res.json()
        
        return render_template("companyinfo.html" ,data=data)


@app.route("/compare" ,methods=["GET", "POST"])
def compare():
    
    if(request.method == "POST"):
        
        comp1 = request.form.get("")
        comp2 = request.form.get("")
        
        res1 = requests.get("https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey=6V8HYZYHGF4V86E6".format(comp1))
        data1 = res1.json()

        res2 = requests.get("https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey=6V8HYZYHGF4V86E6".format(comp2))
        data2 = res1.json()
        
        result ,insights_record = compare_companys(data1 ,data2)
        
        return render_template("compare_result.html" ,data1=data1 ,data2=data2 ,result=result ,insights_record=insights_record)      # Compare_result.html is similar to the compare file only add company information table and at the end give the result of the compare { For the write both company informatio you can used the table for the both company}
        
    return render_template("compare.html")  # compare.html is contain only two input column where user enter the company name
        
        
def compare_companys(d1 ,d2):
    comp1_score = 0
    comp2_score = 0
    insights_record = []
    
    indicators = ["PERatio" ,"PriceToBookRatio" ,"ReturnOnEquityTTM" ,"MarketCapitalization" ,"RevenueTTM" ,"QuarterlyRevenueGrowthYOY" ,"DividendYield" ,"Beta" ,"ProfitMargin" ,"AnalystRatingBuy"]
    scores = [5 ,4 ,5 ,4 ,5 ,5 ,1 ,3 ,3 ,3 ,4]
    
    for ind ,scores in zip(indicators, scores):
        if(ind in ["PERatio" ,"PriceToBookRatio" ,"Beta"]):
            if(d1[ind] < d2[ind]):
                insights_record.append(d1["Symbol"])
                comp1_score = comp1_score + scores
            else:
                insights_record.append(d2["Symbol"])
                comp2_score = comp2_score + scores
        else:
            if(d1[ind] > d2[ind]):
                insights_record.append(d1["Symbol"])
                comp1_score = comp1_score + scores
            else:
                insights_record.append(d2["Symbol"])
                comp2_score = comp2_score + scores
    
    if(comp1_score > comp2_score):
        return zip(d1["Symbol"] ,insights_record)
    else:
        return zip(d2["Symbol"] ,insights_record)
    
if (__name__ == "__main__"):
    app.run(debug=True)




'''
Price-to-Earnings (P/E) Ratio - 5   L ( low is better then higer)
Price-to-Book (P/B) Ratio - 4   L
Return on Equity (ROE) - 5  H
Market Capitalization - 4    H
Debt-to-Equity Ratio - 3    Not found
Revenue -5   H
Earnings Growth - 5   H
Volatility - 2   Not found   
Dividend Yield - 1   H
Beta - 3   L 
ProfitMargin - 3   H
Analyst Recommendations - 4   H
'''