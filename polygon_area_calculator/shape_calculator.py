import math
class Rectangle:
  def __init__(self,width,height):
    self.width = width
    self.height = height

  def __str__(self):
    otpt_str = f"Rectangle(width={self.width}, height={self.height})"
    return otpt_str

  def set_width(self,width):
    self.width = width

  def set_height(self,height):
    self.height = height

  def get_area(self):
    area = self.width * self.height
    return area

  def get_perimeter(self):
    perimeter = (self.width + self.height) * 2
    return perimeter

  def get_diagonal(self):
    diagonal = (self.width**2 + self.height**2) ** 0.5
    return diagonal

  def get_picture(self):
    if self.width>50 or self.height>50:
      return "Too big for picture."
    else:
      shape_string = ""

      for i in range(self.height):
        shape_string += f"{'*' * self.width}\n"
      return shape_string

  def get_amount_inside(self,shape):
    fit_shape = 0
    if shape.height>self.height or shape.width>self.width:
      return fit_shape
    else:
      x = shape.height
      while(x <= self.height):
        fit_shape += math.floor(self.width / shape.width)
        x += shape.height
      return fit_shape

class Square(Rectangle):
  def __init__(self,width):
    self.width = width
    self.height = width

  def __str__(self):
    sqr_str = f"Square(side={self.width})"
    return sqr_str

  def set_side(self,side):
    self.width = side
    self.height = side

  def set_height(self, height):
    super().set_height(height)
    self.width = height
  
  def set_width(self, width):
    super().set_width(width)
    self.height = width