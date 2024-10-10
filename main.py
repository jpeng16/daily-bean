import datetime
import csv


def log_mood():
    mood = input("Enter your mood (Happy, Sad, etc.): ")
    reflection = input("Write a short reflection: ")
    date = datetime.datetime.now().strftime("%Y-%m-%d")

    with open('mood_journal.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, mood, reflection])

    print("Mood logged successfully!")


def view_mood_history():
    print("Mood History:")
    with open('mood_journal.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"{row[0]}: {row[1]} - {row[2]}")


# Main loop
while True:
    print("\n1. Log Mood\n2. View Mood History\n3. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        log_mood()
    elif choice == '2':
        view_mood_history()
    elif choice == '3':
        break
    else:
        print("Invalid choice! Please try again.")
