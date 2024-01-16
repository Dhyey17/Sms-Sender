import requests

reciver_num = input("Enter mobile number(without country code) you want to send message (Indian numbers only): ")
message = input("Enter the message you want to send: ")

url = "https://www.fast2sms.com/dev/bulkV2"

querystring = {"authorization": "cfZLFlNtBv4k9267whUpyHqYCsobPSmn08zDTWexrKjgu15IEJN2K8zZUjWrYP1h5VCLwlkvcqganTDm",
               "message": f"{message}", "language": "english", "route": "q", "numbers": f"{reciver_num}"}

headers = {
    'cache-control': "no-cache"
}

response = requests.request("GET", url, headers=headers, params=querystring, timeout=60)

print(response.text)
