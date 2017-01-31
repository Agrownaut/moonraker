print("test")

t = "test"
print(t)

t = "admin"
print(t)

s = 1

if s == 0:
    print("Zero")
else:
    print("One")


def doSomething():
    print("Did something")

doSomething()

def somethingElse(functionname):
    functionname()

somethingElse(doSomething)

r = []
print(r)
r.append(1)
r.append(2)
print(r)
print(len(r))
print(r)
