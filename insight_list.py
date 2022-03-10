import requests
import params
import sys
import json

base_url = params.url

# Get search keyword from user
def keyword_getter():
    key_word = input('What keyword would you like to search insights for?: ')
    return key_word

def main(borrowed_key_word):
    keyword_search(borrowed_key_word)
    selection_to_use = keyword_selection()
    print('Selected: ' +selection_to_use)
    return(selection_to_use)



def keyword_search(borrowed_key_word):
    # Build URL
    url = base_url+"v2/public/insights/select?source=custom&labels=BLKB&search="+borrowed_key_word

    headers = {
        "Accept": "application/json",
        "content-type": "application/json",
        "accept-encoding": "gzip",
        "Api-Key": params.api_key
    }

    response = requests.request("GET", url, headers=headers)

    results = response.text

    # Load into parsable json and isolate relevent data
    results_json = json.loads(results)
    data = results_json['data']
    data_dump = json.dumps(data)
    data_to_parse = json.loads(data_dump)

    # Display names and insight IDs
    print('ID | Name')

    for insight_data in data_to_parse:
        insight_id = insight_data['insight_id']
        insight_name = insight_data['name']
        print(str(insight_id) + ' | ' + insight_name)

def keyword_selection():
    selection = input('Please enter the Insight ID you would like to use. If you would like to search again, enter "retry". If you would like to quit, enter "exit".:')
    if selection == 'retry':
        keyword_search()
    if selection == 'exit':
        print('Exiting...')
    else:
        insight_id_to_use = selection
        return(insight_id_to_use)



#Main
borrowed_key_word = keyword_getter()
id_selection = main(borrowed_key_word)

#f = open('results.txt', 'w')
#print(response.text, file=f)
