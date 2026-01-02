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
                    password = line.strip().lower()
                    if password:  #Skips empty lines..
                        common_passwords.add(password)
            print(f"✓ Loaded {len(common_passwords)} common passwords")
        except FileNotFoundError:
            print("⚠ Warning: common_passwords.txt file not found. Common password check will be skipped.")
        except Exception as e:
            print(f"⚠ Warning: Error loading common passwords: {e}")

        return common_passwords

