---
title: "Videography Light"
author: "ConfusedHello, Jayx2u"
description: "A DIY Film Light for Videography!"
created_at: "2025-06-29"
---

**Total time spent: ??hrs**


## July 7th - @Jayx2u
Hmmm

**Time spent: ??hrs**


## July 3rd, 4th, 7th - @ConfusedHello
Finished off the light PCB!! Here's some screenshots to conclude my development journaling! There's actually better images in the [README](https://raw.githubusercontent.com/ConfusedHello/Videography-Light/) with silkscreens~

![Schematic](https://raw.githubusercontent.com/ConfusedHello/Videography-Light/refs/heads/main/assets/KicadPCB2.png)
![Schematic](https://raw.githubusercontent.com/ConfusedHello/Videography-Light/refs/heads/main/assets/KicadPCB1.png)
![PCB](https://raw.githubusercontent.com/ConfusedHello/Videography-Light/refs/heads/main/assets/FusionPCB2.png)
![PCB](https://raw.githubusercontent.com/ConfusedHello/Videography-Light/refs/heads/main/assets/FusionPCB2.png)

**Time spent: 22hrs**


## July 2nd - @ConfusedHello
Another full day spent on the project - practically the entire day from waking up to going to sleep. Made the control board schematic and PCB today - also wrote the software.

![Schematic](https://raw.githubusercontent.com/ConfusedHello/Videography-Light/refs/heads/main/assets/Schematic3.png)
![PCB](https://raw.githubusercontent.com/ConfusedHello/Videography-Light/refs/heads/main/assets/PCB1.png)


**Time spent: 14hrs**


## June 30th / July 1st - @ConfusedHello
Journaling two days at once here (mostly because I was up until 2am looking at plane tickets) but as a quick summary of what's happened the last two days (would prefer nice, longer journals but timeee)

- RESEARCH HAH
    - Important information about film lights! Brightness, CRI, DMX, etc..
    - RGBW LEDs! I think I've settled on the [Lumileds L1MC-RGB2290500MP0](https://au.mouser.com/ProductDetail/Lumileds/L1MC-RGB2290500MP0?qs=sGAEpiMZZMv0DJfhVcWlKxHzv%2FYltZfuS1ndax89H6UJdf0iYUN9cA%3D%3D) for their 90CRI (not particularly good for filming but still better than all the other 70-80CRI ones). The 2200K (warm white) temperature isn't *the best* but I imagine we can get around that by utilising the RGB colours more when going for a cool lighting and utilising the white more when shooting warm.
    - LED drivers! From the looks of it there doesn't actually seem to be all that many for me to choose from that support the max ~200mA current but 120mA I<sub>f</sub> should do okay (this is the max for the drivers I've found). The [TLC59116](https://www.ti.com/product/TLC59116) should be okay for this project.
    - The case and stand I'm leaving the @Jayx2u - they'll be designing the case, as well as the mounting solution for the light and other misc. components (such as fins).

A lot more research later the setup will most likely be 36 LED packages per board (6x6 grid) and current controlled from 48V.

A LOT of things were researched and scrapped in the process such as suitable DC/DC buck converters (for 3.3V and 4.5V) when looking at the parallel LED drivers before landing on the current (simplified) solution. Cool! Time to design.

Considering that we have a 48V supply let's calculate the amount of chips we'll need to power this board.

48V supply (120W) for 36 LED packages (6x6 matrix)

LED specs:
```
Red - 200mA @ 2.25V drop
Green - 200mA @ 3.55V drop
Blue - 200mA @ 3.3V drop
White - 200mA @ 3.3V drop
```

2.25 x 36 = 81V drop
... 2 channels (40.5V drop each)

3.55 x 36 = 127.8V drop
... 3 channels (42.3V drop each)

3.3 x 36 = 118.8V drop
... 3 channels (39.6V drop each)


And to sanity check our power consumption:
```
Power: 3 x 2 x 200mA + 3 x 200mA + 2 x 200mA
= 2.8A @ 48V
= 105.3W
```

After wiring it up in KiCad:
![Schematic](https://raw.githubusercontent.com/ConfusedHello/Videography-Light/refs/heads/main/assets/Schematic1.png)

And the controllers:
![Schematic](https://raw.githubusercontent.com/ConfusedHello/Videography-Light/refs/heads/main/assets/Schematic2.png)

Will speedrun the rest of the schematic and PCB tomorrow maybe? Time to finish up for today though as it's almost 1AM.

**Time spent: 20hrs**


## June 29th - @ConfusedHello
It's 2AM in the morning and ~~I'm calling you now~~ making a new Git repo! Today was some initial research to determine if the project was achievable and some other general information relating to the project. Also, happy to bring @Jayx2u onboard this time! We'll be working on this project realistically over the next two weeks to (hopefully) make a decent film light for our planned upcoming video!

**Time spent: 3hrs**
