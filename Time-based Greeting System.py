hour = int(input('hello! what time is it?(millitary time format/whole number): '))

if 5 <= hour < 12:
    print('good morning!')
elif 12 <= hour < 18:
    print('good afternoon!')
elif 18 <= hour < 22:
    print('good evening!')
else:
    print('good night!')