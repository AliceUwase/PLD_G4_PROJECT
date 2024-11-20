from db.db import cursor, conn

class JobManager:
    def __init__(self, client_manager):
        self.client_manager = client_manager

    def add_job(self, job_name, client_name, rate, hours):
        query = """
        INSERT INTO jobs (job_name, client_name, rate, hours)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (job_name, client_name, rate, hours))
        conn.commit()
        print(f"Job '{job_name}' added for client '{client_name}'.")

    def list_jobs(self):
        cursor.execute("SELECT * FROM jobs")
        jobs = cursor.fetchall()
        
        if not jobs:
            print("No jobs available.")
            return
            
        for job in jobs:
            print(f"ID: {job[0]} - {job[1]} for {job[2]} - {job[4]} hours at ${job[3]} per hour")

    def update_job(self, job_id):
        # Check if job exists
        cursor.execute("SELECT * FROM jobs WHERE job_id = %s", (job_id,))
        job = cursor.fetchone()
        if not job:
            print("Invalid job ID.")
            return

        print(f"\nUpdating Job: {job[1]}")
        print("Leave blank to keep current value")

        new_name = input(f"Enter new job name ({job[1]}): ")
        new_client = input(f"Enter new client name ({job[2]}): ")
        new_rate = input(f"Enter new rate (${job[3]}): ")
        new_hours = input(f"Enter new hours ({job[4]}): ")

        updates = []
        values = []
        if new_name:
            updates.append("job_name = %s")
            values.append(new_name)
        if new_client:
            updates.append("client_name = %s")
            values.append(new_client)
        if new_rate:
            updates.append("rate = %s")
            values.append(float(new_rate))
        if new_hours:
            updates.append("hours = %s")
            values.append(float(new_hours))

        if updates:
            query = f"UPDATE jobs SET {', '.join(updates)} WHERE job_id = %s"
            values.append(job_id)
            cursor.execute(query, tuple(values))
            conn.commit()
            print("Job updated successfully!")

    def delete_job(self, job_id):
        cursor.execute("SELECT job_name, client_name FROM jobs WHERE job_id = %s", (job_id,))
        job = cursor.fetchone()
        if not job:
            print("Invalid job ID. Delete failed.")
            return

        cursor.execute("DELETE FROM jobs WHERE job_id = %s", (job_id,))
        conn.commit()
        print(f"Job '{job[0]}' for client '{job[1]}' deleted successfully.")

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
                # Check if jobs exist by querying the database
                cursor.execute("SELECT EXISTS(SELECT 1 FROM jobs)")
                jobs_exist = cursor.fetchone()[0]
                if not jobs_exist:
                    print("No jobs available to update.")
                    continue
                self.list_jobs()
                job_id = int(input("Enter the job ID to update: "))
                self.update_job(job_id)

            elif choice == '4':
                # Check if jobs exist by querying the database
                cursor.execute("SELECT EXISTS(SELECT 1 FROM jobs)")
                jobs_exist = cursor.fetchone()[0]
                if not jobs_exist:
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