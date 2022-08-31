message = input('Enter string to modify: ')
splitted_text = message.split('_')
result = ''

for i in splitted_text:
    result += i.capitalize()

print(result)


