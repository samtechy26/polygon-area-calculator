class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

  def set_width(self, val):
    self.width = val

  def set_height(self, val):
    self.height = val

  def get_area(self):
    area = self.width * self.height
    return area

  def get_perimeter(self):
    perimeter = 2 * self.width + 2 * self.height
    return perimeter

  def get_diagonal(self):
    diagonal = (self.width**2 + self.height**2)**0.5
    return diagonal

  def get_picture(self):
    col = self.width
    row = self.height
    img = ''
    if col > 50:
      return "Too big for picture."
    for i in range(row):
      for j in range(col):
        img += '*'
      img += '\n'
    return img

  def get_amount_inside(self, shape):
    shape_height = shape.height
    shape_width = shape.width
    outer_perimeter = self.get_area()
    inner_perimeter = shape.get_area()
    amount_inside = outer_perimeter // inner_perimeter
    return amount_inside


class Square(Rectangle):

  def __init__(self, side_length):
    super().__init__(side_length, side_length)

  def __str__(self):
    return f'Square(side={self.width})'

  def set_side(self, val):
    super().set_width(val)
    super().set_height(val)
