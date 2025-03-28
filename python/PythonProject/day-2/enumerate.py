# We can use enumerate on String, List, Tuple or any kind of iterable
# It by default start from 0, we can start it from any number

for index, char in enumerate("smruti"):
    print(f"{index} - {char}")

for index, char in enumerate("smruti", 10):
    print(f"{index} - {char}")