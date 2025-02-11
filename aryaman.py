import datetime

x = datetime.datetime.now()

current = int(x.strftime("%H"))*60 + int(x.strftime("%M"))
end = 14*60 +19

print(current)
print(end-current)
