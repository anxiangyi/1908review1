class Person:

    def __del__(self):
        print('--------->del')

    def __str__(self):
        return 'abc'

    def run(self):
        print('-------->run')


p = Person()
print(p)

p1 = p
p2 = p

# del p
# del p1
# del p2

# p1.run()

print('----over----')
