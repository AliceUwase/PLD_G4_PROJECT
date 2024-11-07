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
