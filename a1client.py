import requests
import json


class ActionOne:
    def __init__(self):
        self.clientId = "YOUR_ACTION1_CLIENT_ID"
        self.clientSecret = "YOUR_ACTION1_CLIENT_SECRET"
        self.organizationId = ""
        self.organizationName = ""
        self.accessToken = ""
    
    def get_accessToken(self):
        data = "client_id=api-key-c4504b74-48d2-db47-12da-4aa6f61562a67224feab-470d-4569-8801-2959455ccd30@action1.com&client_secret=63d4d691b1835ffe84ced5ee92eac3c8"
        headers = {"Content-Type":"application/x-www-form-urlencoded"}
        req = requests.post("https://app.action1.com/api/3.0/oauth2/token", headers=headers, data=data).text
        accessToken = json.loads(req)
        self.accessToken = accessToken['access_token']
        return self.accessToken
    def get_organizations(self):
        req = requests.get("https://app.action1.com/api/3.0/organizations", headers = {"Authorization":"Bearer {}".format(self.accessToken)})
        result = json.loads(req.text)
        self.organizationId = result['items'][0]['id']
        self.organizationName = result['items'][0]['name']
        return result
    def endpoints(self):
        req = requests.get("https://app.action1.com/api/3.0/endpoints/managed/{}?fields=*".format(self.organizationId), headers = {"Authorization":"Bearer {}".format(self.accessToken)})
        result = json.loads(req.text)
        return result


    def packages(self):
        req = requests.get("https://app.action1.com/api/3.0/packages/all", headers = {"Authorization":"Bearer {}".format(self.accessToken)})
        result = json.loads(req.text)
        return result
    def updates(self, filter=None):
        if filter == None:
            req = requests.get("https://app.action1.com/api/3.0/updates/all", headers={"Authorization":"Bearer {}".format(self.accessToken)})
            result = json.loads(req.text)
            return result
        elif filter == 'Important' or '	Unspecified':
            req = requests.get("https://app.action1.com/api/3.0/updates/all?security_severity={}".format(filter), headers={"Authorization":"Bearer {}".format(self.accessToken)})
            result = json.loads(req.text)
            return result
        else:
            print("Not a listed filter")
