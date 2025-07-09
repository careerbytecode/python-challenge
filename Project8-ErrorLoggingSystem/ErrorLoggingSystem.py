import logging

logging.basicConfig(
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
    level=logging.ERROR,
    filename="age_verification_errors.log"
)



while True:
    try:
        user_name = input(f"Enter your name: ")
        user_age = int(input(f"Enter your age: "))

        if user_age > 18:
            print(f"Your eligible for registration {user_name}")
        else:
            print(f"Your not eligible {user_name}")
            break

    except Exception as e:
        logging.error("User entered a wrong format")
        print("Please enter a valid number.")
