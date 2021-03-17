import json 
  
f = open('response.json') 
releases = json.load(f) 

for release in releases: 
    print(release["tag_name"]) 

f.close() 
