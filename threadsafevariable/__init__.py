import copy
import threading


__version__ = 1.1


class ThreadSafeVariable:

    storage = threading.local()
    master_thread = threading.current_thread()
    defaults = {}

    def __set__(self, instance, value):
        if self.master_thread == threading.current_thread():
            self.defaults[id(instance)] = value
        setattr(self.storage, "%s.%s" % (id(instance), id(self)), value)

    def __get__(self, instance, owner):
        return getattr(
            self.storage,
            "%s.%s" % (id(instance), id(self)),
            self.defaults.get(id(instance)),
        )

    @staticmethod
    def freeze():
        return copy.copy(ThreadSafeVariable.storage.__dict__)

    @staticmethod
    def restore(image):
        for key in image:
            setattr(ThreadSafeVariable.storage, key, image[key])
