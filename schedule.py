import time
from .utils.check_time import check_time

def schedule(start, end, function):
    active = True

    while True:
        if check_time(start, end):
            if not active: 
                print(f"""
                    [{time.strftime('%Y-%m-%d %H:%M')}] Scheduled task is now
                    active and will end at {end} PST.""")

                active = True

            function()

        else:
            if active:
                print(f"""
                    [{time.strftime('%Y-%m-%d %H:%M')}] Scheduled task is now
                    inactive and will resume at {start} PST.""")

                active = False

        time.sleep(5)