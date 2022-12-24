import random

number_of_users = int(input('Enter the number of friends joining (including you): '))
if number_of_users <= 0:
    print('No one is joining for the party')
else:
    print('Enter the name of every friend (including you), each on a new line:')
    users = {input() for i in range(number_of_users)}
    users_dict = dict.fromkeys(users, 0)
    total_bill = float(input('Enter the total bill value: '))
    lucky_feature = input('Do you want to use the "Who is lucky?" feature? Write Yes/No: ')
    if lucky_feature == 'Yes':
        payer = random.sample(sorted(users_dict), 1)
        print(*payer, 'is the lucky one!')
        for key in users_dict.keys():
            if key == payer[0]:
                users_dict[key] = 0
            else:
                users_dict[key] = round(total_bill / (number_of_users - 1), 2)
    else:
        print('No one is going to be lucky')
        for key in users_dict.keys():
            users_dict[key] = round(total_bill / number_of_users, 2)
    print(users_dict)
