grocery = ['bread', 'milk', 'butter']

for item in enumerate(grocery):
  print(item)

print(grocery)

# loop over an enumerate object
for count, item in enumerate(grocery):
  print(count, item)

list1 =[12,22,33,44,55,66]

print(list1[6::-1])
# change the default counter and loop 
for count, item in enumerate(grocery, 100):
  print(count, item)