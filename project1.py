answer = '1'
images = {} #Using a dictionary not a list because I kept getting errors with strings and a list

while (answer == '1'): #Wanted to use a while loop here to enter all the files, works perfectly.
    currentim = input("Please enter the exact name of the file you would like to be merged: ")
    answer = input("Are there any more files? Please enter Yes/No as 1/0: ")
    images[currentim] = currentim
    
print("Please Wait...")

from PIL import Image

RedList = [] #Setting up lists to use for later
BlueList = []
GreenList = []
finalPXList = []

def findRed(RedList): #Setting up funtions to use later to call the median of a bunch of numbers
    Redlength = len(RedList)
    RedSorted = sorted(RedList)
    RedMiddle = (Redlength + 1)//2 - 1
    return RedSorted[RedMiddle]
def findGreen(GreenList):
    Greenlength = len(GreenList)
    GreenSorted = sorted(GreenList)
    GreenMiddle = (Greenlength + 1)//2 - 1
    return GreenSorted[GreenMiddle]
def findBlue(BlueList):
    Bluelength = len(BlueList)
    BlueSorted = sorted(BlueList)
    BlueMiddle = (Bluelength + 1)//2 - 1
    return BlueSorted[BlueMiddle]

tempPic = Image.open(images[currentim]) #Opens currentim to get size to make a new image
picW, picH = tempPic.size
finalImage = Image.new("RGB", (picW, picH)) #New image is made using measurements from the currently open image

for x in range(0, picW):
    for y in range(0, picH):
        for i in images:
            im = Image.open(images[i]) #Opens the images in order (hopefully)
            myRed, myGreen, myBlue = im.getpixel((x,y)) #Gets RGB color info from each pixel depending on what x, y we're on
            RedList.append(myRed)
            GreenList.append(myGreen)
            BlueList.append(myBlue) #Adds the colors of each image's pixels to a respectively colored list
        finalPXList.append(findRed(RedList))
        finalPXList.append(findGreen(GreenList))
        finalPXList.append(findBlue(BlueList)) #Adds each median number of each color in the current pixel
        finalPXList = tuple(finalPXList) #Makes a tuple out of the list of 3 values we just made for RGB
        finalImage.putpixel((x,y),finalPXList) #Adds a pixel to the current coordinate on the newly made image
        finalPXList = list(finalPXList) #Swaps the tuple we made back to a list so we can del[:] and .append
        del RedList[:]
        del GreenList[:]
        del BlueList[:]
        del finalPXList[:] #Clears all the lists to make way for the new pixel
        
finalImage.save('FinalImage.png') #Saves the final picture as a .png
#I guess I'll add my github here too just in case: https://github.com/Private-Shorty/cst205project1