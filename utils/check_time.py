from datetime import datetime

def check_time(start, end):
    new_time = str(datetime.now().time()).split(':')
    current  = int(new_time[0] + new_time[1])

    if start < end: return True if current > start and current < end else False
    else:           return True if current < start and current > end else False