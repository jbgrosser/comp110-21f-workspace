"""Repeating a beat in a loop."""

__author__ = "730475279"


# Begin your solution here...
beat: str = input("What beat do you want to repeat? ")
repeat: int = int(input("How many times do you want to repeat it? "))
i: int = 0
final_string: str = ""
while i < repeat:
    i = i + 1
    if i == 1:
        final_string = beat
    else:
        final_string = final_string + " " + beat
if repeat <= 0:
    print("No beat...")
else:
    print(final_string)