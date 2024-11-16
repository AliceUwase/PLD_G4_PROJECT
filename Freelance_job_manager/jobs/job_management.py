class JobManager:
    def __init__(self, client_manager):
        self.client_manager = client_manager
        self.jobs = []

    def add_job(self, job_name, client_name, rate, hours):
        job = {"job_name": job_name, "client_name": client_name, "rate": rate, "hours": hours}
        self.jobs.append(job)
        print(f"Job '{job_name}' added for client '{client_name}'.")

    def list_jobs(self):
        if not self.jobs:
            print("No jobs available.")
            return
        for idx, job in enumerate(self.jobs, 1):
            print(f"{idx}. {job['job_name']} for {job['client_name']} - {job['hours']} hours at ${job['rate']} per hour")

    def run_menu(self):
        while True:
            print("\nJob Management Menu")
            print("1. Add Job")
            print("2. List Jobs")
            print("3. Back to Main Menu")
            choice = input("Enter your choice (1-3): ")

            if choice == '1':
                job_name = input("Enter job name: ")
                client_name = input("Enter client name: ")
                rate = float(input("Enter hourly rate: "))
                hours = float(input("Enter hours worked: "))
                self.add_job(job_name, client_name, rate, hours)
            elif choice == '2':
                self.list_jobs()
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")
