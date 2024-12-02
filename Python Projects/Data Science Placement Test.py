import random

#Question A1

def repeat_char(string, num):
    output = ""
    for x in string:
        for y in range(num):
            output = output + x
    print(output)

string = ["h", "i"] #Default String List to demonstrate functionality (input functionality is assumed as not needed)

print("Question AE1")
print("Example String is a List with letters 'h' and 'i', in that order, spelling out 'hi'")
print("Function ran: repeat_char(string, 5)")

repeat_char(string, 5) #This is demonstrating the example case

#Question A2

def partial_prod(nums, n):
    temp_num = 1
    for x in range(n):
        if x >= len(nums):
            break
        else:
            temp_num = temp_num*nums[x]
    print(temp_num)

nums = [2,4,7,10]

print("Question AE2")
print("Example nums is a List with numbers in the following order: 2, 4, 7, and 10")
print("Function ran: partial_prod(nums,5)")

partial_prod(nums, 5)

#Question A3

def func(paths):
    temp_string = ""
    for x in paths:
        file = open(x, 'r')
        temp_string = temp_string + file
        file.close()

print("Question AE3")
print("Example not given/ran due to file logistics")
print("I assume here that all files are filled with only text")

#Question A4


class image:
    def __init__(self,dataOrigin,pixelData,label):
        self.image = pixelData
        self.classification = label
    def shuffle(dataset):
        random.shuffle(dataset)
    def labelRetrieve(dataset, label):
        for x in dataset:
            if x.classification == label:
                print(x.dataOrigin + "is labelled as a" + label)


#Placeholder Variables
img1 = ("HistologyLab1", pixelData1, "Cat") 
img2 = ("HistologyLab2", pixelData2, "Dog")
img3 = ("HistologyLab3", pixelData3, "Cat")

dataset = [img1,img2,img3] #Not sure if the question requests this to be in the class

print("Question AE3")
print("Example not ran due to dataset logistics")