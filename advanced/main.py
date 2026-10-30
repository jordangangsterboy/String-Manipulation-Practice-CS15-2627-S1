def main():
    while True:
        print("\nChoose how you want to process a string:")
        print("1. Format a Name")
        print("2. Format a Title")
        print("3. Format a List")
        print("4. Process Numbers")

        choice = input("\nEnter your choice (1-4): ").strip()
        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice, enter a number between 1 and 4.")
            continue

        user_input = input("Enter the string to process: ")

        try:
            if choice == "1":
                names = user_input.strip().split()
                if len(names) < 2:
                    raise ValueError("Enter both a first and last name.")
                formatted_name = " ".join([n.capitalize() for n in names])
                print(f"\nProcessed String:\n{formatted_name}")
                break
            elif choice == "2":
                no_spaces = user_input.replace(" ", "")
                no_commas = no_spaces.replace(",", " ")
                clean_text = no_commas.replace("::", " ")
                formatted_title = clean_text.title()
                print(f"\nProcessed String:\n{formatted_title}")
                break
            elif choice == "3":
                clean_list_string = user_input.strip()
                formatted_list = clean_list_string.replace(",", " | ").upper()
                print(f"\nProcessed String:\n{formatted_list}")
                break
            elif choice == "4":
                clean_string = user_input.strip()
                numbers = [int(num) for num in clean_string.split(",")]
                total = sum(numbers)
                average = total / len(numbers)
                print(f"\nTotal: {total}")
                print(f"Average: {average}")
                break

        except ValueError as error:
            print(f"Error: {error}. Try again.")
        except ZeroDivisionError:
            print("Error: No numbers were given to calculate an average. Try again.")

if __name__ == "__main__":
    main()