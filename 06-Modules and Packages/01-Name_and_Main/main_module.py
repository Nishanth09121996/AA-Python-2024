from classexample import Animal
class Lion:
    def show(self):
        print("The Module name is {}".format(__name__))
if __name__ == '__main__':
    obj  = Animal()
    obj.show()
    obj2 = Lion()
    obj2.show()