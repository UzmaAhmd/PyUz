import requests
baseurl= "https://rickandmortyapi.com/api/"
endpoint= "character"
r=requests.get (baseurl + endpoint)


# print(r)

# if r.status_code == 200:  # Ensure the request was successful
#     data = r.json()
#     print(data)
# else:
#     print(f"Error: {r.status_code}")

data=r.json()

pages=(data['info']['pages'])

print(data)
print(pages)

name=(data['results'][0]['name'])
episodes=(data['results'][0]['episode'])
print(name)
print(len(episodes))