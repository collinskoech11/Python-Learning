#this is a simple trip planner
def Planner():
    speed = 30
    distance = 600
    time = (distance/speed)
    return time

print('you arive at your destination  within' + Planner())