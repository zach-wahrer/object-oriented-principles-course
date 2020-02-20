from shapes import Triangle, Rectangle, Oval, Paper


def draw_rectangle(rect_vars, rect_dict):
    name, size, color, location = rect_vars
    rect_dict[name] = Rectangle()
    rect_dict[name].set_width(size[0])
    rect_dict[name].set_height(size[1])
    rect_dict[name].set_color(color)
    rect_dict[name].set_x(location[0])
    rect_dict[name].set_y(location[1])
    rect_dict[name].draw()


rect_dict = {}

rectangles = [
    ('rect1', (200, 100), 'blue', (200, 200)),
    ('rect2', (50, 150), 'yellow', (100, 100))
]

for rect in rectangles:
    draw_rectangle(rect, rect_dict)

oval1 = Oval()
oval1.randomize()
oval1.draw()

tri1 = Triangle()
tri1.randomize()
tri1.draw()


Paper.display()
