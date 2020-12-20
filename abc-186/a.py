data = [
  "10 3"
]

def input():
  return data.pop(0)

maximum_weight, perKg = map(int, input().split(" "))
print(maximum_weight // perKg)