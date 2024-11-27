#High-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend on details; details should depend on abstractions.

#Example:
#Bad Design:
#A Database class directly dependent on a specific database implementation:
class MySQLDatabase:
    def connect(self):
        return "Connecting to MySQL"

class Application:
    def __init__(self):
        self.db = MySQLDatabase()

    def run(self):
        return self.db.connect()
#Good Design:
#Introduce an abstraction layer:

class Database:
    def connect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        return "Connecting to MySQL"

class MongoDBDatabase(Database):
    def connect(self):
        return "Connecting to MongoDB"

class Application:
    def __init__(self, db: Database):
        self.db = db

    def run(self):
        return self.db.connect()

# Usage
app = Application(MySQLDatabase())
print(app.run())