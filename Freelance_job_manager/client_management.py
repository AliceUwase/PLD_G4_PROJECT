#!/usr/bin/python3
# All the core process functionalities for the Client management feature in the app
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

