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


