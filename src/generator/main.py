import random, json, dataclasses, time
from activity import Activity, ActivityType
from redis import Redis
from datetime import datetime, timedelta
from sample_data import (
    SAMPLE_START_TIMES,
    PACE_RANGES_MIN_PER_KM,
    DISTANCE_RANGES_KM,
    WORKOUT_DURATION_RANGE_MIN,
    CALORIE_RATE_PER_MIN,
)


def build_activity(start_time: datetime) -> Activity:
    activity_type = random.choice(list(ActivityType))
    intensity = random.randint(1, 10)

    if activity_type == ActivityType.WORKOUT:
        distance, avg_pace = None, None
        duration_minutes = random.uniform(*WORKOUT_DURATION_RANGE_MIN)
    else:
        distance = round(random.uniform(*DISTANCE_RANGES_KM[activity_type]), 2)
        avg_pace = round(random.uniform(*PACE_RANGES_MIN_PER_KM[activity_type]), 2)
        duration_minutes = distance * avg_pace

    end_time = start_time + timedelta(minutes=duration_minutes)

    # calories scale with session length and how hard it felt (intensity 1-10)
    calorie_rate = random.uniform(*CALORIE_RATE_PER_MIN[activity_type])
    calories = round(duration_minutes * calorie_rate * (intensity / 5))

    return Activity(activity_type,
                    "João Vitor",
                    start_time,
                    end_time,
                    calories,
                    intensity,
                    distance,
                    avg_pace)

def to_json(a: Activity) -> str:
    a_dict = dataclasses.asdict(a)
    a_dict["start_time"] = a_dict["start_time"].isoformat()
    a_dict["end_time"] = a_dict["end_time"].isoformat()
    a_json = json.dumps(a_dict)
    return a_json

if __name__ == "__main__":
    r = Redis(host='localhost', port=6379, decode_responses=True)    
    for day in SAMPLE_START_TIMES:
        r.xadd("activities", {"payload": to_json(build_activity(day))})   
    print(r.xlen("activities"))
    r.close()
    