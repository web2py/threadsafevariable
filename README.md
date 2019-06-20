# ThreadSafeVariable

## The problem

Imagine you have class like this

```
class A(object):
    def __init__(self, x):
        self.x = x

a = A(3)
print(a.x)
```

``a.x`` is a member variable of object ``a``. It is not thread safe. This means that if one thread changes `a.x``, all other threads see the new value. You can avoid this using a thread local object:

```
import threading

class A(object):    
    def __init__(self, x):
        self.local = threading.local()
        self.local.x

a = A(3)
print(a.local.x)
``` 

This works but has two downsides:

- you have changed the syntax
- even if a is accessible from other threads, a.local.x is only defined for the one thread that created the object

The ThreadSafeVariable module helps solve this problem and preserves the original syntax.

## The solution

We change the code in the first example by declaring which variables should the thrad safe:

```
from threadsafevariable import ThreadSafeVariable

class A(object):
    x = ThreadSafeVariable() # we add this line
    def __init__(self, x):
        self.x = x

a = A(3)
print(a.x)
```

We have preserved the syntax for the first example but a.x is now a thread local variable.

In addition we can do:

```
iceblock = ThreadSafeVariable.freeze()
```

This will store a snapshot all ThreadSafeVariable(s) of all objects defined in the current thread.
Then for any other thread:

```
ThreadSafeVariable.restore(iceblock)
```

will restore all variables of all objects in this thread to the value stores in iceblock.