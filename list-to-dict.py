names = [
    'daniel',
    'mike',
    'william'
]

#List Comprehension
#length = [len(name) for name in names]

#dictionary comprehension
length = {name:len(name) for name in names}
print(length)