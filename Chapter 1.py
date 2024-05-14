a = 10
b = 20
c = 30
d = a + b + c
print(d)

n = 5
n = n + 1
n = n + 1
print(n)

a = 5
x = 2.5
b = a + x
print(b)

a = 6.5
b = 2.1
c = a * b
d = a // b
print(c)
print(d)

quot, rem = divmod(23, 10)
print(quot, rem)

# x = input("Enter a number: ")
# print(type(x))
#
# x = int(input("Enter a number: "))
# print(type(x))

# how to alter a string with concatenation
my_str = "a"
my_str += "b"
my_str += "c"
print(my_str)

a_list = []

while True:
    s = input('Enter name: ')
    if not s:
        break
    a_list.append(s)
a_list.sort()
print(a_list)

