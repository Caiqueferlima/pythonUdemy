somar10 = lambda x: x + 10
print(somar10(2))

def func(x):
  func2 = lambda x: x + 10
  return func2(x) * 5

print(func(2))