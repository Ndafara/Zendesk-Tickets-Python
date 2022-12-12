import requests
import json

# Set the Credentials
base_url = "https://your_domain.zendesk.com"
request_endpoint = "/api/v2/tickets"
user = "your_email" + "/token"
password = "your_token"
headers = {"content-type": "application/json"}

# New ticket information
subject = "Python API Test Ticket One"
body = "Demonstrating creating a ticket with the Zendesk API using Python"
type = "question"
priority = "normal"

# Package the data into a Dictionary
data = {"ticket": {"subject": subject, "type": type, "priority": priority, "comment": {"body": body}}}

# Encode the data to create a JSON payload
payload = json.dumps(data)

# Send the HTTP post request
response = requests.post(base_url+request_endpoint, data=payload, auth=(user, password), headers=headers)

# Check for HTTP codes other than 201 (Created)
if response.status_code != 201:
    print(f"Response Code: {response.status_code}. There was a problem with the request. Exiting.")
    exit()

print('Successfully created the ticket.')
