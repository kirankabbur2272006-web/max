import sys

if len(sys.argv) > 1:
    scores = [int(x) for x in sys.argv[1:]]
    print("User provided scores:", scores)
else:
    print("No input provided – using default values")
    scores = [50, 60, 70, 80, 90]


total = sum(scores)
average = total / len(scores)
maximum = max(scores)
minimum = min(scores)

print("Sum of scores:", total)
print("Average of scores:", average)
print("Maximum score:", maximum)
print("Minimum score:", minimum)