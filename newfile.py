#VEHICLE PARKING LOG SYSTEM

import time
parkingslot = {}
maxslots = 5

while True:
    print("[=== VEHICLE PARKING LOG SYSTEM ===]")
    print("1. Park Vehicle")
    print("2. Remove Vehicle")
    print("3. View Parked Vehicles")
    print("4. Exit")
    
    choice = int(input("Choice (1-4): "))

    if choice == 1:
        if len(parkingslot) >= maxslots:
            print("Full! Come back later!")
        else:
            plate = input("Enter Plate No.: ")
            if plate in parkingslot:
                print("Already parked!")
            else:
                parkingslot[plate] = time.strftime("%Y-%m-%d %H:%M:%S")
                print(f"Parked at {parkingslot[plate]}")
               

    elif choice == 2:
        if not parkingslot:
            print("No Vehicle yet!")
        else:
            plate = input("Enter Plate No. to remove: ")
            if plate in parkingslot:
                time_out = time.strftime("%Y-%m-%d %H:%M:%S")
                print(f"Removed!\nIn: {parkingslot[plate]}\nOut: {time_out}")
                del parkingslot[plate]
            else:
                print("Not found.")

    elif choice == 3:
        if not parkingslot:
            print("No Vehicle Park yet")
        else:
            print("[--- Parked ---]")
            for i, (p, t) in enumerate(parkingslot.items(), 1):
                print(f"{i}. {p} | {t}")

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid!")