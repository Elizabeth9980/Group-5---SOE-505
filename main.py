import hashlib

def login_system():
    # Simple logic for Exercise A
    user = input("Enter Role (Staff/Student): ")
    password = "password123" # This is a "Hardcoded Secret" - SonarQube will catch this!
    
    # Hashing the password (Secure practice)
    hashed = hashlib.sha256(password.encode()).hexdigest()
    
    if user == "Staff":
        print("Welcome, Staff. Accessing Secure Records...")
    else:
        print("Welcome, Student. Accessing Library...")

if __name__ == "__main__":
    login_system()
