import json

try:
    with open('data.json', 'r') as file:
        user_data = json.load(file)
except FileNotFoundError:
    user_data = {}


def save_data():
    with open('data.json', 'w') as file:
        json.dump(user_data, file, indent=4)

def sign_up():
    user_name = input("Enter user_name: ")
    if user_name in user_data:
        print("user_name exists! Try different user_name.")
        return
    password = input("Enter Password: ")
    phone_number = input("Enter Mobile Number: ")
    user_data[user_name] = {
        'password': password,
        'phone_number': phone_number
    }
    save_data()
    print("Sign up successful!")

def sign_in():
    user_name = input("Enter user_name: ")
    password = input("Enter Password: ")
    if user_name in user_data and user_data[user_name]['password'] == password:
        print(f"Welcome to the device. Your phone number is {user_data[user_name]['phone_number']}.")
    else:
        print("Incorrect credentials!")

def main():
    print("1. Sign Up")
    print("2. Sign In")
    choice = input("Enter your choice (1 or 2): ")
    if choice == '1':
        sign_up()
    elif choice == '2':
        sign_in()
    else:
        print("Invalid choice! Please enter 1 or 2.")

if __name__ == "__main__":
    main()
