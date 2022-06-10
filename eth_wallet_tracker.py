from requests import get
from matplotlib import pyplot as plt
from datetime import datetime

API_KEY = "HD8T9DFW919M41VM3GW7UJSKT25X91P2T3"
address = "0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae"
BASE_URL = "https://api.etherscan.io/api"
ETHER_VALUE = 10 ** 18

def make_api_url(module, action, address, **kwargs):
    url = BASE_URL + f"?module={module}&action={action}&address={address}&apikey={API_KEY}"

    for key, value in kwargs.items():
        url += f"&{key}={value}"
    return url

def get_account_balance(address):
    get_balance_url = make_api_url("account","balance", address, tag="latest")
    response = get(get_balance_url)
    data = response.json()
    value = int(data["result"]) / ETHER_VALUE
    return value

def get_transactions(address):
    get_transactions_url = make_api_url("account", "txlist", address, startblock=0, endblock=99999999, page=1, offset=10000, sort="asc")
    response = get(get_transactions_url)
    data = response.json()["result"]

    for tx in data:
        to = tx["to"]
        from_address = tx["from"]
        value = int(tx["value"]) / ETHER_VALUE
        gas = int(tx["gasUsed"]) * int(tx["gasPrice"]) / ETHER_VALUE
        time = datetime.fromtimestamp(int(tx["timeStamp"]))
        print("--------------------")
        print("To: ", to)
        print("From: ", from_address)
        print("Value: ", value)
        print("Gas Cost: ", gas)
        print("Time: ", time)

eth = get_account_balance(address)
print(eth)

trans = get_transactions(address)
print(trans)