def build_person(first_name, last_name, age=''):
    """return a dictionary, which includes some information about people"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendirx', age=27)
print(musician)

