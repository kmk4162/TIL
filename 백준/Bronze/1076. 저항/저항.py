colors = {
    'black' : 0,
    'brown' : 1,
    'red' : 2,
    'orange' : 3,
    'yellow' : 4,
    'green' : 5,
    'blue' : 6,
    'violet' : 7,
    'grey' : 8,
    'white' : 9
}
color1 = colors[input()]
color2 = colors[input()]
mul = 10 ** colors[input()]

digits = color1 * 10 + color2
print(digits * mul)
