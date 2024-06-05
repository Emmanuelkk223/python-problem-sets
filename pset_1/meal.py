def main():
    breakfast = 7.0
    end_breakfast = 8.0
    launch = 12.0 
    end_launch = 13.0
    dinner = 18.00 
    end_dinner = 17.0
    ask_time = input("What time is it? ")
    ask_time = convert(ask_time)
    if breakfast <= ask_time < end_breakfast:
        print("breakfast time")
    elif launch <= ask_time < end_launch:
        print("Launch time")
    elif dinner <= ask_time < end_dinner:
        print("Dinner time")


def convert(time):
    hour, minute = time.split(":")
    hour = int(hour)
    minute = int(minute)
    total_hour = hour + minute / 60
    return total_hour


if __name__ == "__main__":
    main()
