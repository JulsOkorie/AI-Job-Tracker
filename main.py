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
        print("3. Search for applications")
        print("4. Sort applications by date")
        print("5. Exit")
        print("6. Export applications to CSV")

        choice = input("Enter your choice: ")

        if choice == "1":
            while True:
                company = input("Enter company name: ").strip()
                role = input("Enter job role applied for: ").strip()
                date_applied = get_valid_date()

                added = tracker.add_application(company, role, date_applied)
                if added:
                    print("✅ Application successfully added!")

                another = input("Do you want to add another application? (yes/no): ").strip().lower()
                if another != "yes":
                    break

        elif choice == "2":
            applications = tracker.list_applications()
            if applications:
                print("\nYour Tracked Applications:")
                for i, app in enumerate(applications, start=1):
                    print(f"{i}. {app['company'].title()} - {app['role'].title()} (Applied on: {app['date_applied']})")

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
            print("\n🔍 Search Job Applications")
            print("1. Search by company")
            print("2. Search by role")
            print("3. Search by date applied")
            print("4. Back to main menu")
            search_choice = input("Enter your search option: ")

            if search_choice == "1":
                company_name = input("Enter company name to search: ").strip()
                results = tracker.search_by_company(company_name)

            elif search_choice == "2":
                job_role = input("Enter job role to search: ").strip()
                results = tracker.search_by_role(job_role)

            elif search_choice == "3":
                date_applied = get_valid_date()
                results = tracker.search_by_date(date_applied)

            else:
                continue

            if results:
                print("\n🔎 Search Results:")
                for i, app in enumerate(results, start=1):
                    print(f"{i}. {app['company'].title()} - {app['role'].title()} (Applied on: {app['date_applied']})")

            else:
                print("⚠️ No matching applications found.")

        elif choice == "4":
            if tracker.applications:
                sort_order = input("Sort by (1) Oldest to Newest or (2) Newest to Oldest? ").strip()
                sorted_apps = tracker.sort_by_date(ascending=(sort_order == "1"))
                print("\n📅 Sorted Applications:")

                for i, app in enumerate(sorted_apps, start=1):
                    print(f"{i}. {app['company'].title()} - {app['role'].title()} (Applied on: {app['date_applied']})")

            else:
                print("⚠️ No applications to sort.")

        elif choice == "5":
            print("Exiting AI Job Tracker. Goodbye! 👋")
            break

        elif choice == "6":
            tracker.export_to_csv()

        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()