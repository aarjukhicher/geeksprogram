import requests
import json

r = requests.get("https://test.deribit.com/api/v2/public/get_order_book?depth=5&instrument_name=BTC-PERPETUAL")
print(r)
print(r.status_code)
print(r.text)
print()
print(r.ok)
print(r.headers)
print()
print()
r_dict = r.json()
print(r_dict)
print()
print()
print(r_dict["jsonrpc"])
# print(r_deribit.status_code)
# print(type(r_deribit))
# print(r_deribit.text)
# data = json.loads(r_deribit)
# print(type(data))
# r_dict_deribit = r_deribit.json()
# print(r_dict_deribit)
# deribit_json = json.dumps(r_dict_deribit, indent = 2)
# print(deribit_json)
