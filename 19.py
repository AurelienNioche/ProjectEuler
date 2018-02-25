import numpy as np


class Calendar(object):

    thirty_days = [9, 4, 6, 11]
    thirty_one_days = [1, 3, 5, 7, 8, 10, 12]

    def __init__(self):
        self.week_day, self.day, self.month, self.year = 1, 1, 1, 1900
        self.leap = None

        self.have_to_count = False

        self.stop = False

        self.counter = 0

    def change_month(self):

        self.month += 1
        self.day = 1

    def change_year(self):

        if self.year == 2000:

            self.stop = True
            return

        self.year += 1
        self.month = 1
        self.day = 1

        if self.year == 1901:

            self.have_to_count = True

        self.check_leap()

    def check_leap(self):

        if self.year % 100 == 0:
            if self.year % 400 == 0:
                self.leap = True
            else:
                self.leap = False

        elif self.year % 4 == 0:
            self.leap = True

        else:
            self.leap = False

    def change_week_day(self):

        self.week_day += 1

        if self.week_day == 8:
            self.week_day = 1

    def make_count(self):

        if self.day == 1 and self.week_day == 7:

            self.counter += 1

    def update(self):

        if self.month == 12 and self.day == 31:
            self.change_year()

        elif self.day == 31 and self.month in self.thirty_one_days:

            self.change_month()

        elif self.day == 30 and self.month in self.thirty_days:

            self.change_month()

        elif self.day == 28 and self.month == 2 and self.leap is False:

            self.change_month()

        elif self.day == 29 and self.month == 2 and self.leap is True:

            self.change_month()

        else:
            self.day += 1

        self.change_week_day()

    def run(self):

        self.check_leap()

        while not self.stop:
            if self.have_to_count:
                self.make_count()
            self.update()
            print(self.year, self.month, self.day, self.week_day)
            if self.day > 31:
                print(self.leap)
                raise Exception

        return self.counter


c = Calendar()
print(c.run())