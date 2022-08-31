name_age = input('Enter name and dates: ')

devided_data = name_age.split('*')
name = devided_data[0]
birth_year = int(devided_data[1].split('-')[0])
death_year = int(devided_data[2].split('-')[0])
age = death_year - birth_year

print(f'Name: {name}\n'
      f'Age: {age}')

