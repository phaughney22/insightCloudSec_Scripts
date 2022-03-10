# insightCloudSec_Scripts
Scripts for automation with Rapid7's insightCloudSec

## Update Parameters and API Key
params.py will need to be updated to define the parameters specific for your installation. 

I use KeePass as an easy way to store API keys with a reasonable level of security so the get_creds.py file utilizes this. params.py reaches out to this so it is easy to swap out if you want to use a different way of storing the API key. 

There are a couple libraries that are required. They are listed in requirements.py and can be installed via:
> $ pip install -r requirements.txt


## Scripts Overview
### insight_list.py
The insight_list.py searches for keywords in custom insights. It takes a keyword input and returns a list of insights with associated IDs. Line 23 contains a URL that should have its parameters updated to be relevant to the specific environment and insight. 

### add_user.py
This script adds a user to ICS. It is currently set to a SAML based user. It takes a first and last name and assumes a format of first.last@domain.com. The domain can be set in the params.py file. 
