# UnrealWorld Utilities
These are some utilities for the game [UnRealWorld](http://www.unrealworld.fi), a sandbox game set in Iron Age Finland. 

## Generate a character name
`namestartswith.py` will generate a Finnish character name and tell you which gender and which culture a character with that name would be from. I haven't added all of the new names that were added to the game recently so these are just the old ones.

## Generate an entire character completely randomly
`urwChar.py` generates a character completely randomly, giving you a Finnish name, and telling you what options to pick. This isn't as advanced as the characters urwbot generates because I wrote this in 2012, so if you want a custom difficulty level, come see us in IRC. Log on to [freenode.net](http://freenode.net/) and `/msg urwbot help`. [Full list of my bot's features](http://unrealworld.fi/wiki/index.php?title=Chat)


## Cast weatherlore 1000 times

Edit: It turns out this utility has less use than I thought because the game has anti grinding measures in place; weatherlore can only be meaningfully cast once per game hour. I'll leave this description up for posterity though.

`urwSkill.py` grinding certain skills can be boring. If you want to cast weatherlore a thousand times while you do the laundry or something IRL, this program can help. It needs [PyAutoGUI](https://pypi.org/project/PyAutoGUI/) to do its magic. Right now, weatherlore is the only skill that makes sense to use this with but I may add more functionality later. 

Usage: `urwSkill.py -t 5` casts the default skill (weatherlore) five times, with the default delay of 2 seconds.

Specify the keyboard combination for switching to the desktop that has urw running with `-d`. The default is "ctrl winleft 5" which switches to desktop 5 in my window manager but your window manager probably has different shortcuts.