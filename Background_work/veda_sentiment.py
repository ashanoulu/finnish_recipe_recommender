# import requests
#
# url = "https://translation.googleapis.com/language/translate/v2"
# # key = "cbd7830bcf8a4e46c99631f15498e93c30e02653"
# key = "cf9a66c0d47a11b2d1b0f1e6c39280d4fb9a4886"
#
# params = {
#     "q": "Hello world",
#     "source": "en",
#     "target": "es",
#     "key": key
# }
#
# response = requests.post(url, params=params)
#
# if response.status_code == 200:
#     result = response.json()
#     translated_text = result["data"]["translations"][0]["translatedText"]
#     print(translated_text)
# else:
#     print("Error:", response.status_code, response.text)

import google.cloud

# Set up authentication
translate_client = translate.Client.from_service_account_json('path/to/keyfile.json')