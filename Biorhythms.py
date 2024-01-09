def getNextLowAndHighPeak(remainder, daysInCycle, lowPeak, highPeak):
    if remainder > lowPeak: print(daysInCycle - remainder + lowPeak)
    else: print(lowPeak - remainder)
    if remainder > highPeak: print(daysInCycle - remainder + highPeak)
    else: print(highPeak - remainder)

print("Input:")

daysSinceBirth = int(input())

getNextLowAndHighPeak(daysSinceBirth % 23, 23, 6, 17)
getNextLowAndHighPeak(daysSinceBirth % 28, 28, 7, 21)
getNextLowAndHighPeak(daysSinceBirth % 33, 33, 8, 25)

