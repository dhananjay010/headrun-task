days = int(input())

attendClasses = []
missingCeremony = []

# a is absent
# p is present

def attendence(n, eachDay=""):

    if len(eachDay) == days and "aaaa" not in eachDay:
        if eachDay[-1] == "a":
            missingCeremony.append(eachDay)
        attendClasses.append(eachDay)

    if n > 0:
        attendence(n - 1, eachDay + "a")
        attendence(n - 1, eachDay + "p")

attendence(days)

print(f"{len(missingCeremony)}/{len(attendClasses)}")
