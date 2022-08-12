sec = int(input("Введите секунды: "))
hour = sec // 3600
minutes = sec // 60

sec = sec % 60
minutes = minutes % 60

# if hour < 10:
# hour = '0' + str(hour)
# if minutes < 10:
# minutes = '0' + str(minutes)
# if sec < 10:
# sec = '0' + str(sec)

# print(f'{hour}:{minutes}:{sec}')
print(f'%02d:%02d:%02d' % (hour, minutes, sec))