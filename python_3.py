instagram = {}
while True:
choice = int(input("enter your choice"))
if choice ==2:
    user=input("enter username")
    if user in instagram:
         del user[instagram]
    print("username deleted")
else:
        ("username not found enter valid username")
