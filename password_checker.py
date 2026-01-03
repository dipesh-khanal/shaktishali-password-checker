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
            file_path = os.path.join(script_dir, 'data', 'common_passwords.txt')

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
    


    def check_sequential_characters(self, password):
        # 6th check: Whether there are sequential characters in password or not...
        # The argument is password(str) which is simply the password we're checking.
        # It returns tuple: (bool, str) - (is_valid, message).

        password_lower = password.lower()

        # Check for sequential characters
        for i in range(len(password) - 2):

            # First in ascending format
            if (ord(password_lower[i+1]) == ord(password_lower[i]) + 1 and ord(password_lower[i+2]) == ord(password_lower[i]) + 2):
                return False, f"✗ Contains sequential characters"
            
            # Now in descending format
            if (ord(password_lower[i+1]) == ord(password_lower[i]) - 1 and ord(password_lower[i+2]) == ord(password_lower[i]) - 2):
                return False, f"✗ Contains sequential characters"
            
        return True, "✓ No sequential characters found."
    


    def check_common_password(self, password):
        # 7th check: Whether the password is common or not...
        # The argument is password(str) which is simply the password we're checking.
        # It returns tuple: (bool, str) - (is_valid, message).

        if not self.common_passwords:
            return True, "Common password check skipped (no file)"
        if password.lower() in self.common_passwords:
            return False, "✗ This is a commonly used password (not secure)"   
        else:
            return True, "✓ Not a common password" 



    def check_repeated_characters(self, password):
        # 8th check: Whether there are characters repeated consecutively more than twice in password or not...
        # The argument is password(str) which is simply the password we're checking.
        # It returns tuple: (bool, str) - (is_valid, message).

        # Check for pattern (3 or more repeated characters)
        pattern = r'(.)\1{2,3}'
        match = re.search(pattern, password)

        if match:
            repeated_char = match.group(0)
            return False, f"✗ Contains repeated characters: ('{repeated_char}')"
        else:
            return True, "✓ No repeated characters"
    


    def calculate_score(self, password):
        # THis calculates overall score for password strentgh (0-100)
        # The argument is password(str) which is simply the password we're checking.
        # It returns int which is the score (0-100).

        score = 0

        # Score from length (max 20 points)
        length = len(password)
        if length >= 20:
            score += 20
        elif length >= 16:
            score += 15
        elif length >= 12:
            score += 10
        elif length >= 8:
            score += 5
        
        # Score from password's diversity (max 30 points)
        if self.check_uppercase(password)[0]:
            score += 8
        if self.check_lowercase(password)[0]:
            score += 8
        if self.check_numbers(password)[0]:
            score += 7
        if self.check_special_characters(password)[0]:
            score += 7
        
        # Score from security check (max 50 points)
        if self.check_common_password(password)[0]:
            score += 15
        if self.check_sequential_characters(password)[0]:
            score += 10
        if self.check_repeated_characters(password)[0]:
            score += 10
        

        # Bonus
        # If all 4 character types exist
        has_all_types = (
            self.check_uppercase(password)[0] and
            self.check_lowercase(password)[0] and
            self.check_numbers(password)[0] and
            self.check_special_characters(password)[0]
        )
        if has_all_types:
            score += 10
        

        # Bonus for extra length
        if length > 20:
            score += 5
        
        return min(score, 100)     # To limit max score to 100
    


    def get_strength_label(self, score):
        # This gives a strength label based on score.
        # The argument is score(int) which is the score (0-100).
        # It returns str which is the strength label.

        if score >= 86:
            return "Very Strong"
        elif score >= 71:
            return "Strong"
        elif score >= 51:
            return "Moderate"
        elif score >= 26:
            return "Weak"
        else:
            return "Very Weak"
    


    def check_password(self, password):
        # This is the main function to check the password against all criteria.
        # The argument is password(str) which is simply the password we're checking.
        # It returns dict which contains overall results and details.

        if not password:
            return {
                'score': 0,
                'strength': 'Very Weak',
                'results': [(False, "✗ Password cannot be empty.")]
            }
    

        # Running all checks here
        results = [
            self.check_length(password),
            self.check_uppercase(password),
            self.check_lowercase(password),
            self.check_numbers(password),
            self.check_special_characters(password),
            self.check_common_password(password),
            self.check_sequential_characters(password),
            self.check_repeated_characters(password)
        ]

        # Calculates score here
        score = self.calculate_score(password)
        strength = self.get_strength_label(score)

        return {
            'score': score,
            'strength': strength,
            'results': results,
            'passed': sum(1 for r in results if r[0]),
            'total': len(results)
        }
    

    
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
