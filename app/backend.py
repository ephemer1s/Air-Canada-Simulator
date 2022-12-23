# import math
import time, datetime

import numpy as np

# from app.dataloader import FlightInfo, Announcement

class SITUATION_IDX():
    NORMAL = 0
    DELAYED = 1
    CANCELLED = 2
    
class REASON():
    OTHER = -1
    WEATHER = 0
    AIRCRAFT = 1
    SECURITY = 2
    OPERATION = 3
    
class MiscDict():
    Code2Name = {
        'YWG': 'Winnipeg',
        'YVR': 'Vancouver',
        'YYZ': 'Toronto',
        'YUL': 'Montreal',
        'YEG': 'Edmonton',
        'YOW': 'Ottawa',
        'YHZ': 'Halifax',
    }
    Name2Code = {
        'Winnipeg': 'YWG',
        'Vancouver': 'YVR',
        'Toronto': 'YYZ',
        'Montreal': 'YUL',
        'Edmonton': 'YEG',
        'Ottawa': 'YOW',
        'Halifax': 'YHZ',
    }

class FlightInfo():
    def __init__(self,
                 typeidx=SITUATION_IDX.NORMAL,
                 firstname='John',
                 lastname='Example',
                 flight='AC',
                 volume='299',
                 departure_code='YWG',
                 arrival_code='YVR',
                 std_boarding=None,
                 std_departure=None,
                 std_arrival=None,
                ):
        # arrange arguments to self
        self.typeidx = typeidx
        self.firstname = firstname
        self.lastname = lastname
        self.flight = flight
        self.volume = volume

        # maybe use a new structure
        self.departure_code = departure_code
        self.arrival_code = arrival_code

        # time
        if std_boarding is None:
            self.std_boarding = datetime.datetime(year=2020, month=1, day=1, hour=0, minute=0, second=0)
        else:
            self.std_boarding = std_boarding
            
        if std_departure is None:
            self.std_boarding = datetime.datetime(year=2020, month=1, day=1, hour=0, minute=0, second=0)
        else:
            self.std_departure = std_departure
            
        if std_arrival is None:
            self.std_boarding = datetime.datetime(year=2020, month=1, day=1, hour=0, minute=0, second=0)
        else:
            self.std_arrival = std_arrival
        
        # reserved for delay
        self.est_boarding = None
        self.est_departure = None
        self.est_arrival = None
        self.reason = None
        
        return
    
    def setDelayed(self, time, reason):
        self.est_boarding = time + self.std_boarding
        self.est_departure = time + self.std_departure
        self.est_arrival = time + self.std_arrival
        
        self.typeidx = SITUATION_IDX.DELAYED
        self.reason = reason
        
        return self
        
    
class Announcement(object):
    def __init__(self, info):
        if info.typeidx == SITUATION_IDX.DELAYED:
            self.title = f'Flight {info.flight}{info.volume} to {MiscDict.Code2Name[info.arrival_code]} is delayed'
            self.heading1 = f'Hello {info.firstname}, your flight is delayed and is now departing at {info.est_departure}. We apologize and are working to get you on your way.'
            self.context = self.get_context(info.reason)
        return 

    def get_context(self, reason):
        if reason == REASON.WEATHER:
            return 'The delay is due to weather.'
        elif reason == REASON.AIRCRAFT:
            return 'The delay is due to an aircraft issue.'
        elif reason == REASON.SECURITY:
            return 'The delay is due to a security issue.'
        elif reason == REASON.OPERATION:
            return 'This flight is delayed due to an operational issue from an earlier flight which is causing the aircraft that is scheduled to operate your flight to arrive late. An example of an operational issue could include scheduling conflicts, operational decisions or a connection delay. \n\n Situations surrounding flight disruptions can be complex and have multiple causes. We are required to inform you of the reason for a flight disruption. Please be aware that the reasons provided for a flight disruption may change as the situation evolves, new issues arise, or new information is received.'
        else:
            return 'The delay is due to an unknown issue.'
        

    def print(self):
        print(self.title)
        print(self.heading1)
        print(self.context)


def get_weighted_random_delay():
    ''''''    
    modifier = np.random.random(1)
    delay_minutes = np.random.randint(0, 59)
    delay_hours = 2147483647
    
    if modifier < 0.2:
        delay_hours = np.random.randint(0, 1)
    elif modifier < 0.5:
        delay_hours = np.random.randint(1, 3)
    elif modifier < 0.8:
        delay_hours = np.random.randint(3, 6)
    elif modifier < 0.9:
        delay_hours = np.random.randint(6, 24)
    elif modifier < 0.99:
        delay_hours = np.random.randint(24, 168)
    else:
        delay_hours = np.random.randint(168, delay_hours)

    return datetime.timedelta(hours=delay_hours, minutes=delay_minutes)



if __name__ == "__main__":
    example_flight = FlightInfo(
        firstname='Tsukihi',
        lastname='Fujiwara',
        std_boarding=datetime.datetime(year=2022, month=12, day=20, hour=16, minute=20, second=0),
        std_departure=datetime.datetime(year=2022, month=12, day=20, hour=16, minute=55, second=0),
        std_arrival=datetime.datetime(year=2022, month=12, day=20, hour=20, minute=18, second=0),
    )
    example_flight = example_flight.setDelayed(get_weighted_random_delay(), REASON.OPERATION)
    
    announcement = Announcement(example_flight)
    announcement.print()
    