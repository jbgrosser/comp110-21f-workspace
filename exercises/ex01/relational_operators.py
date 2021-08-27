"""Compares two numerical variables and returns resulting bool."""

__author__ = "730475279"

left: str = input("Left-hand side: ")
right: str = input("Right-hand side: ")
left_integer: int = int(left)
right_integer: int = int(right)
print(left + " < " + right + " is " + str(left_integer < right_integer))
print(left + " >= " + right + " is " + str(left_integer >= right_integer))
print(left + " == " + right + " is " + str(left_integer == right_integer))
print(left + " != " + right + " is " + str(left != right))