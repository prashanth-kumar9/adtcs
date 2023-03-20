f = open("out1.txt", "r")
no_of_vehicles=[]

for data in f:
    no_of_vehicles.append(int(data))

baseTimer = 180  # each lane waiting time
timeLimits = [5, 60]  # time limit

print("Input no of vehicles : ", *no_of_vehicles)
t = [(i / sum(no_of_vehicles)) * baseTimer if timeLimits[0] < (i / sum(no_of_vehicles)) * baseTimer < timeLimits[1] 
else min(timeLimits, key=lambda x: abs(x - (i / sum(no_of_vehicles)) * baseTimer)) for i in no_of_vehicles]
r=[]
print(t)
def count():
    for i in range(len(t)):
        r1=t.index(max(t))
        r.append(r1+1)
        print("lane" + str(r1+1))
        t[r1]=0
    return r