def convert_to_24_hour(hour, minute, period):
    if period.lower() == "pm" and hour != 12:
        hour += 12
    elif period.lower() == "am" and hour == 12:
        hour = 0
    
    formatted_hour = str(hour).zfill(2)
    formatted_minute = str(minute).zfill(2)
    
    return f"{formatted_hour}:{formatted_minute}"
