#!/usr/bin/python3
# All the core functionalities for the Financial management feature
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

