import time
import sys


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.025)


def doMaths(stringNow, viewProgress):
    while int(stringNow) > 100:
        nextString = ""
        if len(stringNow) % 2 == 0:
            for i in range(1, int(len(stringNow)/2+1)):
                nextString += str(int(stringNow[i-1]) + int(stringNow[-i]))
        else:
            for i in range(1, int((len(stringNow)-1)/2+1)):
                nextString += str(int(stringNow[i-1]) + int(stringNow[-i]))
            nextString += str(int(stringNow[int((len(stringNow)-1)/2)]))
        if viewProgress:
            print()
            delay_print(nextString)
            print()
            time.sleep(0.5)
        stringNow = nextString
    return stringNow


def matchMake(person1, person2, method, viewProgress):
    if person1 == "" or person2 == "":
        return 0
    stringNow = ""
    if viewProgress:
        print()
        delay_print("Progress: ")
        print()
        time.sleep(0.5)
        delay_print(person1)
        print()
        delay_print(person2)
        time.sleep(1)
        print()
    person1 = ''.join(ch for ch in person1 if ch.isalnum())
    person2 = ''.join(ch for ch in person2 if ch.isalnum())
    for letter1 in person1:
        totalNow = 0
        if method == 2:
            if person1.count(letter1) != 0 and person1.count(letter1) != 1:
                totalNow = person1.count(letter1) - 1
        for letter2 in person2:
            if letter1 == letter2:
                totalNow += 1
                person1 = person1.replace(letter1, "")
                person2 = person2.replace(letter2, "")
        if totalNow != 0:
            stringNow += str(totalNow)
        if viewProgress:
            delay_print(stringNow)
            print()
            time.sleep(0.5)
    return doMaths(stringNow, viewProgress)


def main():
    delay_print(
        "Welcome to Match Maker, where we detimine the compatibility between you and your crush!")
    print()
    time.sleep(2)
    delay_print("Enter person's FULL name: ")
    person1 = input().lower()
    delay_print("Enter the person's FULL name you'd like to match them with: ")
    person2 = input().lower()
    delay_print(
        "Which method of matching would you like to use? [1/2] (Default: 1): ")
    method = input().lower()
    delay_print(
        "Would you like to see the progress of the matching? [y/n] (Default: n): ")
    viewProgress = input().lower()
    if viewProgress == "y":
        viewProgress = True
    else:
        viewProgress = False
    if method == "2":
        method = 2
    else:
        method = 1
    total = matchMake(person1, person2, method, viewProgress)
    delay_print("The probability of the two people dating is: ")
    time.sleep(0.5)
    delay_print(".")
    time.sleep(0.1)
    delay_print(".")
    time.sleep(0.1)
    delay_print(".")
    time.sleep(0.1)
    delay_print(" ")
    time.sleep(2)
    delay_print(str(total) + "%!!!")


if __name__ == "__main__":
    main()
