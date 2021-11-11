import re


class Date():
    def __init__(self, date):
        if re.search("^(?:\d{1,2}[.]){2}\d{1,4}", date):
            self.date = date
        else:
            exit("Incorrect input")

    @classmethod
    def number_date(cls, date):
        numbered_date = [int(i) for i in date.split('.')]
        return numbered_date

    @staticmethod
    def validation(date):
        work_date = [int(i) for i in date.split('.')]
        day, month, year = work_date[0], work_date[1], work_date[2]

        #month check
        if month > 12 or month == 0:
            print("Incorrect month")
            return
        #day check
        if day > 31 or day == 0:
            print("Incorrect day")
            return

        #february check
        if (month == 2) and (day > 28) or (day == 0):
            print("Incorrect day")
            return
        elif (year // 4 == 0) and (month == 2) and (day > 29) or (day == 0):
            print("Incorrect day")
            return
        print("Correct date")