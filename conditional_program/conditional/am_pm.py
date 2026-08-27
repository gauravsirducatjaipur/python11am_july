time = int(input("Enter the time in hours 24 format "))

if time>0 and time<=24:
  pass
else:
  pass


if time>0 and time<=24:
  print("hi")
else:
  print("bye")


if time>0 and time<=24:
  if time>=1 and time<=12:
    print("AM")
  else:
    print("PM")
else:
  print("bye")


if time>0 and time<=24:
  if time<=12:
    print("AM")
  else:
    print("PM")
else:
  print("bye")


# if time>=1 and time<=24:
#   pass
# else:
#   pass


if time>=1 and time<=24:
  if time>12:
    print("PM")
  else:
    print("AM")
else:
  print("Bye")


if time>=1 and time<=24:
  if time<=12:
    print("AM")
  else:
    print("PM")
else:
  print("bye")


if time>=1 and time<=12:
  print("AM")
elif time>=13 and time<=24:
  print("PM")
else:
  print("bye")



if (time <= 24 and time > 0):  
  if (time >= 12):
    print("PM")
  else:
    print("AM")
else:
  print("Invalid range")