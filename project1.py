def drawTable(stats, names):
    out = ""
    c = 0
    num = 0
    counter = []
    #runs through header of stats to be displayed
    for item in names[0:7]:
        count = 0
        for i in item:
            count += 1
        out += "| " + '{:>{}s}'.format(str(item), count) + " "
        counter.append(count)
    out += "|\n"
    #line seperator between the headers and stats
    for i in names[0:7]:
        num = len(i) + 3
        j = 0
        while j < num:
            out += "-"
            j += 1
    out += "\n"

    #actual stats to be displayed corresponding to the headers above
    for item in stats[0:7]:
        out += "| " + '{:>{}s}'.format(str(item), counter[c]) + " "
        c += 1

    out += "|\n\n"

    #second set of headers to be displayed
    for item in names[7:]:
        count = 0
        for i in item:
            count += 1
        out += "| " + '{:>{}s}'.format(str(item), count) + " "
        counter.append(count)
    out += "|\n"
    #line seperator between the headers and stats
    for i in names[7:]:
        num = len(i) + 3
        j = 0
        while j < num:
            out += "-"
            j += 1
    out += "\n"

    #second set of stats to be displayed
    for item in stats[7:]:
        out += "| " + '{:>{}s}'.format(str(item), counter[c]) + " "
        c += 1

    out += "|\n"

    #returns table to be printed
    return out

name = str(input("Please enter Player's Name: "))
sets = 6
#checks to see how many sets player played in a match (used for calculations)
#cant have played more than 5 sets in a single match
while sets > 5:
    sets = int(input("Enter the sets they played: "))
    if sets > 5:
        print("\nInvalid Game Stat! Try Again!")
#offensive stats to be input by the user
statsO = ["attempts", "kills", "errors", "assists", "serves", 
           "aces", "service errors"]
#defensive stats to be input by the user
statsD = ["block assists", "block solo", "digs", "ball handeling errors",
          "zero pass", "one pass", "two pass", "three pass"]
#lists of actual stats from the player in the match
statO = []
statD = []
for item in statsO:
    statO.append(int(input("How many " + item + ": ")))
for item in statsD:
    statD.append(int(input("How many " + item + ": ")))

#calculations for offense start here
statO.insert(3, '{0:.3f}'.format((statO[1] - statO[2]) / statO[0]))
statsO.insert(3, "hitting percentage")
statO.insert(4, '{0:.3f}'.format((statO[1] / statO[0])))
statsO.insert(4, "kill percentage")
statO.insert(5, (statO[1] / sets))
statsO.insert(5, "kills per set")
statO.insert(7, (statO[6] / sets))
statsO.insert(7, "assists per set")
statO.insert(11, (statO[9] / sets))
statsO.insert(11, "aces per set")
statO.insert(12, '{0:.3f}'.format((statO[9] / statO[8])))
statsO.insert(12, "ace percentage")
statO.insert(13, '{0:.3f}'.format(((statO[8] - statO[10]) / statO[8])))
statsO.insert(13, "serve percentage")

#calculations for defense start here
total = statD[4] + statD[5] + statD[6] + statD[7]
statD.insert(2, (((statD[0] * 0.5) + statD[1]) / sets))
statsD.insert(2, "blocks per set")
statD.insert(4, (statD[3] / sets))
statsD.insert(4, "digs per set")
if total == 0:
    statD.insert(7, '{0:.3f}'.format(0))
else:
    statD.insert(7, '{0:.3f}'.format((statD[6] / total)))
statsD.insert(7, "zero pass percentage")
if total == 0:
    statD.insert(9, '{0:.3f}'.format(0))
else:
    statD.insert(9, '{0:.3f}'.format((statD[8] / total)))
statsD.insert(9, "one pass percentage")
if total == 0:
    statD.insert(11, '{0:.3f}'.format(0))
else:
    statD.insert(11, '{0:.3f}'.format((statD[10] / total)))
statsD.insert(11, "two pass percentage")
if total == 0:
    statD.insert(13, '{0:.3f}'.format(0))
else:
    statD.insert(13, '{0:.3f}'.format((statD[12] / total)))
statsD.insert(13, "perfect pass percentage")

#final output of all stats by player
print("\nPlayer: " + name + "\nSets Played: " + sets + "\n")
print("\nOffensive Stats:\n")
print(drawTable(statO, statsO))
print("\nDefensive Stats:\n")
print(drawTable(statD, statsD))
