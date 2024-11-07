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

