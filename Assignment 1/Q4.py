# Simple password system with 3 attempts

correct_password = "admin123"
attempts = 3

for i in range(attempts):
    password = input("Enter password: ")
    if password == correct_password:
        print("Access Granted")
        break
else:
    print("Access Denied")