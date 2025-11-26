import datetime


class Reminder:
    def __init__(self, title, time_str, repeat="daily"):
        self.title = title
        self.time_str = time_str
        self.repeat = repeat

    def get_next_trigger_time(self):
        """
        根据 HH:MM 字符串计算下一次提醒时间。
        如果今天已过，则顺延到明天。
        """
        now = datetime.datetime.now()
        hour, minute = map(int, self.time_str.split(":"))

        reminder_time = now.replace(hour=hour, minute=minute,
                                    second=0, microsecond=0)

        if reminder_time < now:
            reminder_time += datetime.timedelta(days=1)

        return reminder_time

    def __repr__(self):
        return f"Reminder({self.title}, {self.time_str}, repeat={self.repeat})"
