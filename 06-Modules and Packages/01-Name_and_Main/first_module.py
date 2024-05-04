print('This module will be ran by default')

def main():
    print('The module name is {}'.format(__name__))

if __name__ == '__main__':
    main()