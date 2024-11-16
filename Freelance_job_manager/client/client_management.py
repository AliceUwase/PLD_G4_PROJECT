class ClientManager:
    def __init__(self):
        self.clients = []

    def add_client(self, name, contact_info):
        client = {"name": name, "contact_info": contact_info}
        self.clients.append(client)
        print(f"Client '{name}' added.")

    def list_clients(self):
        if not self.clients:
            print("No clients available.")
            return
        for idx, client in enumerate(self.clients, 1):
            print(f"{idx}. {client['name']} - {client['contact_info']}")

    def run_menu(self):
        while True:
            print("\nClient Management Menu")
            print("1. Add Client")
            print("2. List Clients")
            print("3. Back to Main Menu")
            choice = input("Enter your choice (1-3): ")

            if choice == '1':
                name = input("Enter client name: ")
                contact_info = input("Enter client contact info: ")
                self.add_client(name, contact_info)
            elif choice == '2':
                self.list_clients()
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")
