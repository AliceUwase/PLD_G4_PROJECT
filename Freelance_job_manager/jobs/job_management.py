class JobManager:
    def __init__(self, client_manager):
        self.client_manager = client_manager
        self.jobs = []
        self._next_id = 1  # Add counter for unique IDs
        
    def add_job(self, job_name, client_name, rate, hours):
        # Method to add a new job
        job = {
            "id": self._next_id,
            "job_name": job_name, 
            "client_name": client_name, 
            "rate": rate, 
            "hours": hours
        }
        self._next_id += 1
        self.jobs.append(job)
        print(f"Job '{job_name}' added for client '{client_name}'.")

    def list_jobs(self):
        # Method to display all stored jobs
        if not self.jobs:
            print("No jobs available.")
            return
        for job in self.jobs:
            # Prints detailed information for each job
            print(f"ID: {job['id']} - {job['job_name']} for {job['client_name']} - {job['hours']} hours at ${job['rate']} per hour")

    def get_job_by_id(self, job_id):
        # Helper method to find job by ID
        for index, job in enumerate(self.jobs):
            if job['id'] == job_id:
                return index, job
        return None, None

    def update_job(self, job_id):
        # Update an existing job's details
        index, job = self.get_job_by_id(job_id)
        if job is None:
            print("Invalid job ID.")
            return

        print(f"\nUpdating Job: {job['job_name']}")
        print("Leave blank to keep current value")

        # Get new values or keep current ones if input is blank
        new_name = input(f"Enter new job name ({job['job_name']}): ")
        new_client = input(f"Enter new client name ({job['client_name']}): ")
        new_rate = input(f"Enter new rate (${job['rate']}): ")
        new_hours = input(f"Enter new hours ({job['hours']}): ")

        # Update only if new value provided
        if new_name:
            job['job_name'] = new_name
        if new_client:
            job['client_name'] = new_client
        if new_rate:
            job['rate'] = float(new_rate)
        if new_hours:
            job['hours'] = float(new_hours)

        print("Job updated successfully!")    

    def delete_job(self, job_id):
        # Method to delete a job
        index, job = self.get_job_by_id(job_id)
        if job is not None:
            removed_job = self.jobs.pop(index)
            print(f"Job '{removed_job['job_name']}' for client '{removed_job['client_name']}' deleted successfully.")
        else:
            print("Invalid job ID. Delete failed.")

    def run_menu(self):
        # Method to provide an interactive menu for job management
        while True:
            print("\nJob Management Menu")
            print("1. Add Job")
            print("2. List Jobs")
            print("3. Update Job")
            print("4. Delete Job")
            print("5. Back to Main Menu") 


            # Prompts user for choice
            choice = input("Enter your choice (1-5): ")

            if choice == '1':

                job_name = input("Enter job name: ")
                client_name = input("Enter client name: ")
                rate = float(input("Enter hourly rate: "))
                hours = float(input("Enter hours worked: "))
                self.add_job(job_name, client_name, rate, hours)

            elif choice == '2':
                self.list_jobs()

            elif choice == '3':
                if not self.jobs:
                    print("No jobs available to update.")
                    continue
                self.list_jobs()
                job_id = int(input("Enter the job ID to update: "))
                self.update_job(job_id)
            elif choice == '4':
                if not self.jobs:
                    print("No jobs available to delete.")
                    continue
                self.list_jobs()
                job_id = int(input("Enter the job ID to delete: "))
                self.delete_job(job_id)
            elif choice == '5':
                print("Exiting Job Management Menu.")
                break
            else:
                print("Invalid choice. Please try again.")