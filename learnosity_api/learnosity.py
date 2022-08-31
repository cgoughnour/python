from learnosity_sdk.request import DataApi

security = {
    'consumer_key': '',      
    'domain': 'localhost'
}
# WARNING: The consumer secret should not be committed to source control.
consumer_secret = ''
endpoint = 'https://data.learnosity.com/v1/sessions/responses'
data_request = {
    'activity_id': ['9e0dec39-7842-4323-b45c-3f2b07ba21f1'],
    #'session_id': ['ed6d7694-461c-3fcc-a38b-49ed1dc409de'],
    'user_id': ['531e84eb13561e2126f8313d00865604'],
}
action = 'get'

client = DataApi()

res = client.request(endpoint, security, consumer_secret, data_request, action)
response = res.json()
for x in response["data"]:
    print(" student_id: " + x["user_id"] +", session_id: " + str(x["session_id"]) + ", num_attempted: " + str(x["num_attempted"]) + ", score: " + str(x["score"]) + "/" + str(x["max_score"]))
#print(response['data'])