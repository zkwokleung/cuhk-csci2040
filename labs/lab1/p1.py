nums = []  # A list to store all the numbers
numStrs = ["first", "second", "third", "fourth", "fifth"]


def is_int(input: str):  # A function to check if the input is an integer
    if input.isnumeric():
        return True
    else:
        print("Your input is not an integer!")
        return False


for i in range(5):
    ipt = input("Please input the {} number: ".format(numStrs[i]))
    if is_int(ipt):
        nums.append(int(ipt))

nums.sort(reverse=True)

if len(nums) > 0:
    # average
    avg = sum(nums) / len(nums)

    # List of input where x <= average
    temp = [x for x in nums if x <= avg and x >= 0]
    # Bigest integer that is smaller then the avaerage
    val = temp[0] if len(temp) > 0 else 0

    if len(nums) >= 3:
        val = nums[2] if nums[2] > val else val
    else:
        val = nums[-1] if nums[-1] > val else val

    print("The value is {}.".format(val))
print("Program ends.")
