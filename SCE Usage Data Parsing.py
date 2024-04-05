
#this is parse the client's usage data from SCE

def seperateByDay():
    print("hello")
    data = open("UsageData.csv", "r")

#making a list of each day to index from later
#using lists because dictionaries would have repeated entries for the same date
    recording = []
    ##measurements = []
    for line in data:
        line = line.strip()
        min15 = line.split(",")
        clock = min15[0]
        ##energy = min15[1]
        recording.append(clock)
        ##measurements.append(energy)

#separating the time out
    mDate = []
    for entry in recording:
        entry = entry.split(" ")
        day = entry[0]
        mDate.append(day)

    i = 0
    list = []

#attempt to isolate days and cancel duplicates
    for post in mDate:
        post = post.strip()
        fetcha = post.split("-")
        number = fetcha[0]
        list.append(number)


    data.close()
    return list




def seperateByHour():
    print("hello")

def main():
    test = seperateByDay()
    print(test)

main()

