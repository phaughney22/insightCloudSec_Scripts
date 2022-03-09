from getpass4 import getpass
from pykeepass import PyKeePass

# Get user's KeePassDB Password and db name
db_pw = getpass('KeePassDB Password: ')

# Name/location of the KeepPass db file
db_name = 'api_key_db.kdbx'

# Use password to load keepassdb database file and get api key from entry
kpdb = PyKeePass(db_name, db_pw)
entry = kpdb.find_entries(title='ics_api', first=True)

# set actual
ics_api_key = entry.password
