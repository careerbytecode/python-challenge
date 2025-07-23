import bcrypt
import argparse

def hash_password(password: str, rounds: int = 12) -> bytes:
    salt = bcrypt.gensalt(rounds)
    return bcrypt.hashpw(password.encode('utf-8'), salt)

def check_password(password: str, hashed: bytes) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

def main():
    parser = argparse.ArgumentParser(description="Secure password hashing and verification")
    parser.add_argument("password", help="Password to hash or verify")
    parser.add_argument("--verify", help="Hashed password to verify against (in utf-8)", default=None)
    parser.add_argument("--rounds", type=int, help="Salt rounds for hashing (default: 12)", default=12)
    args = parser.parse_args()

    if args.verify:
        hashed_bytes = args.verify.encode('utf-8')
        is_match = check_password(args.password, hashed_bytes)
        print(f"Password Match: {is_match}")
    else:
        hashed = hash_password(args.password, args.rounds)
        print(f"Hashed Password: {hashed.decode('utf-8')}")

if __name__ == "__main__":
    main()

