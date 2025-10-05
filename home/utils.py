from datetime import datetime, time
def is_restaurantopen():
    now = datetime.now()
    current_day = now.weekday()
    currrent_time = now.time()
    if current_day < 5:
        open_time = time(9, 0)
        close_time = time(22, 0)
    else:
        open_time = time(10, 0)
        close_time = time(23, 0)

    return open_time <= currrent_time <= close_time