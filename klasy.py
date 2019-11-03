class Super:
    def method(self):
        print('w Super.method')

class Sub(Super):
    def method(self):
        print('poczatek w sub.method')
        Super.method(self)
        print('koniec sub.method')







x = Super()
x.method()


x = Sub()
x.method()


