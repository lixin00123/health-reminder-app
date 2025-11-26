import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from storage import Storage
from reminders import Reminder
import os


def test_integration_add_and_load():
    test_file = "test_reminders.json"

    # Clean previous tests file
    if os.path.exists(test_file):
        os.remove(test_file)

    storage = Storage(test_file)

    r = Reminder("Drink water", "10:00")
    reminders = [{
        "title": r.title,
        "time": r.time_str,
        "repeat": r.repeat
    }]

    storage.save(reminders)

    loaded = storage.load()

    assert loaded[0]["title"] == "Drink water"

    os.remove(test_file)
