import requests

reciver_num = input("Enter mobile number(without country code) you want to send message (Indian numbers only): ")
message = input("Enter the message you want to send: ")

url = "https://www.fast2sms.com/dev/bulkV2"

querystring = {"authorization": "btYUDF3u4ljSPqaWZdhTMfJQr6oi8IRgx1pXzE27LeV5G9wsCcSGaP8AR4MvcextQwlu2YEpmJOV19Cq",
               "message": f"{message}", "language": "english", "route": "q", "numbers": f"{reciver_num}"}

headers = {
    'cache-control': "no-cache"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
