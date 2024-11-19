class ClientManager:
    def __init__(self):
        self.clients = []

    def add_client(self, name, contact_info):
        client = {"name": name, "contact_info": contact_info}
        self.clients.append(client)
        print(f"Client '{name}' added.")

def view_clients(self):
  if not self.clients:
    print("\nNo clients found.")
    return

  print("\n-- Client List --")
  for client_id, client in self.clients.items():
    print(f"\nClient ID: {client_id}")
    print(f"Name: {client['name']}")
    print(f"Contact: {client['contact']}")
    print(f"Notes: {client['notes']}")

def search_clients(self):
  search_term = input("\nEnter client name to search: ").lower()
  found = False

  for client_id, client in self.clients.items():
    if search_term in client['name'].lower():
      print(f"\nClient ID: {client_id}")
      print(f"Name: {client['name']}")
      print(f"Contact: {client['contact']}")
      found = True

  if not found:
    print("\nNo matching clients found.")

 def update_client(self):
        try:
            client_id = int(input("\nEnter Client ID to update: "))
            if client_id < 0 or client_id >= len(self.clients):
                print("\nInvalid Client ID.")
                return

            name = input("Enter new name (leave blank to keep current): ")
            contact = input("Enter new contact info (leave blank to keep current): ")
            notes = input("Enter new notes (leave blank to keep current): ")

            if name:
                self.clients[client_id]['name'] = name
            if contact:
                self.clients[client_id]['contact'] = contact
            if notes:
                self.clients[client_id]['notes'] = notes

            print(f"Client ID {client_id} updated successfully.")
        except ValueError:
            print("\nInvalid input. Please enter a valid Client ID.")

 def delete_one_client(self):
        try:
            client_id = int(input("\nEnter Client ID to delete: "))
            if client_id < 0 or client_id >= len(self.clients):
                print("\nInvalid Client ID.")
                return

            deleted_client = self.clients.pop(client_id)
            print(f"Client '{deleted_client['name']}' deleted.")
        except ValueError:
            print("\nInvalid input. Please enter a valid Client ID.")

 def delete_all_clients(self):
        confirmation = input("\nAre you sure you want to delete all clients? (yes/no): ").lower()
        if confirmation == 'yes':
            self.clients.clear()
            print("\nAll clients have been deleted.")
        else:
            print("\nOperation cancelled.")
 def run_menu(self):
        while True:
            print("\n-- Client Management --")
            print("1. Add New Client")
            print("2. View Clients")
            print("3. Search Clients")
            print("4. Update Client")
            print("5. Delete One Client")
            print("6. Delete All Clients")
            print("7. Back to Main Menu")

