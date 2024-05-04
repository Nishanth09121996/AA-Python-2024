class Animal:
    def __init__(self) -> None:
        pass
        
    def show(self):
        print("The Module name is {}".format(__name__))

if __name__ == '__main__':
    obj = Animal()
    obj.show()