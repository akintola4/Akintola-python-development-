#collections in pyhton are lists, tuples, sets, dictionaries etc 
temitope = {}
temitope['first'] = 'temitope'
temitope['last'] = 'akintola'

fola = {}
fola['first'] = 'fola'
fola['last'] = 'akintola'

#always check that it is a [] and not a {}
#this is a list
people = []
people.append(temitope)
people.append(fola)
people.append({
    'first': 'bill', 'last': 'gates'
})

print(type(people))