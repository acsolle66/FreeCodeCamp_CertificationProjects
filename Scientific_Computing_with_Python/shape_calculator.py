class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_picture(self):
        if self.width > 49 or self.height > 49:
            return "Too big for picture."
        else:
            counter = 0
            picture_list = []
            while counter < self.height:
                picture_list.append(["*" * self.width])
                counter += 1

            for i in range(0, len(picture_list)):
                picture_list[i].append("\n")
            picture_string_list = []

            for i in range(0, len(picture_list)):
                for j in range(0, len(picture_list[i])):
                    picture_string_list.append(picture_list[i][j])

            return "".join(picture_string_list)

    def get_amount_inside(self, shape):
        return int(self.height/shape.height) * int(self.width/shape.width)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side=0):
        super().__init__(width=side, height=side)
        self.side = side

    def set_width(self, width):
        super().set_width(width)
        self.side = width
        self.height = width

    def set_height(self, height):
        super().set_height(height)
        self.side = height
        self.width = height

    def set_side(self, side):
        self.side = side
        self.height = side
        self.width = side

    def __str__(self):
        return f"Square(side={self.side})"


