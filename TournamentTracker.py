# %%
import time
import json

def sign_up(participants):
    
    print("Participant Sign Up")
    print("====================\n")

    while(True):

        print("please enter the the name of participant last and first with a comma: \n")
        time.sleep(1)
        name = input()

        if check(name,2):
            break

    
    while(True):

        print("please enter the slot for the participant: " + "1-" + str(len(participants)) + "\n")
        time.sleep(1)
        slot = input()

        if int(slot) >= len(participants)+1 or int(slot) <= 0:
            print("Thats not a vaild slot")
            continue

        if participants[slot] != None:
            print("Someone is in that spot silly")
            continue 

        if check(slot,1):
            break

    participants[slot] = name
    print("Success:")
    print(name + " is signed up in starting slot #" + slot)
    return participants

def cancel_sign_up(participants):

    print("Participant Cancellation")
    print("====================\n")

    while(True):

        print("please enter the the name of participant last and first with a comma: \n")
        time.sleep(1)
        name = input()

        if (name in participants.values()) == False:
            print("No one by that name is in the tournment\n")
            continue

        if check(name,2):
            break

    while(True):

        print("please enter the slot for the participant: " + "1-" + str(len(participants)))
        time.sleep(1)
        slot = input()

        if int(slot) >= len(participants)+1 or int(slot) <= 0:
            print("Thats not a vaild slot")
            continue

        if participants[slot] != name:
            print(name + " is not in that starting slot silly")
            continue 

        if check(slot,1):
            break

    print("Success:")
    print(name + "has been cancelled from starting slot #" + slot + "\n")

    participants[slot] = None
    return participants
    

def view_participants(participants):

    print("View Participants")
    print("====================\n")

    while(True):

        print("please enter the slot for the participant: " + "1-" + str(len(participants)))
        time.sleep(1)
        slot = input()

        if int(slot) >= len(participants)+1 or int(slot) <= 0:
            print("Thats not a vaild slot")
            continue

        if check(slot,1):
            break
    
    for x,y in participants.items():
        if int(x) in range(int(slot)-5,int(slot)+6):
            print(x,": ",y)


def save(participants,name):

    file = open( name + ".json","w")
    file = json.dump(participants, file)

def load(name):

    file = open( name + ".json","r")
    participants = json.load(file)
    return participants

def search(participants):
    while(True):

        print("please enter the the name of participant last and first with a comma: \n")
        time.sleep(1)
        name = input()

        if (name in participants.values()) == False:
            print("No one by that name is in the tournment\n")
            continue

        if check(name,2):
            break
    
    for x,y in participants.items():
        if y == name:
            print(x + ": " + participants[x])

def check(name,number):
    if number == 1:
        for x in name:
            if x.isalpha():
                print("there be a letter in your input\n")
                return False
        else:
            return True

    elif number == 2:
        for x in name:
            if x.isalpha() == False and x != ",":
                print("there be a number in your input\n")
                return False
        else:
            return True



print("Welcome to Tournaments R Us")
print("============================")

participants = {}

while(True):
    print("Enter the number of participants:\n")
    time.sleep(1)
    total = input()

    if check(total,1):
        break

for x in range(0,int(total)):
    participants[str(x+1)] = None

print("There are " + str(total) + " participant slots ready for sign-ups.\n")

while(True):

    menuselection = 0
    
    #test
    print(participants)
    print("\n")

    print("Participant Menu")
    print("================")
    print("1. Sign Up")
    print("2. Cancel Sign Up")
    print("3. View Participants")
    print("4. View Participants Alphabetically By Last Name")
    print("5. Search For Participant")
    print("6. Save Changes")
    print("7. Load file")
    print("8. Exit\n")

    time.sleep(1)
    menuselection = input()

    if menuselection == "1":
        participants = sign_up(participants)
    elif menuselection == "2":
        participants = cancel_sign_up(participants)
    elif menuselection == "3":
        view_participants(participants)
    elif menuselection == "4":
        print(sorted(participants.items(), key=lambda x: (x[1] is None, x[1])))
    elif menuselection == "5":
        search(participants)
    elif menuselection == "6":
        print("What is the name of the file?")
        time.sleep(1)
        name = input()
        save(participants,name)
    elif menuselection == "7":
        print("What is the name of the file?")
        time.sleep(1)
        name = input()
        participants = load(name)
    elif menuselection == "8":
        print("remeber if you have unsaved changes they will not save\n")
        print("are you sure you want to exit press 1 to cancel or anything else to exit ")
        time.sleep(1)
        answer = input()
        if answer == "1":
            continue
        break
    else:
        print("Not Vaild")


print("Goodbye!")


