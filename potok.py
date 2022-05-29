user_age = int(input())
if user_age <= 13:
    print('детство')
elif 14 <= user_age <= 24:
    print('молодость')
elif 25 <= user_age <= 59:
    print('зрелость')
else:
    print('старость')

