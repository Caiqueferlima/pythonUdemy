from sys import getsizeof
# lista:
num = [x * 10 for x in range(20)]
print(getsizeof(num))

# generator:
num = (x * 10 for x in range(20))
print(getsizeof(num))

# a única diferença são os () e []

# o generator não vai armazenar os
# valores na memória, só vai trazê-los 
# quando necessário.
