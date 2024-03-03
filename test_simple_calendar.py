import unittest
from main import SimpleCalendar
from datetime import datetime

class TestSimpleCalendar(unittest.TestCase):
    def setUp(self):
        self.calendar = SimpleCalendar()

    def test_add_event(self):
        event_date = datetime(2024, 3, 10)
        self.calendar.add_event(event_date, "Testevent")
        self.assertIn(event_date, self.calendar.events)
        self.assertIn("Testevent", self.calendar.events[event_date])

    def test_remove_event(self):
        event_date = datetime(2024, 3, 10)
        self.calendar.add_event(event_date, "Testevent")
        self.calendar.remove_event(event_date, "Testevent")
        self.assertNotIn("Testevent", self.calendar.events.get(event_date, []))

    def test_get_events(self):
        # Detta test kan kräva lite mer arbete för att korrekt verifiera utskrifter eller hantera datumen dynamiskt.
        pass

    def test_check_reminders(self):
        # Liksom test_get_events kan detta test behöva anpassas för att hantera dynamiska datum och kontrollera utskrifter.
        pass

if __name__ == '__main__':
    unittest.main()
