import json
import requests

with open("map.json", "r") as fp:
	data = json.load(fp)
	for k, v in data.items():
		url = f"https://atmgateway-client.alibaba.com/smily-big/smile_{v['id']}.png"
		r = requests.get(url)
		with open(f"emojis/{v['t']}.png", "wb") as png:
			png.write(r.content)
