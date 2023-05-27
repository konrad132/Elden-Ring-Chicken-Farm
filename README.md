# Elden-Ring-Chicken-Farm
This is a Elden Ring Farm, that does the "Chicken farm" at the Palace Approach Ledge Road using PYautogui. This code also lets you estimate the duration and your final balance if requested.

Some adjustments to the code will be needed to be run due to Pyautogui using monitor coordinates that differ by monitor size.
To be able to work around this, I created a function called reportmouseposition. This function requires a specific amount of time to run and will, report your mouse coordinates while you go through the sequence.

The code works doing the following steps. 
1. Teleport to nearest Site of Grace
2.  Turn body towards ledge
3.  Walk to ledge
4.  Aim Bow
5.  Position Bow
6.  Repeat

For steps 2 and 5 you will need to use reportmouseposition to find the ideal position to aim towards. 
