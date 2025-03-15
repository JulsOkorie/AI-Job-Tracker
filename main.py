from app.tracker import JobTracker

def main():
    tracker = JobTracker()
    
    while True:
        print("\n-- AI JOB TRACKER ---")
        print("1. Add a job application")
        print("2. View all applications")
        print("3. Exit")
        print("\n")
        choice = input("Enter your choice: ")
        print("\n")

        if choice == "1":
            company = input("Enter company name: ")
            role = input("Enter job role applied for: ")
            date_applied = input("Enter date applied (YYYY-MM-DD): ")
            tracker.add_application(company, role, date_applied)
            print("Application successfully added!")
            print("\n")

        elif choice == "2":
            applications = tracker.list_applications()
            if applications:
                print("\nYour Tracked Applications:")
                for i, app in enumerate(applications, start=1):
                    print(f"{i}. {app['company']} - {app['role']}n(Applied on: {app['date_applied']}")
                    print("\n")
            else:
                print("No applications tracked yet.")
                print("\n")

        elif choice == "3":
            print("Exiting AI Job Tracker. Goodbye!")
            print("\n")
            break

        else:
            print("Invalid choice. Please try again.")
            print("\n")


if __name__ == "__main__":
    main()