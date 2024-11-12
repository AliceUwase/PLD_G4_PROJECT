from menu import display_menu
from auth.authentication import authenticate
from client.client_manager import ClientManager
from finance.financial_manager import FinancialManager
from jobs.job_management import JobManager

def main():
    client_manager = ClientManager()
    job_manager = JobManager()
    financial_manager = FinancialManager()
    
    while True:
        display_menu ()
        choice = input('Enter your choice: ')
        
        if choice == '1':
            client_manager.run_menu()
        elif choice == '2':
            job_manager.run_menu()
        elif choice == '3':
            financial_manager.view_summary()
        elif choice == '4':
            print("\nThank you for using Freelance Job Manager Visit!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == '__main__':
    main()
            
        