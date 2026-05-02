distance = 8

if distance < 3:
    transport = "walk"
elif distance < 15:
    transport = "bike"
else:
    transport = "car"


printZ("recommends you the transport of :", transport)