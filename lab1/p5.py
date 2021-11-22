from getpass import getpass

ipt = getpass("Please input goal posts: ")
region = ipt.split(' ')
region = [int(region[i]) for i in range(2)]

score = 0
goal = 0
top_bin = 0

for i in range(5):
    x = int(input("Player 2 please kick: "))
    if x == region[0] or x == region[1]:
        score += 2
        top_bin += 1
        print("Top Bin!!!")
    elif x > region[0] and x < region[1]:
        score += 1
        goal += 1
        print("Goal!")
    else:
        print("You missed!")

print("Finished with {} goals and {} top bin.".format(goal, top_bin))
print("Your final score is {}.".format(score))
print("Program ends.")
