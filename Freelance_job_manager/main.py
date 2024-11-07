#!/usr/bin/python3
# Import required modules
from datetime import datetime

# Initialize data structures
clients = {}
jobs = {}
client_id_counter = 1
job_id_counter = 1


def display_menu():
    """Display the main menu options"""
    print("\n===== FREELANCE JOB MANAGER =====")
    print("\nOur app is designed to help you stay in control of your freelance business with three essential features:")
    print("1. Client Management")
    print("2. Job Management")
    print("3. Financial Overview")
    print("\nLet’s get started on simplifying your freelance workflow!")
    print("\nPress 4 to quit the App")

# Rest of your functions...
def add_client():
    """Add a new client to the system"""
    global client_id_counter
    print("\n-- Add New Client --")
    name = input("Enter client name: ")
    contact = input("Enter client contact (email/phone): ")
    notes = input("Enter any notes (optional): ")

    clients[client_id_counter] = {
        'name': name,
        'contact': contact,
        'notes': notes
    }
    print(f"\nClient added successfully! Client ID: {client_id_counter}")
    client_id_counter += 1


def view_clients():
    """Display all clients"""
    if not clients:
        print("\nNo clients found.")
        return

    print("\n-- Client List --")
    for client_id, client in clients.items():
        print(f"\nClient ID: {client_id}")
        print(f"Name: {client['name']}")
        print(f"Contact: {client['contact']}")
        print(f"Notes: {client['notes']}")


def search_clients():
    """Search for clients by name"""
    search_term = input("\nEnter client name to search: ").lower()
    found = False

    for client_id, client in clients.items():
        if search_term in client['name'].lower():
            print(f"\nClient ID: {client_id}")
            print(f"Name: {client['name']}")
            print(f"Contact: {client['contact']}")
            print(f"Notes: {client['notes']}")

            found = True

    if not found:
        print("\nNo matching clients found.")


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


def mark_job_complete():
    """Mark a job as complete"""
    view_jobs('active')
    job_id = input("\nEnter job ID to mark as complete: ")

    if job_id.isdigit() and int(job_id) in jobs:
        jobs[int(job_id)]['status'] = 'completed'
        print("\nJob marked as complete!")
    else:
        print("\nInvalid job ID.")


def view_financial_summary():
    """Display financial overview"""
    total_earnings = 0
    pending_amount = 0

    for job in jobs.values():
        if job['status'] == 'completed':
            total_earnings += job['price']
        else:
            pending_amount += job['price']

    print("\n-- Financial Summary --")
    print(f"Total Earnings: ${total_earnings:.2f}")
    print(f"Pending Payments: ${pending_amount:.2f}")
    print(f"Total Value: ${(total_earnings + pending_amount):.2f}")


def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-4): ")

        if choice == '1':
            while True:
                print("\n-- Client Management --")
                print("1. Add New Client")
                print("2. View Clients")
                print("3. Search Clients")
                print("4. Back to Main Menu")

                sub_choice = input("\nEnter your choice (1-4): ")
                if sub_choice == '1':
                    add_client()
                elif sub_choice == '2':
                    view_clients()
                elif sub_choice == '3':
                    search_clients()
                elif sub_choice == '4':
                    break
                else:
                    print("\nInvalid choice. Please try again.")

        elif choice == '2':
            while True:
                print("\n-- Job Management --")
                print("1. Add New Job")
                print("2. View Active Jobs")
                print("3. View Completed Jobs")
                print("4. Mark Job Complete")
                print("5. Back to Main Menu")

                sub_choice = input("\nEnter your choice (1-5): ")
                if sub_choice == '1':
                    add_job()
                elif sub_choice == '2':
                    view_jobs('active')
                elif sub_choice == '3':
                    view_jobs('completed')
                elif sub_choice == '4':
                    mark_job_complete()
                elif sub_choice == '5':
                    break
                else:
                    print("\nInvalid choice. Please try again.")

        elif choice == '3':
            view_financial_summary()

        elif choice == '4':
            print("\nThank you for using Freelance Job Manager!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
