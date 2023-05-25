

tp = 'house=дом','car=машина', 'men=человек', 'tree=дерево'
print(tuple(map(lambda x: tuple(x.split('=')), tp)))

tp = 'house=дом car=машина men=человек tree=дерево'
result = tuple(map(lambda x: tuple(x.split('=')), tp.split(' ')))
print(result)

def tp_tuple(info: str) -> tuple[tuple]:
    return tuple(map(lambda x: tuple(x.split('=')), info.split()))

print(tp_tuple('house=дом car=машина men=человек tree=дерево'))