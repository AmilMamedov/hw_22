# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных, 
# чтобы было понятно, за что эти переменные отвечают 
# и что происходит и без комментариев


class Unit:
    def __init__(self, field, x_coord, y_coord, is_fly=False):
        self.field = field
        self.x_coord = x_coord
        self.y_coord = y_coord
        if is_fly:
            self.speed = 1.2
        else:
            self.speed = 0.5

    def move(self, direction):

        if direction == 'UP':
                new_y = self.y_coord + self.speed
                new_x = self.x_coord
        elif direction == 'DOWN':
                new_y = self.y_coord - self.speed
                new_x = self.x_coord
        elif direction == 'LEFT':
                new_y = self.y_coord
                new_x = self.x_coord - self.speed
        elif direction == 'RIGTH':
                new_y = self.y_coord
                new_x = self.x_coord + self.speed

        self.field.set_unit(x=new_x, y=new_y, unit=self)

