import random
import string

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "`!@#$%^&*(){}[]\/<>"

string = lower + upper + number + symbols
length = 10
password = "".join(random.sample(string, length))

print("Your new Password is\n→ " + password)
