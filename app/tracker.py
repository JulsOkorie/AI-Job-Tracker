import json
import shutil
import os
import csv
from datetime import datetime


class JobTracker:
    def __init__(self):
        self.filename = "data/applications.json"
        self.backup_filename = "data/applications_backup.json"
        self.applications = self.load_applications()


    def export_to_csv(self, filename="exported_applications.csv"):
        if not self.applications:
            print("⚠️ No applications to export.")
            return

        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["company", "role", "date_applied"])
            writer.writeheader()
            for app in self.applications:
                # 👇🏽 Only write relevant fields (exclude 'timestamp')
                writer.writerow({
                    "company": app["company"],
                    "role": app["role"],
                    "date_applied": app["date_applied"]
                })

        print(f"✅ Applications exported successfully to '{filename}'")


    def add_application(self, company, role, date_applied):
        for app in self.applications:
            if (app["company"] == company.lower() and app["role"] == role.lower() and
                    app["date_applied"] == date_applied):
                print("⚠️ Duplicate application detected! This entry already exists.")
                return False

        self.applications.append({
            "company": company.strip(),
            "role": role.strip(),
            "date_applied": date_applied,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        self.save_applications()
        return True

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
            file.flush()
            os.fsync(file.fileno())

        self.backup_applications()

    def backup_applications(self):
        shutil.copy(self.filename, self.backup_filename)

    def load_applications(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                return json.load(file)
        return []

    def sort_by_date(self, ascending=True):
        return sorted(self.applications, key=lambda app: app["date_applied"], reverse=not ascending)


def track_applications():
    print("Tracking job applications...(feature coming soon!)")
#  return self.track_applications()
