import json
import os

class Storage:
    def __init__(self, filename="reminders.json"):
        self.filename = filename

        # 如果文件不存在，创建一个空数组文件
        if not os.path.exists(filename):
            with open(filename, "w") as f:
                json.dump([], f)

    def load(self):
        """读取 reminders.json 中的提醒内容"""
        with open(self.filename, "r") as f:
            return json.load(f)

    def save(self, reminders):
        """写入 reminders.json"""
        with open(self.filename, "w") as f:
            json.dump(reminders, f, indent=2)
