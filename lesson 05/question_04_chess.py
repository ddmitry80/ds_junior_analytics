def define_color(xy_cord):
    """ Возвращает 0 если клетка черная, 1 если клетка белая  """
    coord_line='ABCDEFGH'
    x_cord = xy_cord[0]
    y_cord = xy_cord[1]
    x_up = x_cord.upper()
    x = coord_line.find(x_up) + 1
    y = int(y_cord)
    return (x + y) % 2


cell_a = input('Введите коррдинаты клетки 1 в формате "A1":')
cell_b = input('Введите коррдинаты клетки 1 в формате "A1":')
color_a = define_color(cell_a)
color_b = define_color(cell_b)
print(color_a, color_b)
if color_a == color_b:
    print('Клетки одного цвета')
else:
    print('Клетки разных цветов')