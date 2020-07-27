student = {'name': 'John', 'age': 25, 'courses': ['Math', 'English']}

student['phone'] = '555-5555'
student.get('phone', 'Not Found')

student.update({'name': 'Jane', 'age': 26, "phone": '555-6666'})

print(student['name'])
print(student['courses'])
print(student['phone'])
age = student.pop('age')

print(student)
print(age)
print(len(student))  # returns the number of elements in the dictionary
print(student.keys())  # print out all the keys
print(student.values())  # print out all values
print(student.items())  # print out key value pairs

for key in student:
    print(key)



for key, value in student.items():
    print(key, value)
