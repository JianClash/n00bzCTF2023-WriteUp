# Numbers

>*Description* - Welcome to numbers! just answer my few questions to get the flag!
Note: To make this less confusing, I have an example. let's say if it asks - "How many 3's appear till 40?" The answer - 14 because ['3','13','23','30','31','32','33','33','34','35','36','37','38','39'].<br>
Also, the '33' is counted twice (not a typo!) as the three occurs two times (once in the 'ones' digit place and once in the 'tens' digit place)(each entry in that list is like count++). Author: NoobMaster

<br>

- First pipe the questions from the server to file with the command  
    <code>nc challs.n00bzunit3d.xyz 13541 >> numbersOutput</code>

<br>

- We can get the answers with a basic script  

        j = numbers[1]
        k = numbers[0]
        counter = 0
        
        # 0 and j are excluded 
        for i in range(1, int(j)):
            num = str(i)
            for c in num:
                if c == k:
                    counter += 1

        print(f"counter: {counter}")

Note: Now I didn't know this at the time but we can use `count()` function in python to get how many times a character is repeated in a string

<br>

- We can read frome the file that the questions are written to with:  

        import re
        
        # Open numbersOutput with read and write permissions
        with open("numbersOutput", "r+") as file:
            while True:
                file.readline() # Round n!
                question = file.readline() # How many y's appear till x?

                # Only get the numbers from the string as it also contains text
                numbers = re.findall('\\d+', question)

                j = int(numbers[1])
                k = numbers[0]
                counter = 0

                for i in range(1, int(j)):

                    num = str(i)
                    for c in num:
                        if c == k:
                            counter += 1

                print(f"counter: {counter}")
                file.write("")

                file.readline() # Moving On!

<br>

- Finally we can automate our keyboard input with:   
    
        import re
        import time
        from pynput.keyboard import Controller, Key

        keyboard = Controller()
        time.sleep(5)

        with open("numbersOutput", "r+") as file:
            while True:
                a = file.readline() # Round n!
                question = file.readline() # How many y's appear till x?
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
                    
                # To get to the end of the file  
                while file.readline() == "":
                    countinue

<br>

- Splitting our terminal and running `nc challs.n00bzunit3d.xyz 13541 >> numbersOutput` and `python3 numbers.py`.
    After some time we will get an `Index Error:`.  
    `cat numbersOutput` gives us the flag

<br>

**Note: Instead of automating our keyboard we can send our answers directly to the server.  
This was my first ctf and the first time I did challenges like this. So I didn't know you could do that.  
This is not the most efficent or the most intuitive solution to see the intended solution  
check out the [official writeup](https://github.com/n00bzUnit3d/n00bzCTF2023-OfficalWriteups/tree/master/Misc/Numbers).**  


### Flag - n00bz{4n_345y_pr0gr4mm1ng_ch4ll}
