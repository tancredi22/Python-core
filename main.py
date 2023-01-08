class TimeInterval:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __add_sub(self, other, operation_type):
        own = self.hours * 3600 + self.minutes * 60 + self.seconds
        another = other.hours * 3600 + other.minutes * 60 + other.seconds

        if operation_type == 'subtraction':
            new_time = own - another
        elif operation_type == 'addition':
            new_time = own + another
        else:
            raise Exception('Unknown operation')

        new_hours = new_time // 3600
        new_minutes = (new_time % 3600) // 60
        new_seconds = new_time % 60

        return TimeInterval(hours=new_hours, minutes=new_minutes, seconds=new_seconds)

    def __add__(self, other):
        if isinstance(other, TimeInterval):
            return self.__add_sub(other, 'addition')
        else:
            raise TypeError('can only add TimeInterval objects')

    def __sub__(self, other):
        if isinstance(other, TimeInterval):
            return self.__add_sub(other, 'subtraction')
        else:
            raise TypeError('can only subtract TimeInterval objects')

    def __mul__(self, other):
        if isinstance(other, int):
            new_time = (self.hours * 3600 + self.minutes * 60 + self.seconds) * other
            new_hours = new_time // 3600
            new_minutes = (new_time % 3600) // 60
            new_seconds = new_time % 60
            return TimeInterval(hours=new_hours, minutes=new_minutes, seconds=new_seconds)
        else:
            raise TypeError('can only multiply TimeInterval objects by integers')

    def __str__(self):
        return "%s:%s:%s" % (self.hours, self.minutes, self.seconds)
t1 = TimeInterval(hours=21, minutes=58, seconds=50)
t2 = TimeInterval(1, 45, 22)

assert str(t1 + t2) == '23:44:12'
assert str(t1 - t2) == '20:13:28'
assert str(t1 * 2) == '43:57:40'

print('It works like a charm')
