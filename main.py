import hashlib

def login_system():
    print("--- University Portal Login ---")
    user_role = input("Enter Role (Staff/Student): ")
    user_input_pw = input("Enter Password: ")

    hashed_input = hashlib.sha256(user_input_pw.encode()).hexdigest()
    
    if user_role == "Staff":
        print("Welcome, Staff. Accessing Secure Records...")
    elif user_role == "Student":
        print("Welcome, Student. Accessing Library...")
    else:
        print("Access Denied.")

if __name__ == "__main__":
    login_system()
