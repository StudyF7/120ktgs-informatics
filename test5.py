# множество set
a= {1, 1.2, 'hello'}

# множество set - create
a = {}
b = set()
c = frozenset()

a = {1, 1.1, 'a', (1, 1.1)}
a = {1, 1.1, [1,2]}

a = frozenset({1, 1.1})

a = [1, 'abc', 1]
set(a)
b = set('слово')
c = frozenset('hello')
d = set([1, [2.1], 1)

# множество set - RETRIVE (Read), UPDATE, DELETE
a = {1, 1.1 'a'}
a.add('привет')
b = 1
a.add(b)
a = {1, 2, 3}

a = {1, 2, 3}
a.update({5, 2})

a = {1, 1.1, 'a'}
a[0]

a = {1, 1.1, 'a'}
a[0] = 'a'

a = {1, 2, 3}

# удаление (методы)
a = {1, 2, 3}
a.clear