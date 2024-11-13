class ClientManager:
    def __init__(self):
        self.client = {}
    def add_client(self,name,contact_info):
        client = {"name":name,"contact_info": contact_info}
        self.clients.append(client)
        print(f"client'{name}'added.")
