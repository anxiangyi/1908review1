import re

print(re.search('A(super.*?)B', 'AsuperBxyzAsuper111Bsuper'))
print(re.match('A(super.*?)B', 'AsuperBxyzAsuper111Bsuper'))
print(re.findall('A(super.*?)B', 'AsuperBxyzAsuper111Bsuper'))

s = 'admin=22,lisi=19,wangwu=20'
print(re.findall(r'=(\d+)', s))


def test(match):
    age = int(match.group())
    age += 1
    return str(age)


result = re.sub(r'(\d+)', test, s,count=1)
print(result)

r = range(0,5)
print(r,type(r))

for i in range(0,5):
    pass

