

# Python Private Variables and Methods

Python does not have _true_ private variables. It does not enforce privacy in the way some other languages like Java or C++ do.  
A general guideline that helps produce better code, encapsulation, is
to make everything as hidden as possible. This can be achieved by using underscores, single or double.
## Single Underscore & Double Underscores

`_foo`: Python convention says that this is to be treated as a private variable. There is no Python enforcement. 

`__foo`: This takes _privacy_ to the next level, name mangling will be used and there will be Python enforcement.



## Name Mangling - leading double underscore
Leading double underscore names are a signal that the variable is
intended to be _"private"_, meaning it should not be accessed or modified directly from outside its containing class. 
Variables with double underscores have their local scope enforced when a variable in a function is declared with a double 
underscore. It is used to prevent accidental reuse of variables or clashes.

Name mangling sounds more complicated than it is. It is just the variable name with the class name and `_` prefixed to the front.

mangled name: <span style="color: orange;">_</span> + <span style="color: orange;">&lt;class name&gt;</span> + <span style="color: orange;">__variable</span>  


In the example code, the __counter variable is prefixed by the name of the class. The Python interpreter will automatically
mangle leading `__` names.




Therefore, the new mangled name for the original variable name ___counter_ in class Singleton becomes <span style="color: orange;">_Singleton__counter</span>





### Enforcement - AttributeError raised

The following unittest, correctly raises an AttributeError. 
The variable name has been mangled by the Python interpreter and does not appear to the programmer in its originally typed form. 
The name that the programmer is trying to access does not exist.
The user may not access the variable and an error is raised, this is a desired behaviour.

```python
        def test_get_private_variable_error(self):
        """access member variable not allowed."""
        with self.assertRaises(AttributeError):
            dun1 = Singleton()
            x = dun1.__counter
```
### AttributeError can be avoided

The mangled name can be accessed without raising an error.

This is not recommended as it violates the principle of encapsulation, but it is possible and is therefore not truly private. 

It is here for demonstration purposes only. 

### unittest - passes using mangled name
```python
    def test__modify_contents_mangled_name(self):
        """Demostration purposes only. This is not good programming
        practice."""
        self.s1._Singleton__counter = 345
        print(f"s1.__dict__: {self.s1.__dict__}")
        print(f"s2.__dict__: {self.s2.__dict__}")
        print(f"s3.__dict__: {self.s3.__dict__}")
        self.assertEqual(self.s1._Singleton__counter, 345)
        self.assertEqual(self.s1._Singleton__counter, self.s3._Singleton__counter)
        self.assertEqual(self.s2._Singleton__counter, self.s3._Singleton__counter)
```
### output

```
    s1.__dict__: {'_Singleton__counter': 345}
    s2.__dict__: {'_Singleton__counter': 345}
    s3.__dict__: {'_Singleton__counter': 345}
```

