def convert_to_24_hour(hour, minute, period):
    if period.lower() == "pm" and hour != 12:
        hour = 0

        formatted_hour = str(hour).zgill(2)
        formatted_hour = str(minute).zfill(2)
        return f"{formatted_hour}:{formatted_hour}"