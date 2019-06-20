import copy
import threading


__version__ = 1.0


class ThreadSafeVariable(object):

    storage = threading.local()

    def __set__(self, instance, value):
        setattr(self.storage, "%s.%s" % (id(instance), id(self)), value)

    def __get__(self, instance, owner):
        return getattr(self.storage, "%s.%s" % (id(instance), id(self)))

    @staticmethod
    def freeze():
        return copy.copy(ThreadSafeVariable.storage.__dict__)

    @staticmethod
    def restore(image):
        for key in image:
            setattr(ThreadSafeVariable.storage, key, image[key])
