# And
age = 120

if age >= 0 and age <= 120:
    print('Valid age')
else:
    print('Invalid age')

# Or
python_score = 40
c_score = 45

if python_score > 60 or c_score > 60:
    print('Exam passed!')
else:
    print('Failed, try harder!')

# Not
is_employee = False

if not is_employee:
    print('External staff are not allowed!')

# Elif
holiday_name = 'Birthday'

if holiday_name == 'Valentine':
    print('Buy rose, watch movie')
elif holiday_name == 'Christmas':
    print('Buy apple, fine dining')
elif holiday_name == 'Birthday':
    print('Buy cake')
else:
    print('Every day is holiday!')