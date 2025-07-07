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

![PCB](https://raw.githubusercontent.com/ConfusedHello/Videography-Light/refs/heads/main/assets/KicadPCB2.png)
![PCB](https://raw.githubusercontent.com/ConfusedHello/Videography-Light/refs/heads/main/assets/KicadPCB1.png)
![PCB](https://raw.githubusercontent.com/ConfusedHello/Videography-Light/refs/heads/main/assets/FusionPCB2.png)
![PCB](https://raw.githubusercontent.com/ConfusedHello/Videography-Light/refs/heads/main/assets/FusionPCB2.png)

Finishing off the PCB was not particularly easy but it (hopefully) should be functional! Here's some crazy routing (with the GND plane removed)

![PCB](https://raw.githubusercontent.com/ConfusedHello/Videography-Light/refs/heads/main/assets/PCB2.png)


**Time spent: 22hrs**


## July 2nd - @ConfusedHello
Another full day spent on the project - practically the entire day from waking up to going to sleep. Made the control board schematic and PCB today!

The control board will use a XIAO RP2040 MCU, along with a DAC for precise RGBW intensity control (voltage control). The PCB layout for this board was honestly not the worst I've done. There's also a 5V regulator circuit for the MCU and DAC.

![Schematic](https://raw.githubusercontent.com/ConfusedHello/Videography-Light/refs/heads/main/assets/Schematic3.png)
![PCB](https://raw.githubusercontent.com/ConfusedHello/Videography-Light/refs/heads/main/assets/PCB1.png)

Also managed to write the software for the MCU today now available in [\src\Software](https://github.com/ConfusedHello/Videography-Light/tree/main/src/Software)


**Time spent: 14hrs**


## June 30th / July 1st - @ConfusedHello
Journaling two days at once here (mostly because I was up until 2am looking at plane tickets) but as a quick summary of what's happened the last two days (would prefer nice, longer journals but timeee), the initial research involved looking at current commercial products and planning a little into how we're going to do this. A few things we looked at include:

- Important information about film lights! This includes brightness, CRI, DMX. One important spec is the Color Rendering Index which determines the accuracy of skin tone under the light. Typical film lights are ~96CRI.
- RGBW LEDs! I think I've settled on the [Lumileds L1MC-RGB2290500MP0](https://au.mouser.com/ProductDetail/Lumileds/L1MC-RGB2290500MP0?qs=sGAEpiMZZMv0DJfhVcWlKxHzv%2FYltZfuS1ndax89H6UJdf0iYUN9cA%3D%3D) for their 90CRI (not particularly good for filming but still better than all the other 70-80CRI ones). The 2200K (warm white) temperature isn't *the best* but I imagine we can get around that by utilising the RGB colours more when going for a cool lighting and utilising the white more when shooting warm.
- LED drivers! From the looks of it there doesn't actually seem to be all that many for me to choose from that support the max ~200mA current but 120mA I<sub>f</sub> should do okay (this is the max for the drivers I've found). The [TLC59116](https://www.ti.com/product/TLC59116) should be okay for this project.
- The case and stand I'm leaving the @Jayx2u - they'll be designing the case, as well as the mounting solution for the light and other misc. components (such as fins).

A lot more research later the setup will most likely be 36 LED packages per board (6x6 grid) and current controlled from 48V, continuing on with the research, A LOT of things were scrapped in the process such as suitable DC/DC buck converters (for 3.3V and 4.5V) when looking at parallel LED drivers before landing on the current (simplified), more efficient solution: driving the LEDs directly from a 48V supply with current control. This high-voltage approach minimizes current requirements, while also reducing trace widths on the PCB.

Considering that we have a 48V supply let's calculate the amount of chips we'll need to power this board.

48V supply for 36 LED packages (6x6 matrix)

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


After wiring it up in KiCad:
![Schematic](https://raw.githubusercontent.com/ConfusedHello/Videography-Light/refs/heads/main/assets/Schematic1.png)

And the controllers:
![Schematic](https://raw.githubusercontent.com/ConfusedHello/Videography-Light/refs/heads/main/assets/Schematic2.png)

Will speedrun the rest of the schematic and PCB tomorrow maybe? Time to finish up for today though as it's almost 1AM.

**Time spent: 20hrs**


## June 29th - @ConfusedHello
It's 2AM in the morning and ~~I'm calling you now~~ making a new Git repo! Today was some initial research to determine if the project was achievable and some other general information relating to the project. Also, happy to bring @Jayx2u onboard this time! We'll be working on this project realistically over the next two weeks to (hopefully) make a decent film light for our planned upcoming video!

**Time spent: 3hrs**
