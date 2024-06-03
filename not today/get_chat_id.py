from requests import get

api_req = 'https://api.telegram.org/bot7191032155:AAFmw9T1Idrj7tzHAOHZfyOauTTp0rdxmPg'

updates = get(api_req + '/getUpdates?offset=-1').json()

print(updates)

m = updates['result'][0]['message']

chat_id = m['from']['id']
print(chat_id)
text = m['text']

send_message = get(api_req + f'/sendMessage?chat_id={chat_id}&text={text}')