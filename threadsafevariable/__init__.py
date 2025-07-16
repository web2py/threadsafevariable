import copy
import threading


__version__ = 20250716.1


class ThreadSafeVariable:

    storage = threading.local()
    storage.vars = {}
    master_thread = threading.current_thread()
    defaults = {}

    def __set__(self, instance, value):
        key = "%s.%s" % (id(instance), id(self))
        if self.master_thread == threading.current_thread():
            self.defaults[key] = value
        self.storage.vars[key] = value

    def __get__(self, instance, owner):
        key = "%s.%s" % (id(instance), id(self))
        try:
            return self.storage.vars[key]
        except KeyError: 
            return self.defaults.get(key)

    @staticmethod
    def freeze():
        return copy.copy(ThreadSafeVariable.storage.vars)

    @staticmethod
    def restore(image):
        ThreadSafeVariable.storage.vars = copy.copy(image)
