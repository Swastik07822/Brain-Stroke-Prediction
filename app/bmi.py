import requests

url = "https://body-mass-index-bmi-calculator.p.rapidapi.com/metric"

querystring = {"weight":"150","height":"1.83"}

headers = {
	"x-rapidapi-key": "7e1b01dc8bmshb4b9a6e64d93d79p183994jsnd7ec8c5a6df6",
	"x-rapidapi-host": "body-mass-index-bmi-calculator.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())