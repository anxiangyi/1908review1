import random


class RandomIter(object):
    def __init__(self):
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < 30:
            self.count += 1
            ran = random.randint(1, 50)
            return ran
        else:
            raise StopIteration


g = RandomIter()

print(next(g))
print(next(g))
print(next(g))
print(next(g))

print('---------------------------------')


class Randomlter:
    def __init__(self, start, end, times):
        self.start = start
        self.end = end
        self.max_times = times
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count <= self.max_times:
            return random.randint(self.start, self.end)
        else:
            raise StopIteration()


r = Randomlter(1, 50, 30)

print(next(r))
print(next(r))
print(next(r))
print(next(r))

print('-----------------')


def rand():
    for i in range(30):
        a = random.randint(1, 50)
        yield a


print(next(rand()))
print(next(rand()))
print(next(rand()))
print(next(rand()))
