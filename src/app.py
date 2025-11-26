from reminders import Reminder
from storage import Storage


def show_menu():
    print("\n==== Health Reminder App ====")
    print("1. Add reminder")
    print("2. View reminders")
    print("3. Delete reminder")
    print("4. Exit")
    return input("Choose an option: ")


def main():
    storage = Storage()
    reminders_data = storage.load()

    while True:
        choice = show_menu()

        if choice == "1":
            title = input("Enter reminder title: ")
            time_str = input("Enter time (HH:MM): ")

            reminder = Reminder(title, time_str)

            reminders_data.append({
                "title": title,
                "time": time_str,
                "repeat": reminder.repeat
            })

            storage.save(reminders_data)
            print("\n✔ Reminder added successfully!")

        elif choice == "2":
            print("\n=== Current reminders ===")
            if not reminders_data:
                print("No reminders yet.")
            else:
                for i, r in enumerate(reminders_data):
                    print(
                        f"{i + 1}. {r['title']} at {r['time']} "
                        f"({r['repeat']})")

        elif choice == "3":
            print("\n=== Delete a reminder ===")
            if not reminders_data:
                print("There are no reminders to delete.")
                continue

            index_str = input("Enter the number of the reminder to delete: ")
            if not index_str.isdigit():
                print("Invalid input. Please enter a number.")
                continue

            idx = int(index_str) - 1

            if 0 <= idx < len(reminders_data):
                removed = reminders_data.pop(idx)
                storage.save(reminders_data)
                print(f"✔ Deleted reminder: {removed['title']}")
            else:
                print("❌ Invalid index!")

        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("❌ Invalid option, please try again.")


if __name__ == "__main__":
    main()
