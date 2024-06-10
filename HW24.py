# Использование %:
team1_num = 22
team2_num = 20
print('В команде "Номер 1" %d участника' % team1_num)
print('Сегодня в команде "Номер 1" %d участника, а в команде "Номер 2" %d участников' % (team1_num, team2_num))

# Использование format():
score_2 = 32
team1_time = 1215
print('Команда "Номер 2" решила {} задачи'.format(score_2))
print('Команда "Номер 2" решила задания за {} сек.'.format(team1_time))

# Использование f-строк:
score_1 = 35
print(f'Команды сегодня решили {score_1} и {score_2} задачи, а всего {score_1+score_2}!')
if score_1 > score_2:
    challenge_result = 'Победила команда "Номер 1"!'
elif score_1 < score_2:
    challenge_result = 'Победила команда "Номер 2"!'
else:
    challenge_result = 'Ничья!'
print(f'Сегодня {challenge_result}')