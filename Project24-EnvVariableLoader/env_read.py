import os

def load_config():
    api_key = os.environ.get("API_KEY")
    db_password = os.environ.get("DB_PASSWORD")

    if not api_key or not db_password:
        print("Missing environment variables!")
        return

    print("Configuration loaded successfully.")
    print(f"API Key: {api_key}")
    print(f"Database Password: {db_password}")

if __name__ == "__main__":
    load_config()

