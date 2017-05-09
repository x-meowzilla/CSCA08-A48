x = 1
y = x
y = 2
print(x, y)

x = [1, 2, 3]
y = x
x[0] = 99
print(x, y)

x = "Hello"
y = x
x = "Bye"
print(x, y)

x = [1, 2, 3]
y = [1, 2, 3]
x[0] = 99
y[0] = 98
print(x, y)

x = [1, 2, 3]
y = x[:]
x[0] = 99
y[0] = 98
print(x, y)

x = [[1, 2], 3]
y = x[:]
x[0][0] = 99
y[0][1] = 98
print(x, y)

def mutator1(x):
    x[0] = "MUTATED"

def mutator2(x):
    x[0][0] = "MUTATED"
    
def cloner1(x):
    clone = x[:]
    clone[0] = "COPIED"
    return clone

def cloner2(x):
    clone = x[:]
    clone[0][0] = "COPIED"
    return clone

x = [['A', 'B'], 'C']
y = mutator1(x)
print(x, y)

x = [['A', 'B'], 'C']
y = cloner1(x)
print(x, y)

x = [['A', 'B'], 'C']
y = mutator2(x)
print(x, y)

x = [['A', 'B'], 'C']
y = cloner2(x)
print(x, y)
    
