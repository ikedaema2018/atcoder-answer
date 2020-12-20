data = [
  "3 2",
  "4 4",
  "4 4",
  "4 4"
]

def input():
  return data.pop(0)

height, width = list(map(int, input().split(" ")))
number_rows = []

for _ in range(0, height):
  number_rows.append(list(map(int, input().split(" "))))
  
min_number = 100

for number_row in number_rows:
  for number in number_row:
    min_number = number if min_number > number else min_number

sum = 0

for number_row in number_rows:
  for number in number_row:
    sum += (number - min_number)
    
print(sum)