clients = {}
job_id_counter = 0

def add_job():
   """Add a new job"""
   global job_id_counter

   if not clients:
       print("\nNo clients available. Please add a client first.")
       return
   print("\n-- Add New Job --")
   view_clients()
   client_id = input("\nEnter client ID: ")

   if client_id.isdigit() and int(client_id) in clients:
       project_name = input("Enter project name: ")
       due_date = input("Enter due date (DD/MM/YYYY): ")
       price = float(input("Enter project price: "))

       jobs[job_id_counter] = {
           'client_id': int(client_id),
           'project_name': project_name,
           'due_date': due_date,
           'price': price,
           'status': 'active'
       }
       print(f"\nJob added successfully! Job ID: {job_id_counter}")
       job_id_counter += 1
   else:
       print("\nInvalid client ID.")

   def view_jobs(status='all'):
       """View jobs based on status"""
       if not jobs:
           print("\nNo jobs found.")
           return
       print(f"\n-- Job List ({status.title()}) --")
       for job_id, job in jobs.items():
           if status == 'all' or job['status'] == status:
               client = clients[job['client_id']]
               print(f"\nJob ID: {job_id}")
               print(f"Client: {client['name']}")
               print(f"Project: {job['project_name']}")
               print(f"Due Date: {job['due_date']}")
               print(f"Price: ${job['price']:.2f}")
               print(f"Status: {job['status']}")



