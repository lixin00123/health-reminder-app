import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from reminders import Reminder

def test_next_trigger_time():
    r = Reminder("Test", "23:59")
    t = r.get_next_trigger_time()

    assert t.hour == 23
    assert t.minute == 59
