people = {'mark': {'name': 'John', 'age': '27', 'sex': 'Male'},
          'tark': {'name': 'Marie', 'age': '22', 'sex': 'Female'},
          'lark': {'name': 'Luna', 'age': '24', 'sex': 'Female', 'married': 'No'}}

people[4] = {'name': 'Peter', 'age': '29', 'sex': 'Male', 'married': 'Yes'}
print(people[4])
print(people)
print("The length of dic is: ",len(people))

del people['lark']['married']
del people[4]['married']

print(people['lark'])
print(people[4])
print("Dic after deleted is: ",people)


