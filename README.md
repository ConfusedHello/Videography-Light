# Videography-Light
Ever wanted a videography light but died when seeing the insane prices? Me too! This project involves a DIY, high-power RGBW film light built by [@ConfusedHello](https://github.com/confusedhello) and [@Jayx2u](https://github.com/Jayx2u/) for the Hack Club [Highway to Hardware](https://highway.hackclub.com/) program!

We decided to design this project because as students, we honestly don't have the spare cash lying around for one, and we wanted a nice accent light for our planned upcoming videos. It utilises 36 *current controlled* RGBW LEDs running off a 48V supply and controlled with a Xiao RP2040!

For details about the design process or other information, check out the [development journal](https://highway.hackclub.com/projects/ConfusedHello/Videography-Light). A local copy is available in [JOURNAL.md](https://github.com/ConfusedHello/Videography-Light/blob/main/JOURNAL.md).


## The Design
Here's a quick diagram showing how the project works!
![Wiring Diagram](/assets/WiringDiagram.png)

<!-- TODO:
Screenshot of a full 3D model render
-->

And a nice rendered image of the control board.
![Control Board](/assets/ControlBoard.png)

As well as the schematic and PCB for both the control and light boards! 
![Schematic and PCB for both boards](/assets/SchematicPCB.png)


## Bill of Materials
Also available in .csv format in [BOM.csv](https://github.com/ConfusedHello/Videography-Light/blob/main/BOM.csv)! BOMs for the PCBs are in [ControlBoard.csv](https://github.com/ConfusedHello/Videography-Light/blob/main/src/Production/Control%20PCB/ControlBoard.csv) and [VideographyLight.csv](https://github.com/ConfusedHello/Videography-Light/blob/main/src/Production/Light%20PCB/VideographyLight.csv)~

|Item                      |Qty.|Price (USD)|Ext. (USD)|Link                                                 |
|--------------------------|----|-----------|----------|-----------------------------------------------------|
|997-L1MCRGB2295MP0        |36  |$1.36      |$48.96    |https://mouser.com/c/?q=997-L1MCRGB2295MP0           |
|81-GRM32EC72A106ME5K      |11  |$0.71      |$7.85     |https://mouser.com/c/?q=81-GRM32EC72A106ME5K         |
|710-7447706101            |11  |$1.01      |$11.11    |https://mouser.com/c/?q=710-7447706101               |
|71-WSLT2010R5000FEA1      |11  |$0.57      |$6.28     |https://mouser.com/c/?q=71-WSLT2010R5000FEA1         |
|625-SS1H10-E3             |11  |$0.28      |$3.11     |https://mouser.com/c/?q=625-SS1H10-E3                |
|621-AL8862SP-13           |11  |$0.54      |$5.93     |https://mouser.com/c/?q=621-AL8862SP-13              |
|179-TB0012-508-04GR       |2   |$1.29      |$2.58     |https://mouser.com/c/?q=179-TB0012-508-04GR          |
|179-TB0012-508-02GR       |2   |$0.69      |$1.38     |https://mouser.com/c/?q=179-TB0012-508-02GR          |
|579-MCP4728-E/UN          |1   |$2.50      |$2.50     |https://mouser.com/c/?q=579-MCP4728-E/UN             |
|713-102010428             |1   |$5.40      |$5.40     |https://mouser.com/c/?q=713-102010428                |
|595-LMR51606XFQDBRQ1      |1   |$2.25      |$2.25     |https://mouser.com/c/?q=595-LMR51606XFQDBRQ1         |
|179-TS046695BK100SMT      |5   |$0.16      |$0.80     |https://mouser.com/c/?q=179-TS046695BK100SMT         |
|71-CRCW12104K70JNAIF      |2   |$0.58      |$1.16     |https://mouser.com/c/?q=71-CRCW12104K70JNAIF         |
|71-CRMA1210AF100KFKF      |1   |$0.85      |$0.85     |https://mouser.com/c/?q=71-CRMA1210AF100KFKF         |
|71-CRCW0402-19.1K-E3      |1   |$0.10      |$0.10     |https://mouser.com/c/?q=71-CRCW0402-19.1K-E3         |
|71-CRCW0402-100K-E3       |1   |$0.10      |$0.10     |https://mouser.com/c/?q=71-CRCW0402-100K-E3          |
|70-IFDC5050JZER470M       |1   |$0.96      |$0.96     |https://mouser.com/c/?q=70-IFDC5050JZER470M          |
|637-1N4148W               |5   |$0.10      |$0.50     |https://mouser.com/c/?q=637-1N4148W                  |
|810-C3225X7R1H106MAC      |2   |$0.96      |$1.92     |https://mouser.com/c/?q=810-C3225X7R1H106MAC         |
|81-GRM155R71C104KA88      |2   |$0.10      |$0.20     |https://mouser.com/c/?q=81-GRM155R71C104KA88         |
|81-GRM188R72A104KA35      |1   |$0.15      |$0.15     |https://mouser.com/c/?q=81-GRM188R72A104KA35         |
|581-KAM32LR72A475KU       |1   |$0.91      |$0.91     |https://mouser.com/c/?q=581-KAM32LR72A475KU          |
|Aluminum Heatsink         |10  |$0.73      |$7.33     |https://www.aliexpress.com/item/4000723868050.html   |
|0.96 Inch OLED Display    |1   |$2.60      |$2.60     |https://www.aliexpress.com/item/1005007614149117.html|
|M2 Heat Insert            |16  |$0.11      |$1.73     |https://www.aliexpress.com/item/1005003582355741.html|
|M2 Screw (10mm)           |16  |$0.21      |$3.40     |https://www.aliexpress.com/item/1005005688616965.html|
|48V Power Supply          |1   |$25.73     |$25.73    |https://www.aliexpress.com/item/1005008528926877.html|
|JLCPCB Control Board      |1   |$2.00      |$2.00     |https://www.jlcpcb.com                               |
|JLCPCB Light Board        |1   |$2.00      |$2.00     |https://www.jlcpcb.com                               |
|JLCPCB Light Board Stencil|1   |$7.00      |$7.00     |https://www.jlcpcb.com                               |
|JLCPCB Shipping           |1   |$21.22     |$21.22    |https://www.jlcpcb.com                               |

**Total:** $178.01 USD

<hr>

Made with ❤️ by [@ConfusedHello](https://github.com/confusedhello) and [@Jayx2u](https://github.com/Jayx2u/)
