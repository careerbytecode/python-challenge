import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def get(endpoint):
    url = f"{BASE_URL}/{endpoint.lstrip('/')}"
    response = requests.get(url)
    return response.json()

def post(endpoint, data):
    url = f"{BASE_URL}/{endpoint.lstrip('/')}"
    response = requests.post(url, json=data)
    return response.json()

def put(endpoint, data):
    url = f"{BASE_URL}/{endpoint.lstrip('/')}"
    response = requests.put(url, json=data)
    return response.json()

def delete(endpoint):
    url = f"{BASE_URL}/{endpoint.lstrip('/')}"
    response = requests.delete(url)
    return response.status_code


if __name__ == "__main__":
    users = get("users")
    print("Users:", users)

    new_post = post("posts", {"title": "foo", "body": "bar", "userId": 1})
    print("New Post:", new_post)

    updated_post = put("posts/1", {"id": 1, "title": "updated", "body": "baz", "userId": 1})
    print("Updated Post:", updated_post)

    delete_status = delete("posts/1")
    print("Delete Status:", delete_status)
