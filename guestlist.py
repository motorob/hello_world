guestlist = ['Jimi', 'Sandy', 'Camilla']
print(guestlist)

for guest in guestlist:
    #print(guest)
    print(f"Hello {guest.title()}!  You wanna come over for a party!.")

cantmakeit = "Jimi"
print(cantmakeit)
guestlist.remove('Jimi')
print(guestlist)
print(f"\n{cantmakeit}!  So sorry you can't make it!  Hopefully we can get together soon!")

guestlist.append("PG")
print(guestlist)

newguest = "PG"
if newguest in (guestlist):
    #print(newguest)
    print (f"Hello {newguest.upper()}!  You wanna come over for a party!.")

for guest in guestlist:
    print(f"Hello {guest}!  Great news!  We found more space!  More to come!")

guestlist.insert(0, "Kelly")
guestlist.insert(3, "Anais")
guestlist.append("henry")
print(guestlist)

for guest in guestlist:
    #print(guest)
    print(f"Hello {guest.title()}!  Here are the revised invites!  Looking forward to seeing everyone!")

for guest in guestlist:
    #print(guest)
    print(f"Uh oh! Well, {guest.title()}, looks like we goofed!  Have to univite everyone but two.  So's!")

i = 0
while i < len(guestlist)+2:
    #print("this is working")
    disinvited = guestlist.pop()
    print(f"Sorry, {disinvited}, we have to dis-invite you!  Hope to catch up soon!")
    print(guestlist)
    i = i + 1

for guest in guestlist:
 print(f"{guest.title()}, looks like it's just us!")



i = -1
while i < len(guestlist):
    for guest in guestlist:
        del guestlist[0]
    print(f"{guest}, looks like the party is cancelled.  :(")
    i = i + 1


print(guestlist)