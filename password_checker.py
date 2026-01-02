## Core logic here..

import re
import os

class PasswordChecker:
    # Simple class to check password strength based on certain criteria...

    def __init__(self):
        # This initializes password checker and loads common passwords from attached file..

        self.common_passwords = self.load_common_passwords()
    

    def load_common_passwords(self):
        # This loads the common passwords file into a set which allows faster lookup.
        # Returns set() which would be a set of common passwords in lowercase.

        common_passwords = set()
        try:
            # Get the directory where this script is located

            script_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(script_dir, 'common_passwords.txt')

            with open(file_path, 'r') as file:  # Read mode..
                for line in file:
                    password = line.strip().lower()   # Lowercasing
                    if password:  #Skips empty lines..
                        common_passwords.add(password)
            print(f"✓ Loaded {len(common_passwords)} common passwords")
        except FileNotFoundError:
            print("⚠ Warning: common_passwords.txt file not found. Common password check will be skipped.")
        except Exception as e:
            print(f"⚠ Warning: Error loading common passwords: {e}")

        return common_passwords



    def check_length(self, password):
        # 1st check: The length of password...
        # The argument is password(str) which is simply the password we're checking.
        # It returns tuple: (bool, str) - (is_valid, message).

        min_length = 12
        length = len(password)

        if length >= min_length:
            return True, f"✓ Length: {length} characters (minimum: {min_length})"     # If meets length criteria
        else:
            return False, f"✗ Length: {length} characters (minimum required: {min_length})"    # If doesn't meet length criteria
    


    def check_uppercase(self, password):
        # 2nd check: Whether there are 2 uppercase letters in password or not...
        # The argument is password(str) which is simply the password we're checking.
        # It returns tuple: (bool, str) - (is_valid, message).

        uppercase_count = sum(1 for c in password if c.isupper())
        required = 2

        if uppercase_count >= required:
            return True, f"✓ Uppercase letters: {uppercase_count} (minimum: {required})"   # If meets uppercase criteria
        else:
            return False, f"✗ Uppercase letters: {uppercase_count} (minimum required: {required})"  # If dones't meet uppercase criteria
    


    def check_lowercase(self, password):
        # 3rd check: Whether there are 2 lowercase letters in password or not...
        # The argument is password(str) which is simply the password we're checking.
        # It returns tuple: (bool, str) - (is_valid, message).

        lowercase_count = sum(1 for c in password if c.islower())
        required = 2

        if lowercase_count >= required:
            return True, f"✓ Lowercase letters: {lowercase_count} (minimum: {required})"   # If meets lowercase criteria
        else:
            return False, f"✗ Lowercase letters: {lowercase_count} (minimum required: {required})"  # If doesn't meet lowercase criteria
    


    def check_numbers(self, password):
        # 4th check: Whether there are 2 numbers in password or not...
        # The argument is password(str) which is simply the password we're checking.
        # It returns tuple: (bool, str) - (is_valid, message).

        number_count = sum(1 for c in password if c.isdigit())
        required = 2

        if number_count >= required:
            return True, f"✓ Numbers: {number_count} (minimum: {required})"   # If meets number criteria
        else:
            return False, f"✗ Numbers: {number_count} (minimum required: {required})"  # If doesn't meet number criteria
    


    def check_special_characters(self, password):
        # 5th check: Whether there are 2 special characters in password or not...
        # The argument is password(str) which is simply the password we're checking.
        # It returns tuple: (bool, str) - (is_valid, message).

        special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?/~`"
        special_char_count = sum(1 for c in password if c in special_chars)
        required = 2

        if special_char_count >= required:
            return True, f"✓ Special characters: {special_char_count} (minimum: {required})"   # If meets special character criteria
        else:
            return False, f"✗ Special characters: {special_char_count} (minimum required: {required})"  # If doesn't meet special character criteria
    






def main():
    # Main driver function to test the password checker in console mode.

    print("=" * 60)
    print("Shaktishali Password Checker - Console Version")
    print("=" * 60)
    print()

    # Initializing the password checker
    checker = PasswordChecker()
    print()

    # Loop for user's choice
    while True:
        print("-" * 60)
        password = input("\nEnter the password to check (or type 'quit' to exit): ")

        if password.lower() == 'quit':
            print("\nThank you for your time. Stay secure!")
            break


        # Actual checking if user doens't quit.
        result = checker.check_password(password)

        # Displaying results
        print("\n" + "=" * 60)
        print(f"Strength: {result['strength']} ({result['score']}/100)")
        print(f"Passed: {result['passed']}/{result['total']} checks")
        print("=" * 60)
        print("\nDetailed Results:")
        print("-" * 60)

        for is_valid, message in result['details']:
            print(message)
        
        print("\n" + "=" * 60)

if __name__ == "__main__":
    main()