import requests
from cachetools import TTLCache, cached

user_cache = TTLCache(maxsize=100, ttl=20)

@cached(user_cache)
def get_user_info(user_id):
    print(f"Fetching data for user {user_id} from API...")
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    return response.json()

if __name__ == "__main__":
    print(get_user_info(1))  # Fetches from API
    print(get_user_info(1))  # Uses cache (if within 20 seconds)
    print(get_user_info(2))  # Fetches new user
