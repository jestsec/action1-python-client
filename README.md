# Action1-Python-Client
## An action1 api client for python. 

### How To Use:

#### Set Your Client ID and Secret

##### You can set your keys in the a1client.py
~~~
self.clientId = "YOUR_ACTION1_CLIENT_ID"
self.clientSecret = "YOUR_ACTION1_CLIENT_SECRET"
~~~

#### Import
~~~
from a1client import ActionOne
~~~

#### Get Access Token

~~~
from a1client import ActionOne
act = ActionOne()
act.get_accessToken()
~~~

#### Get Organizations
~~~
from a1client import ActionOne

act = ActionOne()
act.get_accessToken()
orgs = act.get_organizations()

print("Total Orgs: {}".format(orgs['total_items']))
print("ID: {}".format(orgs['items'][0]['id']))
print("Name: {}".format(orgs['items'][0]['name']))
~~~

#### Get Endpoint Information
~~~
orgs = act.get_organizations()
selectedOrg = orgs['id']
getEndpoints = act.endpoints()

print("OS: {}".format(getEndpoints['items'][0]['OS']))
print("Platform: {}".format(getEndpoints['items'][0]['platform']))
print("Status: {}".format(getEndpoints['items'][0]['status']))
print("Private Address: {}".format(getEndpoints['items'][0]['address']))
print("Public Address: {}".format(getEndpoints['items'][0]['external_address']))
print("Last Seen: {}".format(getEndpoints['items'][0]['last_seen']))
print("Device Name: {}".format(getEndpoints['items'][0]['device_name']))
print("Missing Critical Updates: {}".format(getEndpoints['items'][0]['missing_critical_updates']))
print("Other Missing Updates: {}".format(getEndpoints['items'][0]['missing_other_updates']))
~~~

#### Get Updates Needed 
##### You can choose to filter the results by either Unspecified or Important
~~~
getUpdates = act.updates(filter='Unspecified')
for i in getUpdates['items']:
  print(i['name'])
~~~
##### If you dont pass any filter the updates method will return all updates available
~~~
getUpdates = act.updates()
for i in getUpdates['items']:
  print(i['name'])


~~~
