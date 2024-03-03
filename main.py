from datetime import datetime, timedelta

class SimpleCalendar:
    def __init__(self):
        self.events = {}

    def add_event(self, date, event):
        """Lägger till en händelse på ett specifikt datum."""
        if date in self.events:
            self.events[date].append(event)
        else:
            self.events[date] = [event]

    def remove_event(self, date, event):
        """Tar bort en specifik händelse på ett datum."""
        if date in self.events and event in self.events[date]:
            self.events[date].remove(event)
            if not self.events[date]:
                del self.events[date]

    def get_events(self, month):
        """Returnerar alla händelser för en specifik månad."""
        for date in sorted(self.events):
            if date.month == month:
                for event in self.events[date]:
                    print(f"{date.strftime('%Y-%m-%d')}: {event}")

    def check_reminders(self):
        """Visar påminnelser för händelser som är nära i tid."""
        today = datetime.now()
        for date in self.events:
            if 0 <= (date - today).days < 3:  # Påminn 3 dagar innan
                for event in self.events[date]:
                    print(f"Påminnelse: {event} på {date.strftime('%Y-%m-%d')}")

# Exempel på hur man använder klassen
if __name__ == "__main__":
    calendar = SimpleCalendar()
    event_date = datetime(2024, 3, 10)  # Exempeldatum
    calendar.add_event(event_date, "Möte med teamet")
    calendar.check_reminders()
    calendar.get_events(3)  # Visa händelser för Mars
