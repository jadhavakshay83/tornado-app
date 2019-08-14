import redis

class RedisHandler():
    client = None
    def getClient(self):
        if(client != None):
            return client
        else:
            client = redis.Redis(host='localhost', port=6379, db=1)
            return client
    
    def getValue(self,key):
        return client.get(key)
    
    def setValue(self,key,value):
        return client.set(key,value)