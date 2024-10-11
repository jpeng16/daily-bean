import json
from datetime import datetime


class DailyBean:
    def __init__(self, filename='daily_bean_data.json'):
        self.filename = filename
        self.load_moods()

    def load_moods(self):
        """Load mood data from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                self.moods = json.load(file)
        except FileNotFoundError:
            self.moods = []

    def save_moods(self):
        """Save mood data to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(self.moods, file, indent=4)

    def add_mood(self, mood, description):
        """Add a mood and description to the tracker."""
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.moods.append({'date': date, 'mood': mood, 'description': description})
        self.save_moods()
        print(f"Mood '{mood}' recorded on {date} with description: '{description}'.")

    def view_moods(self):
        """View all recorded moods."""
        if not self.moods:
            print("No moods recorded yet.")
            return

        print("\nMood History:")
        for entry in self.moods:
            print(f"{entry['date']}: {entry['mood']} - {entry['description']}")


def main():
    tracker = DailyBean()

    while True:
        print("\nWelcome to Daily Bean!")
        print("1. Add Mood")
        print("2. View Moods")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            mood = input("Enter your mood (e.g., Happy, Sad, Angry): ")
            description = input("Enter a short description: ")
            tracker.add_mood(mood, description)
        elif choice == '2':
            tracker.view_moods()
        elif choice == '3':
            print("Exiting Daily Bean. Take care!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
