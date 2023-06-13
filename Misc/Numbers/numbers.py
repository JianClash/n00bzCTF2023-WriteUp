import re
import time
from pynput.keyboard import Controller, Key

keyboard = Controller()
time.sleep(5)

with open("numbersOutput", "r+") as file:
    while True:
        a = file.readline()
        question = file.readline()
        numbers = re.findall('\\d+', question)

        j = int(numbers[1])
        k = numbers[0]
        print(j, a)
        counter = 0

        for i in range(1, int(j)):

            num = str(i)
            for c in num:
                if c == k:
                    counter += 1

        print(f"counter: {counter}")
        for c in str(counter):
            keyboard.press(c)
            keyboard.release(c)

        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        while file.readline() == "":
            continue
