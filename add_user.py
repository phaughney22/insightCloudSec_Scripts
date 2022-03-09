import requests
import params

base_url = params.url
url = base_url+"v2/public/user/create"
user_email_domain = params.email_domain

# User Inputs

first_name = input("Type user's first name: ")
last_name = input("Type user's last name: ")

# Create user creds from inputs
full_name = first_name + " " + last_name
user_name = first_name + "." + last_name + user_email_domain
email_address = first_name + "." + last_name + user_email_domain


payload = {
    "authentication_type": "saml",
    "access_level": "BASIC_USER",
    "username": user_name,
    "authentication_server_id": 1,
    "name": full_name,
    "email": email_address
}
headers = {
    "Accept": "application/json",
    "content-type": "application/json",
    "accept-encoding": "gzip",
    "Api-Key": params.api_key
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)
