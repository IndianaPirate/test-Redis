import redis

pool = redis.ConnectionPool(host='localhost', port=6379, username="default", password="password123", db=0)
redis = redis.Redis(connection_pool=pool)

if redis.ping():
    print("Connexion reussi")
else:
    print("Erreur de connexion")

def setValue(name, value):
    redis.set(name, value)

def getValue(name):
    value = redis.get(name)
    return value

setValue("name", "Milasoa")
print("Name: ",getValue("name"))
