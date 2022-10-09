import calendar

if __name__ == '__main__':
    month, day, year = input().split()
    c = calendar.weekday(int(year), int(month), int(day))
    print((calendar.day_name[int(c)]).upper())
