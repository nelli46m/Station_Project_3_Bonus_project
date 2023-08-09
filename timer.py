import time

def format_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

def countdown_timer(seconds):
    while seconds > 0:
        print(format_time(seconds))
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

def main():
    try:
        time_str = input("Enter the countdown time (hh:mm:ss): ")
        hours, minutes, seconds = map(int, time_str.split(":"))
        total_seconds = hours * 3600 + minutes * 60 + seconds
        countdown_timer(total_seconds)
    except ValueError:
        print("Invalid input. Please enter a valid time in the format hh:mm:ss.")

if __name__ == "__main__":
    main()

