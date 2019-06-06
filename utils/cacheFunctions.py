import pickle
import pathlib

class CacheHandler():
    @staticmethod
    def setValue(key,value):
        data = {}
        data[key] = value
        file = open('sys_cache', 'wb')
        pickle.dump(data, file)
        file.close()
    
    @staticmethod
    def getValue(key):
        data = {}
        file = pathlib.Path("sys_cache")
        if file.exists ():
            cache = open('sys_cache', 'rb')
            unpickler = pickle.Unpickler(cache)
            try:
                data = unpickler.load()
            except EOFError:
                data = {}
            cache.close()
            if key in data:
                return data[key]
            else:
                return False
        else:
            cache = open('sys_cache', 'a')
            cache.close()