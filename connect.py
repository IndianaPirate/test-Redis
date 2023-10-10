import redis

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
redis = redis.Redis(connection_pool=pool)

def setValue(name, value):
    redis.set(name, value)

def getValue(name):
    value = redis.get(name)
    return value

setValue("name", "Rakoto")
print("Name: ",getValue("name"))
