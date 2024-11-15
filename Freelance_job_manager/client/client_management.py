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

def run_menu(self):
  while True:
    print("\n-- Client Management --")
    print("1. Add New Client")
    print("2. View Clients")
    print("3. Search Clients")
    print("4. Back to Main Menu")

    sub_choice = input("\nEnter your choice (1-4): ")
    if sub_choice == '1':
      self.add_client()
    elif sub_choice == '2':
      self.view_clients()
    elif sub_choice == '3':
      self.search_clients()
    elif sub_choice == '4':
      break
    else:
      print("\nInvalid choice. Please try again.")
