import json
import os


class JobTracker:
    def __init__(self):
        self.filename = "applications.json"
        self.applications = self.load_applications()

    def add_application(self, company, role, date_applied):
        for app in self.applications:
            if (app["company"] == company.lower() and app["role"] == role.lower() and
                    app["date_applied"] == date_applied):
                print("⚠️ Duplicate application detected! This entry already exists.")
                return

        self.applications.append({
            "company": company.lower(),
            "role": role.lower(),
            "date_applied": date_applied
        })
        self.save_applications()

    def list_applications(self):
        if not self.applications:
            return []

        print(f"\n📌 You have {len(self.applications)} tracked applications.\n")
        return self.applications

    def search_by_company(self, company_name):
        return [app for app in self.applications if
                   company_name.lower() in app["company"].lower()]

    def search_by_role(self, job_role):
        return [app for app in self.applications if
                   job_role.lower() in app["role"].lower()]

    def search_by_date(self, date_applied):
        return [app for app in self.applications if app["date_applied"] == date_applied]


    def search_application(self, role):
        matches = [app for app in self.applications if role.lower() in app['role'].lower()]
        if matches:
            for app in matches:
                print(f"Company: {app['company']}, Role: {app['role']}, Date Applied: {app['date_applied']}")

        else:
            print("⚠️ No matching applications found.")

    def save_applications(self):
        with open(self.filename, "w") as file:
            json.dump(self.applications, file, indent=4)

    def load_applications(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                return json.load(file)
        return []

    

def track_applications():
    print("Tracking job applications...(feature coming soon!)")
#  return self.track_applications()
