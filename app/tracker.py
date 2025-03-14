class JobTracker:
    def __init__(self):
        self.applications = []


    def add_application(self, company, role, date_applied):
        self.applications.append({
            "company": company,
            "role": role,
            "date_applied": date_applied
        })


    def list_applications(self):
        return self.applications