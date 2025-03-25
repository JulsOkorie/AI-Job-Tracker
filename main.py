from app.tracker import JobTracker
import datetime


def  get_valid_date():

    today = datetime.date.today()

    while True:
        date_str = input("Enter date applied (YYYY-MM-DD): ")
        try:
            date_applied = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()

            if date_applied > today:
                print("❌ You cannot enter a future date. Please enter today’s date or a past date.")
            else:
                return date_str  # If valid, return the formatted date

        except ValueError:
            print("❌ Invalid date! Please enter a real date in YYYY-MM-DD format (e.g., 2024-03-11).")

def main():
    tracker = JobTracker()
    
    while True:
        print("\n-- AI JOB TRACKER ---")
        print("1. Add a job application")
        print("2. View all applications")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            while True:
                company = input("Enter company name: ").strip()
                role = input("Enter job role applied for: ").strip()
                date_applied = get_valid_date()

                tracker.add_application(company, role, date_applied)
                print("✅ Application successfully added!")

                another = input("Do you want to add another application? (yes/no): ").strip().lower()
                if another != "yes":
                    break

        elif choice == "2":
            applications = tracker.list_applications()
            if applications:
                print("\nYour Tracked Applications:")
                for i, app in enumerate(applications, start=1):
                    print(f"{i}. {app['company']} - {app['role']} (Applied on: {app['date_applied']})")
                    print("\n")
            else:
                print("⚠️ No applications tracked yet.")
                while True:
                    action = input("Do you want to (1) Go back to main menu or (2) Exit the program? ").strip()
                    if action == "1":
                        break  # Return to main menu
                    elif action == "2":
                        print("Exiting AI Job Tracker. Goodbye! 👋")
                        return  # Exit program
                    else:
                        print("❌ Invalid choice! Please enter 1 or 2.")

        elif choice == "3":
            print("Exiting AI Job Tracker. Goodbye!")
            print("\n")
            break

        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()