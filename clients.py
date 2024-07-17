import requests
import json

class OpenDotaClient():
  def __init__(self, id):
    self.id = id
    self.url = "https://api.opendota.com/api/players"
    
  def get_last_match(self):
    link = f"{self.url}/{self.id}/matches?limit=1"
    request = requests.get(link)
    data = json.loads(request.text)[0]
    return data

  def get_account(self):
    link = f"{self.url}/{self.id}"
    request = requests.get(link)
    data = json.loads(request.text)
    return data