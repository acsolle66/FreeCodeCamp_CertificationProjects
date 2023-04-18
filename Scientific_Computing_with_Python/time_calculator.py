def time_calculator(*args):
    start_time = (args[0].split(" "))[0]
    duration_time = args[1]
    try:
        starting_day = (args[2]).lower()
    except:
        starting_day = False

    MINS_IN_HOUR = 60
    TIME_FORMAT = 720  # 12 hours multiplied by 60 minutes
    WEEKDAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

    start_time_hour = int((start_time.split(":"))[0])
    start_time_min = int((start_time.split(":"))[1])
    start_time_total = (start_time_hour * MINS_IN_HOUR) + start_time_min  # total start time in minutes
    start_time_suffix = (args[0].split(" "))[1]

    duration_time_hour = int((duration_time.split(":"))[0])
    duration_time_min = int((duration_time.split(":"))[1])
    duration_time_total = (duration_time_hour * MINS_IN_HOUR) + duration_time_min  # total duration time in minutes

    result_time_total = start_time_total + duration_time_total
    result_time = result_time_total
    result_time_suffix = start_time_suffix

    if result_time > TIME_FORMAT:
        day_counter = 0
        time_counter = 0
        while result_time > TIME_FORMAT:
            result_time = result_time - TIME_FORMAT
            time_counter += 1
            result_time_hour = int(result_time/MINS_IN_HOUR)
            result_time_min = result_time_total - (result_time_hour * MINS_IN_HOUR) - (time_counter * TIME_FORMAT)
            if result_time_suffix == "PM":
                result_time_suffix = "AM"
                day_counter += 1
            elif result_time_suffix == "AM":
                result_time_suffix = "PM"
        if starting_day:
            starting_day_index = WEEKDAYS.index(starting_day)
            day_count = starting_day_index + day_counter
            if day_count > 6:
                while day_count > 6:
                    day_count = day_count - 7
                result_day = WEEKDAYS[day_count]
            else:
                result_day = WEEKDAYS[day_count]
    else:
        result_time_hour = int(result_time/MINS_IN_HOUR)
        result_time_min = result_time_total - (result_time_hour * MINS_IN_HOUR)
        result_time_suffix = start_time_suffix
        result_day = starting_day
        day_counter = 0

    if result_time_hour == 0:
        result_time_hour = str(12)
    else:
        result_time_hour = str(result_time_hour)

    if len(str(result_time_min)) == 1:
        result_time_min = f"0{result_time_min}"
    else:
        result_time_min = str(result_time_min)

    final_time_string = ":".join([result_time_hour, result_time_min])
    final_time_string_with_suffix = " ".join([final_time_string, result_time_suffix])

    if starting_day:
        final_time_with_day = ", ".join([final_time_string_with_suffix, result_day.capitalize()])
        if day_counter > 1:
            return " ".join([final_time_with_day, f"({day_counter} days later)"])
        elif day_counter == 1:
            return " ".join([final_time_with_day, "(next day)"])
        else:
            return final_time_with_day
    elif starting_day is False:
        if day_counter > 1:
            return " ".join([final_time_string_with_suffix, f"({day_counter} days later)"])
        elif day_counter == 1:
            return " ".join([final_time_string_with_suffix, "(next day)"])
        else:
            return final_time_string_with_suffix
