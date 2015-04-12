import requests

text = 'Hello how are you?'
params3 = {'apikey': 'd8894db2dd60aed653e7bd91ea854ce91f46ec85', 'text': text, 'outputMode': 'json'}
analyzedString = requests.get('http://access.alchemyapi.com/calls/text/TextGetTextSentiment',params=params3).json()
print analyzedString['language']



