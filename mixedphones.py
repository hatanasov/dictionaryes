""" You will be given several phone entries, in the form of strings in format:
    {firstElement} : {secondElement}.When you receive the command “Over”, you
    are to print all names you’ve stored with their phones.The names must be
    printed in alphabetical order.
    Example: input       ouput
    123123123 : Nanyo   Nanyo -> 123123123
    Pesho : 150925812   Pesho -> 150925812
    Over
"""

def get_contacts():
    contacts_list = []
    while True:
        contact = input().split(' : ')
        if contact == ['Over']:
            break
        contact.sort()
        contacts_list.append({'name': contact[1], 'number': contact[0]})
    return sorted(contacts_list, key=lambda k: k['name'])

for contact in get_contacts():
    print(contact['name'], '->', contact['number'])
