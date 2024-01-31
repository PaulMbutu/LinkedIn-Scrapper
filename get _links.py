import requests
import os
import csv

Api_KEY=open('api_key.txt').read()
Search_ID=open('search_engine_id.txt').read()

search_query='site:linkedin.com/in "building" or "architecture" or "architect" or "construction" and ("Kenya" or  "Uganda" or "Rwanda")'

url= 'https://www.googleapis.com/customsearch/v1'



def write_to(file_name,lst):
    csv_file_path = f"C:\\Users\\{file_name}"   #edit accordingly

    # Open the CSV file in write mode with newline='' to prevent extra newlines

    print(f"writting {file_name}")
    with open(csv_file_path, 'w', newline='') as csvfile:
        # Create a CSV writer
        csvwriter = csv.writer(csvfile)

        # Write each row from the list to the CSV file
        for row in lst:
                csvwriter.writerow([row])
all_links=[]
for i in range(1,100,10):
    params={
        'q':    search_query,
        'key':  Api_KEY,
        'cx':   Search_ID,
        'start': i

    }
    response=requests.get(url,params=params)
    results=response.json()['items']

    for item in results:

        all_links.append(item['link'])
write_to("gathered_links.csv",all_links)
