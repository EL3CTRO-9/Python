def password_input():
    while True:
        user_input = input("Enter New Password: ")
        new_list = [char for char in user_input]
        if len(new_list) > 12 and any(char.isdigit() for char in new_list) and any(char in ["#", "$", "%", "@", "!", "*", "&"] for char in new_list):
            return new_list
        else:
            print("|| Password not secure enough || Should contain numbers || Should contain special digits ||")

def main():
    password = password_input()
    print("Password is secure enough")

main()
