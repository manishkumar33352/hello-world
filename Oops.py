import random

class Server:
    def __init__(self):
        """Creates a new server instance, with no active connections."""
        self.connections = {}

    def add_connection(self, connection_id):
        """Adds a new connection to this server."""
        self.connection_load = random.random() * 10 + 1
        self.connection = {connection_id: connection_load}
        self.connections.update(connection)

    def close_connection(self, connection_id):
        """Closes a connection on this server."""
        del self.connections[connection_id]

    def load(self):
        """Calculates the current load for all connections."""
        total = sum(self.connections.values())
        return total

    def __str__(self):
        """Returns a string with the current load of the server"""
        return "{:.2f}%".format(self.load())



server = Server()
server.add_connection("192.168.1.1")
print(server.load())
