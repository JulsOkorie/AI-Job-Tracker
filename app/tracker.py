import json
import os


class JobTracker:
    def __init__(self):
        self.filename = "applications.json"
        self.applications = self.load_applications()

    def add_application(self, company, role, date_applied):
        self.applications.append({
            "company": company,
            "role": role,
            "date_applied": date_applied
        })
        self.save_applications()

    def list_applications(self):
        return self.applications

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
