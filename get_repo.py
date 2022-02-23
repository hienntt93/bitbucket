# Step 1
from atlassian import Bitbucket
bitbucket = Bitbucket(url="https://api.bitbucket.org",username='{username}',password='{password}',cloud=True)

#Step 2
import csv
f = open('repo_list.csv','w', newline = '')
columns = ['project','full_name','language','owner','created_on','updated_on']
writer = csv.DictWriter(f, fieldnames=columns)
writer.writeheader()

repos = bitbucket.get_repositories('{organization}')
for i in repos: 
    writer.writerow({'project':i['project']['name'], 'full_name':i['full_name'], 'language': i['language'], 'owner': i['owner']['username'],'created_on':i['created_on'],'updated_on':i['updated_on']})
    
f.close()
