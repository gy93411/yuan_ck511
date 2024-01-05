
num=1
print(id(num))

def print_info(name):
    print(name)

print(id(print_info))
aaa=print_info
print(id(aaa))
print_info('good')

class Family:
    def __init__(self):
        print('hello')
Family()
bbb=Family
print(id(bbb))

ccc=list()

ccc.append(Family)
ccc.append(print_info)
print(ccc)
for item in ccc:
    print(item)