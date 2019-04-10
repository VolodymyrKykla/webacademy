# age_intervals = [14, 18, 12, 12333]
#
# user_birth = int(input('enter your birth year (0000):'))
#
# current_year = 2019
#
# user_age = current_year - user_birth
#
# shop_access = False if user_age < 18 else True
# print (shop_access)
#
# # if user_age <= 14:
# #     print("Redirect to 1 shop")
# # elif 15 <= user_age <=18:
# #     print('redirect to 2')
# # else:
# #     print('fuck off')

while True:
    user_name = input ('Enter your name: ')
    if len(user_name) > 50 or not len(user_name):
        print('wrong name')
        continue

    user_b = input('enter your b (0000)')
    if len(user_b) != 4 or int(user_b) < 1930 or int(user_b) > current_y:
        print('wrong year')
        continue

    current_y = 2019

    user_age = current_y - int(user_b)

    if user_age < 18:
        print ('Uderage')
        break
    else:
        print ('welcome')
        break
