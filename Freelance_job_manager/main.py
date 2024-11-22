from client.client_management import ClientManager
from jobs.job_management import JobManager
from finance.financeManagement import FinancialSummary
from menu import display_menu

welcome_screen = """
███████╗██████╗ ███████╗███████╗██╗      █████╗ ███╗   ██╗ ██████╗███████╗
██╔════╝██╔══██╗██╔════╝██╔════╝██║     ██╔══██╗████╗  ██║██╔════╝██╔════╝
█████╗  ██████╔╝█████╗  █████╗  ██║     ███████║██╔██╗ ██║██║     █████╗  
██╔══╝  ██╔══██╗██╔══╝  ██╔══╝  ██║     ██╔══██║██║╚██╗██║██║     ██╔══╝  
██║     ██║  ██║███████╗███████╗███████╗██║  ██║██║ ╚████║╚█████╗███████
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝
     ██╗ ██████╗ ██████╗     ███╗   ███╗ █████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗██████╗ 
     ██║██╔═══██╗██╔══██╗    ████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝██╔══██╗
     ██║██║   ██║██████╔╝    ██╔████╔██║███████║██╔██╗ ██║███████║██║  ███╗█████╗  ██████╔╝
██   ██║██║   ██║██╔══██╗    ██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║██║   ██║██╔══╝  ██╔══██╗
╚█████╔╝╚██████╔╝██████╔╝    ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║██████╔╝██████╗██║  ██║
 ╚════╝  ╚═════╝ ╚═════╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
"""

def main():
    # Display welcome screen
    print(welcome_screen)
    
    # Initialize managers
    client_manager = ClientManager()
    job_manager = JobManager(client_manager)
    financial_manager = FinancialSummary(job_manager)

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-4): ")

        if choice == '1':
            client_manager.run_menu()
        elif choice == '2':
            job_manager.run_menu()
        elif choice == '3':
            financial_manager.display_summary()
        elif choice == '4':
            print("\nThank you for using Freelance Job Manager!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
