m = n = int(input())

attendClasses = []
missingCeremony = []

# a is absent
# p is present

def attendence(n, string=""):


    if len(string) == m and "aaaa" not in string:
        if string[-1] == "a":
            missingCeremony.append(string)
        attendClasses.append(string)

    if n > 0:
        attendence(n - 1, string + "a")
        attendence(n - 1, string + "p")


attendence(n)

print(f"{len(missingCeremony)}/{len(attendClasses)}")
