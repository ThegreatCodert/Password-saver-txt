for_what =input("For what ? ")
user_name_string = input('What is your username: ')
user_password_string = input('What is your password: ')
conform_password = input('Rewrite the password: ')

def make_file():
    file = open("C:\\Users\\aaran\\Desktop\\Dont delete\\password.txt", "a")
    file.write("Username: ")
    file.write(user_name_string )
    file.write('')
    file.write('  ')
    file.write("Password: ")
    file.write(user_password_string)
    file.write(" ")
    file.write(f"({for_what})""\n")
    file.close()
    file = open("data.txt", "r")
    print(file.read())


if user_password_string == conform_password:
    make_file()
else:
    rewrite = input("Try again: ")
    if rewrite == user_password_string:
        make_file()
    else:
        print("Sorry try later")
        pass
