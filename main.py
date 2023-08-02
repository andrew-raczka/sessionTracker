from pymongo import MongoClient
import datetime
import pprint

client = MongoClient("localhost", 27017)
db = client.sessionTracker

# get the e1rm % from the database for the given reps & rpe
def getModifier(reps, rpe):
    collection = db.rpe
    pipeline = [
        {
            '$match': {
                'rpe': rpe, 
                'reps': reps
            }
        }, 
        {
            '$project': {
                'modifier': 1,
                '_id': 0
            }
        }
    ]
    result = collection.aggregate(pipeline)
    return result

def calcTonnage(reps, weight):
    tonnage = reps * weight
    return tonnage

# workout = {
#     "exercise": "comp bench",
#     "date": datetime.datetime.now(tz=datetime.timezone.utc),
#     "sets": [
#         {
#             "reps": 1,
#             "weight": 260,
#             "rpe": 7
#         },
#         {
#             "reps": 5,
#             "weight": 225,
#             "rpe": 6
#         }
#     ]
# }

# for i in workout["sets"]:
#     # go to the database and get the modifier for the rpe/rep combo
#     modifier = getModifier(i["reps"], i["rpe"])
#     for m in modifier:
#         e1rm = i["weight"] / m['modifier']
#         i["e1rm"] = round(e1rm,2)

# collection = db.workouts
# workout_id = collection.insert_one(workout)

sets = [
    {
    "exercise": "comp bench",
    "date": datetime.datetime.now(tz=datetime.timezone.utc),
    "reps": 1,
    "weight": 260,
    "rpe": 7,
    "category": "horizontal push"
    },
    {
    "exercise": "comp bench",
    "date": datetime.datetime.now(tz=datetime.timezone.utc),
    "reps": 5,
    "weight": 225,
    "rpe": 6,
    "category": "horizontal push"
    },
    {
    "exercise": "comp bench",
    "date": datetime.datetime.now(tz=datetime.timezone.utc),
    "reps": 5,
    "weight": 225,
    "rpe": 7,
    "category": "horizontal push"
    },
    {
    "exercise": "comp bench",
    "date": datetime.datetime.now(tz=datetime.timezone.utc),
    "reps": 5,
    "weight": 225,
    "rpe": 8,
    "category": "horizontal push"
    },
    {
    "exercise": "incline bench",
    "date": datetime.datetime.now(tz=datetime.timezone.utc),
    "reps": 5,
    "weight": 150,
    "rpe": 6,
    "category": "horizontal push"
    },
    {
    "exercise": "incline bench",
    "date": datetime.datetime.now(tz=datetime.timezone.utc),
    "reps": 5,
    "weight": 150,
    "rpe": 6,
    "category": "horizontal push"
    },
    {
    "exercise": "incline bench",
    "date": datetime.datetime.now(tz=datetime.timezone.utc),
    "reps": 5,
    "weight": 150,
    "rpe": 6,
    "category": "horizontal push"
    }
]

for s in sets:
    # go to the database and get the modifier for the rpe/rep combo
    modifier = getModifier(s["reps"], s["rpe"])
    for m in modifier:
        e1rm = s["weight"] / m['modifier']
        s["e1rm"] = round(e1rm,2)
    tonnage = calcTonnage(s["reps"],s["weight"])
    s["tonnage"] = tonnage

collection = db.workouts
workout_id = collection.insert_many(sets)
