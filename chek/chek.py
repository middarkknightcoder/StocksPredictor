# import requests

# url = "https://yahoo-finance15.p.rapidapi.com/api/v2/markets/tickers"

# querystring = {"type":"IBM","page":"5"}

# headers = {
# 	"X-RapidAPI-Key": "c763a1ff3dmsh6a56a980225e75cp16acbbjsn058a0a2dbc7f",
# 	"X-RapidAPI-Host": "yahoo-finance15.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)

# print(response.json())


# https://rapidapi.com/sparior/api/yahoo-finance15

import requests

headers = {
	"X-RapidAPI-Key": "08f1541678msh2a4747804150020p1237efjsn27b025299ffd",
	"X-RapidAPI-Host": "yahoo-finance15.p.rapidapi.com"
}

comp1 = "TATAPOWER.NS"
comp2 = "ADANIPOWER.NS"

# url1 = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/qu/quote/{}/default-key-statistics".format(comp1)
# url2 = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/qu/quote/{}/default-key-statistics".format(comp2)

# url1_2 = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/qu/quote/{}/financial-data".format(comp1)
# url2_2 = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/qu/quote/{}/financial-data".format(comp2)


# data1 = requests.get(url1, headers=headers).json()
# data2 = requests.get(url2,headers=headers).json()

# data1_2 = requests.get(url1_2, headers=headers).json()
# data2_2 = requests.get(url2_2,headers=headers).json()

# def compare_companys(d1 ,d2 ,d1_2 ,d2_2):
#     comp1_score = 0
#     comp2_score = 0
#     insights_record = []
    
#     indicators = ["forwardPE" ,"priceToBook"  ,"returnOnEquity" ,"enterpriseValue" ,"totalRevenue" ,"beta" ,"profitMargins" ,"numberOfAnalystOpinions"]
#     scores = [5 ,4 ,5 ,3 ,5 ,3 ,3 ,4]
    
#     for ind ,scores in zip(indicators, scores):
#             if(ind in ["forwardPE" ,"priceToBook" ,"beta"]):
#                 if((type(d1["body"][ind]) is dict) and (type(d2["body"][ind]) is dict)):
#                     if(d1["body"][ind]["raw"] < d2["body"][ind]["raw"]):
#                         insights_record.append({ind:d1["meta"]["symbol"]})
#                         comp1_score = comp1_score + scores
#                     else:
#                         insights_record.append({ind:d2["meta"]["symbol"]})
#                         comp2_score = comp2_score + scores
#                 else:
#                     continue
#             else:
#                 if(ind in ["totalRevenue" ,"profitMargins" ,"numberOfAnalystOpinions" ,"returnOnEquity"]):
#                     if((type(d1_2["body"][ind]) is dict) and (type(d2_2["body"][ind]) is dict)):
#                         if(d1_2["body"][ind]["raw"]> d2_2["body"][ind]["raw"]):
#                             insights_record.append({ind:d1_2["meta"]["symbol"]})
#                             comp1_score = comp1_score + scores
#                         else:
#                             insights_record.append({ind:d2_2["meta"]["symbol"]})
#                             comp2_score = comp2_score + scores
#                     else:
#                         continue
#                 else:
#                     if((type(d1["body"][ind]) is dict) and (type(d2["body"][ind]) is dict)):
#                         if(d1["body"][ind]["raw"] > d2["body"][ind]["raw"]):
#                             insights_record.append({ind:d1["meta"]["symbol"]})
#                             comp1_score = comp1_score + scores
#                         else:
#                             insights_record.append({ind:d2["meta"]["symbol"]})
#                             comp2_score = comp2_score + scores
#                     else:
#                         continue
 
                        
#     if(comp1_score > comp2_score):
#         return d1["meta"]["symbol"] ,insights_record
#     else:
#         return d2["meta"]["symbol"] ,insights_record


# result ,insights_record = compare_companys(data1 ,data2 ,data1_2 ,data2_2) 
    
# print(f"The result is {result}")
# print(insights_record)
    
    
'''
    totalRevenue   :  url1_2
    profitMargins  : url1_2
    numberOfAnalystOpinions : url1_2
    "returnOnEquity": url1_2
    numberOfAnalystOpinions  : This is REcomendation for the buy
    '''
    
def compare_companys(d1 ,d2 ,d1_2 ,d2_2):
    comp1_score = 0
    comp2_score = 0
    insights_record = []
    
    indicators = ["forwardPE" ,"priceToBook"  ,"returnOnEquity" ,"enterpriseValue" ,"totalRevenue" ,"beta" ,"profitMargins" ,"numberOfAnalystOpinions"]
    scores = [5 ,4 ,5 ,3 ,5 ,3 ,3 ,4]
    i=0
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
                    insights_record.append({ind:"","comp1":"" ,"comp2":""})
                    i=i+1
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
                        insights_record.append({ind:"","comp1":"" ,"comp2":""})
                        i=i+1
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
                        insights_record.append({ind:"","comp1":"" ,"comp2":""})
                        i=i+1
                        continue
 
                        
    if(comp1_score > comp2_score):
        return d1["meta"]["symbol"] ,insights_record
    else:
        return d2["meta"]["symbol"] ,insights_record
    
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

print(result)
print(insights_record)