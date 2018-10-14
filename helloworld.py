class hello:
    def __init__(self):
        print("hello im chirchir")

    def welcomemore(self,name):
        print("hello " + name + ",how may I help you")

    def goodbye(self,name):
        print("Goodbye " + name + ",see you soon")



hello = hello()
action = input("Hi what is your name?").upper()
hello.welcomemore(action)
hello.goodbye(action)
