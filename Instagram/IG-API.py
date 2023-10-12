from instagram_private_api import Client, ClientCompatPatch

# Replace with your Instagram app credentials
username = 'your_username'
password = 'your_password'
user_id = 'your_user_id'

# Create an Instagram API client
api = Client(username, password)
results = api.user_feed(user_id)

for post in results:
    print(post['caption']['text'])
