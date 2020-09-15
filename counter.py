class Duration:
    def __init__(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

    def add(self, time):
        time, ms = time.split('.')
        hour, minutes, seconds = time.split(':')
        self.hours += int(hour)
        self.minutes += int(minutes)
        self.seconds += int(seconds)

    @property
    def duration(self):
        overflow_minutes, new_seconds = divmod(self.seconds, 60)
        self.seconds = new_seconds
        self.minutes += overflow_minutes

        overflow_hours, new_minutes = divmod(self.minutes, 60)
        self.minutes = new_minutes
        self.hours += overflow_hours

        return (self.hours, self.minutes, self.seconds)


with open('./output.txt') as f:
    duration = Duration()
    for line in f:
        duration.add(line.strip('\n'))

    print(duration.duration)
