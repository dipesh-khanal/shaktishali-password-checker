## Entry point.

from password_checker import PasswordChecker

def print_welcome():
    # To display the welcome message to the user..

    print("\n" + "=" * 70)
    print(" " * 20 + "Shaktishali Password Checker")
    print(" " * 16 + "Console Version as of now. GUI later.")
    print("=" * 70)
    print("\nThis tool checks your password strength based on strict security criteria.")
    print("  - Minimum 12 characters")
    print("  - At least 2 uppercase, 2 lowercase, 2 numbers, 2 special characters")
    print("  - Not a common password")
    print("  - No sequential or repeated characters")
    print("\n" + "=" * 70 + "\n")

def print_divider():
    # To display a visual divider line on the screen..

    print("\n" + "-" * 70 + "\n")

def get_strength_color_symbol(strength):
    # To get a visual symbol that indicates password strength..
    # Here the argument is strength(str) which is just a strength label.
    # And it returns str which is its visual representation.

    symbols = {
        "Very Strong": "█████ (Excellent!)",
        "Strong": "████░ (Good)",
        "Moderate": "███░░ (Fair)",
        "Weak": "██░░░ (Poor)",
        "Very Weak": "█░░░░ (Very Poor)"
    }
    return symbols.get(strength, "░░░░░ (Unknown)")

def display_result(result):
    # To display the strength result in a formatted way..
    # Argument is result(dict) which is result dictionary from PasswordChecker.

    try:
        print("\n" + '=' * 70)
        print(" " * 30 + "RESULTS")
        print("=" * 70)


        # Here displaying score and strength
        strength = result.get('strength', 'Unknown')
        score = result.get('score', 0)
        passed = result.get('passed', 0)
        total = result.get('total', 0)


        print(f"\nOverall Strength: {strength}")
        print(f"Score: {score}/100")
        print(f"Visual: {get_strength_color_symbol(strength)}")
        print(f"Checks Passed: {passed}/{total}")

        
        print("\n" + "-" * 70)
        print(" " * 27 + "DETAILED CHECKS:")
        print("-" * 70)


        # Here displaying each check result
        results = result.get('results', [])
        for item in results:
            if isinstance(item, tuple) and len(item) == 2:
                is_valid, message = item
                print(f"  {message}")
            else:
                print(f"  Unexpected result format: {item}")

        
        # Recommendations for weak passwords
        if score < 86:
            print("\n" + "-" * 70)
            print(" " * 14 + "RECOMMENDATIONS TO IMPROVE YOUR PASSWORD:")
            print("-" * 70)

            failed_checks = []
            for item in results:
                if isinstance(item, tuple) and len(item) == 2:
                    valid, msg = item
                    if not valid:
                        failed_checks.append(msg)

            if failed_checks:
                for check in failed_checks:
                    
                    # Extract requirements
                    if "Length" in check:
                        print(" - Increase the length to at least 12 characters.")
                    elif "Uppercase" in check:
                        print(" - Add more uppercase letters (A-Z)")
                    elif "Lowercase" in check:
                        print(" - Add more lowercase letters (a-z)")
                    elif "Numbers" in check:
                        print(" - Add more numbers (0-9)")
                    elif "Special" in check:
                        print(" - Add more special characters (!@#$%^&* etc.)")
                    elif "common" in check:
                        print(" - Avoid common passwords - use a unique combination")
                    elif "sequential" in check:
                        print(" - Avoid sequential patterns (abc, 123, etc.)")
                    elif "repeated" in check:
                        print(" - Avoid repeating the same character multiple times")
            else:
                print(" - Add more length and character variety for maximum security")

        print("\n" + "=" * 70 + "\n")
    
    except Exception as e:
        print(f"\n An error occured displaying results: {e}")
        print(f"Result data: {result}\n")



def main():
    # Main welcome function
    print_welcome()

    # Start the password checker
    print("Initializing Shaktishali Password Checker...")
    try:
        checker = PasswordChecker()
    except Exception as e:
        print(f"\n Error initializing Password Checker: {e}\n")
        return
    print()


    # Main loop for user input
    while True:
        try:
            # Gets user input
            password = input("Enter a password to check (or type 'quit' to exit): ")

            # Check if user wants to quit
            if password.lower() == 'quit':
                print("\n" + "=" * 70)
                print(" " * 20 + "Thanks for using")
                print(" " * 15 + "Shaktishali Password Checker!")
                print("=" * 70 + "\n")
                break

            # Skip empty input
            if not password.strip():
                print("\n Please enter a password to check.\n")
                continue

            # Check password
            result = checker.check_password(password)

            # Display results
            display_result(result)

            # Prompt ready for another check
            print("Ready to check another password...\n")

        except KeyboardInterrupt:
            # In case of interruption with Ctrl+C
            print("\n\n" + "=" * 70)
            print(" " * 20 + "Session interrupted.")
            print(" " * 15 + "Thanks for using Shaktishali Password Checker!")
            print("=" * 70 + "\n")
            break

        except Exception as e:
            # If any unexpected error
            print(f"\n An error occured: {e}")
            print("Please try again.\n")

if __name__ == "__main__":
    main()
