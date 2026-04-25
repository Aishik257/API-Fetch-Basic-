import requests

def fetch_user():
    url = "https://jsonplaceholder.typicode.com/users/1"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        name = data["name"]
        username = data["username"]
        email = data["email"]
        city = data["address"]["city"]

        print("Name:", name)
        print("Username:", username)
        print("Email:", email)
        print("City:", city)

    else:
        print("Error:", response.status_code)

fetch_user()