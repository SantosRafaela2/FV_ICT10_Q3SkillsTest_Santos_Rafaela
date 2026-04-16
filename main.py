def is_title_case(name):
    words = name.replace(",", "").split()

    for i in range(len(words)):
        if words[i][0].islower():
            return False

    return True


print("SIGN UP SYSTEM")

name = input("Full Name: ")
username = input("Username: ")
password = input("Password: ")

# CHECK NAME
if not is_title_case(name):
    print("❌ Name must be Title Case.")
else:
    # CHECK USERNAME
    if len(username) < 7:
        print("❌ Username must be at least 7 characters.")
    else:
        # CHECK PASSWORD
        has_letter = False
        has_number = False

        for i in range(len(password)):
            if password[i].isalpha():
                has_letter = True
            if password[i].isdigit():
                has_number = True

        if len(password) < 10 or not has_letter or not has_number:
            print("❌ Password must be 10+ chars with letters & numbers.")
        else:
            print("✅ Account created successfully!")





