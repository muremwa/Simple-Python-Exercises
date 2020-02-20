# Ask user information, for ex: name, department, college etc and display them using print function

def main():
    name = input('Enter your name: ')
    college = input('Enter your college: ')
    department = input('Enter your department: ')

    print('\n')
    print('-'*35)
    print('Name' + ' '*(len('department')-len('name')), ': ', name)
    print('College' + ' '*(len('department') - len('college')), ': ', college)
    print('Department : ', department)


if __name__ == '__main__':
    main()
