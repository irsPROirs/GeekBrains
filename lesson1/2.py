seconds = int(input('введите время в секундах: '))
hours = seconds // 3600
seconds = seconds % 3600
minutes = seconds // 60
seconds = seconds % 60
print(f'Полученное время {hours}:{minutes}:{seconds}')
print('Полученное время %d:%d:%d' % (hours, minutes, seconds))
print('Полученное время {}:{}:{}'.format(hours, minutes, seconds))
