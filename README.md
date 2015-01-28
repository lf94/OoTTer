# Ocarina of Time Terminal
Ootter - A really rudimentary terminal written for Ocarina of Time (Debug ROM)

Written by Lee (lee@is-an-information-technology-professional.com)

I wrote this to avoid having to use modified emulators to print debug texts in N64 games. It is in no way more superior than modified emulators, but it was a neat proof of concept. This was written for specifically the Ocarina of Time Debug ROM, but could easily be ported to other games. Currently only stable with 10 lines of text, but it could display more if graph_alloc (a function in the game) is modified. If there are any questions feel free to file an issue or improve it and send a pull request.

## Features
* 32 lines of display (for this game at least)
* printf-like functionality
* Easy to use
* Flexible - port to other games supporting bcopy/memcpy or *printf, and screen drawing

## Build Instructions
Assembled with Renegade64 using the following options:
* Language: r4300i
* Mode: On Command
* Code Type: 81
* NOP Type: Long
* Output Type: Normal 

## Tools
These are the tools I used to build this tiny project.
* Nemu64 for N64 emulation and debugging
* Renegade64 for its dis/assembler
* Python for tiny scripts and calculator
* Leo (outline editor) for organization
* IDA to search for printf functions
* WINE to run Nemu64 and Renegade64.

All development was done on Debian SID.

## Thanks
Thank you to twili for helping me look for printf functions; electric_ for motivation.
