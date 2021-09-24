import requests

class APIComm:
    def __init__(self, base_url, x_auth_token):
        self.base_url = base_url
        self.x_auth_token = x_auth_token
        self.auth_key = 0

    def Start(self, problem_):
        self.header = {'X-Auth-Token': self.x_auth_token}
        self.parameter = {'problem': problem_}
        self.res = requests.post(self.base_url + '/start', headers=self.header, params=self.parameter)
        self.res_json = self.res.json()
        self.auth_key = self.res_json['auth_key']
        return self.res

    def Locations(self):
        self.header = {'Authorization': self.auth_key}
        self.parameter = {}
        self.res = requests.get(self.base_url + '/locations', headers=self.header, params=self.parameter)
        return self.res

    def Trucks(self):
        self.header = {'Authorization': self.auth_key}
        self.parameter = {}
        self.res = requests.get(self.base_url + '/trucks', headers=self.header, params=self.parameter)
        return self.res

    def Simulate(self, commands):
        self.header = {'Authorization': self.auth_key}
        self.parameter = {commands}
        self.res = requests.get(self.base_url + '/simulate', headers=self.header, params=self.parameter)
        return self.res

    def Score(self):
        self.header = {'Authorization': self.auth_key}
        self.parameter = {}
        self.res = requests.get(self.base_url + '/score', headers=self.header, params=self.parameter)
        return self.res

base_url = "https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users"
x_auth_token = "dbe8808fe6b71e44ca5697496b607583"

comm = APIComm(base_url, x_auth_token)
res = comm.Start(1)
res_json = res.json()
print(res_json)


idx = 1
board = [[0] * 5 for _ in range(5)]
for j in range(5):
    for i in range(4, -1, -1):
        board[i][j] = idx
        idx += 1

print(board)
