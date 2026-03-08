class Hello:
    #static method cr8 for all the object and 
    # classes once ,and common for all(everybody can 
    # use it anytime)
    #eg we make num of instance(object),but static method
    # only define once 
    @staticmethod
    #static method not access or use instance. 
    def print_hello_msg():
        print("hello world")

say_hello=Hello()
say_hello.print_hello_msg()
        