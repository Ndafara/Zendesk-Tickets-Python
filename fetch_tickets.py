import requests

# Set the Credentials
base_url = 'https://your_domain.zendesk.com'
request_endpoint = '/api/v2/tickets'
user = 'your_email' + '/token'
password = 'your_token'

# Request Tickets from Endpoint
response = requests.get(base_url+request_endpoint, auth=(user, password))

# Check status code
if response.status_code != 200:
    print(f"Response Code: {response.status_code}. There was a problem with the request. Exiting.")
    exit()

# Decode JSON Response and get tickets
data = response.json()
ticket_list = data['tickets']

# Loop through the tickets and print details
for ticket in ticket_list:
    print(f"Ticket ID: {ticket['id']}")
    print(f"Subject: {ticket['raw_subject']}")
    print(f"Description: {ticket['description']}")
    print(f"Priority: {ticket['priority']}")
    print(f"Due Date: {ticket['due_at']}")
    print()
