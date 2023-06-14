# Flag Shop  

>Come and buy yourself a flag! Author: NoobMaster  

- This is pretty simple `nc challs.n00bzunit3d.xyz 50267` returns  

Welcome to the flag shop! The flag costs $1337 but you have $100. You can buy the fake flag which costs $50  
[1] Buy real flag - $1337  
[2] Buy fake flag - $50  
[3] Check account balance  

<br>

- It restricts us from buying a real flag `Not enough money!` if we don't have enough money.
But it does not restrict us from buying a fake flag  

<br>

- Buying three fake flags and checking our balance `$-50` we can see that our balance is now negetive.

<br>

- Buying a real flag now we get the flag.    
n00bz{5h0p_g0t_h3ck3d_4nd_fl4g_g0t_570l3n!}

<br>

- This is because of an integer underflow and it is an unsigned int causing the balance to be a huge number. 

<br>

[Original Writeup](https://github.com/n00bzUnit3d/n00bzCTF2023-OfficalWriteups/tree/master/Pwn/Flag%20Shop)  

### Flag - n00bz{5h0p_g0t_h3ck3d_4nd_fl4g_g0t_570l3n!}

