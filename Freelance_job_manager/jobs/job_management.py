from db.db import cursor, conn

class JobManager:
    def __init__(self, client_manager):
        self.client_manager = client_manager
    
    # add job
    def add_job(self, job_name, company_name, rate, hours, location, address):
        query = """
        INSERT INTO jobs (job_name, company_name, rate, hours, location, address)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (job_name, company_name, rate, hours, location, address))
        conn.commit()
        print(f"Job '{job_name}' added for company '{company_name}'.")
    
    # list jobs
    def list_jobs(self):
        cursor.execute("""
            SELECT job_id, job_name, company_name, rate, hours, location,
            DATE_FORMAT(created_on, '%Y-%m-%d') as created_on_fmt
            FROM jobs
        """)
        jobs = cursor.fetchall()
        
        if not jobs:
            print("\nNo jobs available.")
            return

        columns = ['ID', 'Job Name', 'Company', 'Rate', 'Hours', 'Location', 'Created']
        
        widths = {col: len(col) for col in columns}
        for job in jobs:
            for i, value in enumerate(job):
                widths[columns[i]] = max(widths[columns[i]], len(str(value)))
        
        print("\n" + "-" * (sum(widths.values()) + (len(columns) * 3) + 1))
        header = "| "
        for col in columns:
            header += f"{col:<{widths[col]}} | "
        print(header)
        print("-" * (sum(widths.values()) + (len(columns) * 3) + 1))
        
        for job in jobs:
            row = "| "
            for i, value in enumerate(job):
                row += f"{str(value):<{widths[columns[i]]}} | "
            print(row)
        print("-" * (sum(widths.values()) + (len(columns) * 3) + 1))
    
    # update job
    def update_job(self, job_id):
        cursor.execute("SELECT * FROM jobs WHERE job_id = %s", (job_id,))
        job = cursor.fetchone()
        if not job:
            print("Invalid job ID.")
            return

        print(f"\nUpdating Job: {job[1]}")
        print("Leave blank to keep current value")

        new_name = input(f"Enter new job name ({job[1]}): ")
        new_company = input(f"Enter new company name ({job[2]}): ")
        new_rate = input(f"Enter new rate (${job[3]}): ")
        new_hours = input(f"Enter new hours ({job[4]}): ")
        new_location = input(f"Enter new location ({job[5]}): ")
        new_address = input(f"Enter new address ({job[6]}): ")

        updates = []
        values = []
        if new_name:
            updates.append("job_name = %s")
            values.append(new_name)
        if new_company:
            updates.append("company_name = %s")
            values.append(new_company)
        if new_rate:
            updates.append("rate = %s")
            values.append(float(new_rate))
        if new_hours:
            updates.append("hours = %s")
            values.append(float(new_hours))
        if new_location:
            updates.append("location = %s")
            values.append(new_location)
        if new_address:
            updates.append("address = %s")
            values.append(new_address)

        if updates:
            query = f"UPDATE jobs SET {', '.join(updates)} WHERE job_id = %s"
            values.append(job_id)
            cursor.execute(query, tuple(values))
            conn.commit()
            print("Job updated successfully!")
    
    # delete job
    def delete_job(self, job_id):
        cursor.execute("SELECT job_name, company_name FROM jobs WHERE job_id = %s", (job_id,))
        job = cursor.fetchone()
        if not job:
            print("Invalid job ID. Delete failed.")
            return

        cursor.execute("DELETE FROM jobs WHERE job_id = %s", (job_id,))
        conn.commit()
        print(f"Job '{job[0]}' for company '{job[1]}' deleted successfully.")
    
    # search jobs
    def search_jobs(self, search_term, search_type):
        query = """
        SELECT job_id, job_name, company_name, rate, hours, location,
        DATE_FORMAT(created_on, '%Y-%m-%d') as created_on_fmt
        FROM jobs WHERE """ + search_type + " LIKE %s"
        cursor.execute(query, (f'%{search_term}%',))
        jobs = cursor.fetchall()
        
        if not jobs:
            print(f"\nNo jobs found matching '{search_term}' in {search_type}.")
            return

        columns = ['ID', 'Job Name', 'Company', 'Rate', 'Hours', 'Location', 'Created']
        
        widths = {col: len(col) for col in columns}
        for job in jobs:
            for i, value in enumerate(job):
                widths[columns[i]] = max(widths[columns[i]], len(str(value)))
        
        print("\n" + "-" * (sum(widths.values()) + (len(columns) * 3) + 1))
        header = "| "
        for col in columns:
            header += f"{col:<{widths[col]}} | "
        print(header)
        print("-" * (sum(widths.values()) + (len(columns) * 3) + 1))
        
        for job in jobs:
            row = "| "
            for i, value in enumerate(job):
                row += f"{str(value):<{widths[columns[i]]}} | "
            print(row)
        print("-" * (sum(widths.values()) + (len(columns) * 3) + 1))

    def run_menu(self):
        while True:
            print("\nJob Management Menu")
            print("1. Add Job")
            print("2. List Jobs")
            print("3. Update Job")
            print("4. Delete Job")
            print("5. Search Jobs")
            print("6. Back to Main Menu") 


            choice = input("Enter your choice (1-6): ")

            if choice == '1':

                job_name = input("Enter job name: ")
                company_name = input("Enter company name: ")
                rate = float(input("Enter hourly rate: "))
                hours = float(input("Enter hours worked: "))
                location = input("Enter job location: ")
                address = input("Enter job address: ")
                self.add_job(job_name, company_name, rate, hours, location, address)

            elif choice == '2':
                self.list_jobs()

            elif choice == '3':
                cursor.execute("SELECT EXISTS(SELECT 1 FROM jobs)")
                jobs_exist = cursor.fetchone()[0]
                if not jobs_exist:
                    print("No jobs available to update.")
                    continue
                self.list_jobs()
                job_id = int(input("Enter the job ID to update: "))
                self.update_job(job_id)

            elif choice == '4':
                cursor.execute("SELECT EXISTS(SELECT 1 FROM jobs)")
                jobs_exist = cursor.fetchone()[0]
                if not jobs_exist:
                    print("No jobs available to delete.")
                    continue
                self.list_jobs()
                job_id = int(input("Enter the job ID to delete: "))
                self.delete_job(job_id)

            elif choice == '5':
                print("\nSearch by:")
                print("1. Job Name")
                print("2. Location")
                search_choice = input("Enter your choice (1-2): ")
                
                if search_choice == '1':
                    term = input("Enter job name to search: ")
                    self.search_jobs(term, 'job_name')
                elif search_choice == '2':
                    term = input("Enter location to search: ")
                    self.search_jobs(term, 'location')
                else:
                    print("Invalid search choice.")

            elif choice == '6':
                print("Exiting Job Management Menu.")
                break
            else:
                print("Invalid choice. Please try again.")