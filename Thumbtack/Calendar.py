# class Calendar:
'''
Design and implement a class that powers a simple calendar application. It should support the following:

Add one or more events
Delete a given event
Retrieve all events for a given day
'''
import uuid
from sortedcontainers import SortedDict
class Event:
    def __init__(self, event_name, event_content, start, end, date):
        self.start = start
        self.end = end
        self.date = date
        self.event_name = event_name
        self.event_content = event_content
        self.id = str(uuid.uuid1())
    def __str__(self):
        return "Event name {}, content{}, id{}, start:end {}, date{}".format(self.event_name,self.event_content
        ,self.id,(self.start,self.end), self.date)

class Calendar:
    def __init__(self):
        self.cal = [SortedDict() for _ in range(101)]
        self.eventMap = {}
    def add_event(self, event):
        # if multiple events have same start,end time
        # how the events be arranged?
        start, end = event.start, event.end
        date = event.date
        if (start, end) not in self.cal[date]:
            self.cal[date][(start, end)] = []
        self.cal[date][(start, end)].append(event)
        eid = event.id
        self.eventMap[eid] = event
    def remove_event(self, eid):
        event = self.eventMap[eid]
        date, start, end = event.date, event.start, event.end
        for i, e in enumerate(self.cal[date][(start, end)]):
            if eid == e.id:
                self.cal[date][(start, end)].pop(i)
                break
        del self.eventMap[eid]
    def get_events_of(self, date):
        return self.cal[date]
calendar = Calendar()

e1 = Event("a", "a", 1000, 1100, 1)
e2 = Event("b", "b", 1000, 1100, 1)
e3 = Event("d", "d", 1100, 1200, 1)
e4 = Event("c", "c", 1000, 1100, 2)
calendar.add_event(e1)
calendar.add_event(e2)
calendar.add_event(e3)
calendar.add_event(e4)
calendar.remove_event(e2.id)
sd = calendar.get_events_of(1)
for k in sd.keys():
    for e in sd[k]:
        print(e)
