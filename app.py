import http.client

conn = http.client.HTTPSConnection("api.themoviedb.org")

payload = "{}"

conn.request("GET", "/3/configuration?api_key=12217434ad2932f49fc3abd52e259e8a", payload)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
