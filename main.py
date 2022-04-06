import pywhatkit
import datetime
import sys
hours = datetime.datetime.now().hour
minutes = datetime.datetime.now().minute + 1
# message = sys.argv[1]
# print(message)
with open('message.txt') as f:
    message = str(f.readlines()[0])

print(message)
print(type(message))

test = "Test From Python"
pywhatkit.sendwhatmsg_to_group("HOYGYfwPu15H9ElvMqXUSJ", message, hours, minutes)


