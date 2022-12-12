import requests

# Set the Credentials
base_url = 'https://your_domain.zendesk.com'
ticket_id = 7
request_endpoint = '/api/v2/tickets/' + str(ticket_id)
user = 'your_email' + '/token'
password = 'your_token'

# Request Ticket from Endpoint
response = requests.get(base_url+request_endpoint, auth=(user, password))

# Check status code
if response.status_code != 200:
    print(f"Response Code: {response.status_code}. There was a problem with the request. Exiting.")
    exit()

# Decode JSON Response and get the ticket
data = response.json()
ticket_data = data['ticket']

print(f"Ticket ID: {ticket_data['id']}")
print(f"Subject: {ticket_data['raw_subject']}")
print(f"Description: {ticket_data['description']}")
print(f"Priority: {ticket_data['priority']}")
print(f"Type: {ticket_data['type']}")
print()
