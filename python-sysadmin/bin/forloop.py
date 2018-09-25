#!/usr/bin/python3.7
# FOr loop demo

colors=['blue', 'green', 'red', 'purple'] # make a LIST of colors

for color in colors:
    print(color)


print('Now I will only print blue and red using if')
for color in colors: # This will assign the items in 'colors' to 'color' and iterate through it
    if color == 'blue':
        print(color)
        continue
    elif color == 'red':
        print(color)
        break
    else:
        continue
    print(color)
