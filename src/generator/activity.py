from dataclasses import dataclass
from datetime import datetime
from enum import Enum

class ActivityType(str, Enum):
    WORKOUT = "WORKOUT"
    SWIM = "SWIM"
    RUN = "RUN"

@dataclass
class Activity:
    activity_type: ActivityType
    person: str 
    start_time: datetime 
    end_time: datetime
    calories: int
    intensity: int
    distance: float
    avg_pace: float
