import requests

# url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/qu/quote/IBM/default-key-statistics"

# headers = {
# 	"X-RapidAPI-Key": "c763a1ff3dmsh6a56a980225e75cp16acbbjsn058a0a2dbc7f",
# 	"X-RapidAPI-Host": "yahoo-finance15.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers).json()

# print(response)
# print(response["body"]["forwardPE"]["fmt"])


url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/qu/quote/{}/default-key-statistics".format("TATAPOWER.NS")


headers = {
	"X-RapidAPI-Key": "c763a1ff3dmsh6a56a980225e75cp16acbbjsn058a0a2dbc7f",
	"X-RapidAPI-Host": "yahoo-finance15.p.rapidapi.com"
}

response = requests.get(url, headers=headers).json()

print(response)
print(type(response["body"]["forwardPE"]))

