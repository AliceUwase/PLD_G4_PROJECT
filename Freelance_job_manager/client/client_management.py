from db.db import cursor, conn

class ClientManager:
    def __init__(self):
        pass

    def add_client(self, name, contact_info, notes=""):
        query = """
        INSERT INTO clients (name, contact_info, notes)
        VALUES (%s, %s, %s)
        """
        cursor.execute(query, (name, contact_info, notes))
        conn.commit()
        print(f"Client '{name}' added.")

    def view_clients(self):
        cursor.execute("SELECT * FROM clients")
        clients = cursor.fetchall()
        
        if not clients:
            print("\nNo clients found.")
            return

        print("\n-- Client List --")
        for client in clients:
            print(f"\nClient ID: {client[0]}")
            print(f"Name: {client[1]}")
            print(f"Contact: {client[2]}")
            print(f"Notes: {client[3]}")

    def search_clients(self):
        search_term = input("\nEnter client name to search: ").lower()
        
        query = "SELECT * FROM clients WHERE LOWER(name) LIKE %s"
        cursor.execute(query, (f"%{search_term}%",))
        clients = cursor.fetchall()

        if not clients:
            print("\nNo matching clients found.")
            return

        for client in clients:
            print(f"\nClient ID: {client[0]}")
            print(f"Name: {client[1]}")
            print(f"Contact: {client[2]}")

    def update_client(self):
        try:
            client_id = int(input("\nEnter Client ID to update: "))
            
            # Check if client exists
            cursor.execute("SELECT * FROM clients WHERE client_id = %s", (client_id,))
            if not cursor.fetchone():
                print("\nInvalid Client ID.")
                return

            name = input("Enter new name (leave blank to keep current): ")
            contact = input("Enter new contact info (leave blank to keep current): ")
            notes = input("Enter new notes (leave blank to keep current): ")

            updates = []
            values = []
            if name:
                updates.append("name = %s")
                values.append(name)
            if contact:
                updates.append("contact_info = %s")
                values.append(contact)
            if notes:
                updates.append("notes = %s")
                values.append(notes)

            if updates:
                query = f"UPDATE clients SET {', '.join(updates)} WHERE client_id = %s"
                values.append(client_id)
                cursor.execute(query, tuple(values))
                conn.commit()
                print(f"Client ID {client_id} updated successfully.")
            
        except ValueError:
            print("\nInvalid input. Please enter a valid Client ID.")

    def delete_one_client(self):
        try:
            client_id = int(input("\nEnter Client ID to delete: "))
            
            # Check if client exists
            cursor.execute("SELECT name FROM clients WHERE client_id = %s", (client_id,))
            client = cursor.fetchone()
            if not client:
                print("\nInvalid Client ID.")
                return

            cursor.execute("DELETE FROM clients WHERE client_id = %s", (client_id,))
            conn.commit()
            print(f"Client '{client[0]}' deleted.")
            
        except ValueError:
            print("\nInvalid input. Please enter a valid Client ID.")

    def delete_all_clients(self):
        confirmation = input("\nAre you sure you want to delete all clients? (yes/no): ").lower()
        if confirmation == 'yes':
            cursor.execute("DELETE FROM clients")
            conn.commit()
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

            sub_choice = input("\nEnter your choice (1-7): ")
            if sub_choice == '1':
                name = input("Enter client name: ")
                contact_info = input("Enter client contact info: ")
                notes = input("Enter client notes (optional): ")
                self.add_client(name, contact_info, notes)
            elif sub_choice == '2':
                self.view_clients()
            elif sub_choice == '3':
                self.search_clients()
            elif sub_choice == '4':
                self.update_client()
            elif sub_choice == '5':
                self.delete_one_client()
            elif sub_choice == '6':
                self.delete_all_clients()
            elif sub_choice == '7':
                break
            else:
                print("\nInvalid choice. Please try again.")

