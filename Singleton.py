class Singleton:
    """__new__(cls): This is a special method in Python classes. It is
    called to create a new instance of the class. In this method,
    check whether an instance already exists (cls.__instance). If an
    instance doesn't exist, it creates a new one using the super() function
    to call the parent class's __new__ method. It also initialises a counter
    variable (cls.__counter) to 0.
    """

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__new__(cls)
            cls.__counter = 0
        return cls.__instance

    def set_counter(self,count):
        self.__counter = count
    def get_counter(self):
        return self.__counter

    def increment_counter(self):
        self.__counter += 1



