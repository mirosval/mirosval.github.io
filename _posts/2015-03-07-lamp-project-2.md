---
layout: single
title: Lamp Project&#58; The Hardware Prototype
categories: [lamp,english]
tags: [hardware,arduino]
---

The detailed description of the prototype hardware used for the lamp project.

---

[Project Overview]({% post_url 2015-01-18-lamp-project %})

I have, obviously, started with an idea. I didn't like any of the exisiting smart lamp solutions, mostly because they lacked customizability. So my thought process was to start with some minimal requirements. I have come up with the following:

* RGB LED Strip for the actual light
* Bluetooth for controls
* Some sort of Arduino to process it all

![Finished prototype board]({{ site.baseurl }}/images/lamp-hw/finished-board.jpg)

##Choosing the RGB LED Strip

There are lots of different options, there are single-color strips, RGB strips or [programmable strips](http://www.adafruit.com/products/1138), where you can change the color of every single LED. I though I would be fine with just controlling the color of the entire strip so I went with something like [this](http://www.ebay.com/itm/5M-5050-RGB-SMD-LED-Waterproof-Flexible-Strip-300-LEDs-44-Key-IR-Remote-/180992529478).

I don't need the stupid IR controller, but I found that sometimes you can get the same thing *with* the controller for less than without it. The key characteristics are:

* SMD 5050 - this represents the size of a single LED
* 60 LED/m - I want this to be bright
* 12V DC - operating voltage
* 1A/m - required current per 1 meter of the strip

These things are really key, because everything else in the system is based on these values. If you change anything, be sure to adjust the rest of the system accordingly.

![LED Stri Detail]({{ site.baseurl }}/images/lamp-hw/detail-led-strip.jpg)

##Next, Arduino

I have come across [RFduino](http://www.rfduino.com/product/rfd22102-rfduino-dip/index.html). I have bought some basic kit when they were on Kickstarter, but I have since bought 6 more units. The trouble with this board is a bit in its availability. [Sparkfun](https://www.sparkfun.com/categories/274) has it, but in the EU it is much more difficult to get your hands on it. I ended up buying from [Mouser](http://cz.mouser.com/new/rfdigital/rf-digital-rfduino/), but they are primarily a wholesale operation, so it's expensive to buy small quantities from them.

Having said that, I'm really happy with RFduino, it is programmable with the Arduino IDE, has nice sample code and iOS libraries, uses Bluetooth 4.0 Low Energy, which is super nice and, most importantly, I have found the connectivity *great*, it just always works. It has also survived a couple of blunders on my part, such as connecting it to 5V power instead of the recommended 3.3V.

##Power supply

So my calculation went like this: I want a 1m long LED strip controlled by RFduino, that is 12V * 1A = 12W. So I need a 12W power supply. I ended up buying [this one](http://www.gmelectronic.com/power-ac-adapter-12v-1500ma-connector-2-1mm-mw-p751-193) because it has enough power, nice connector and is relatively cheap.

##Connecting it all together

Now I have a LED strip and a power supply which both operate at 12V, but I have a RFduino which operates at 3.3V. So the problem is twofold:

1. Convert 12V to 3.3V to power the RFduino
2. Drive the 12V LED with the signal from RFduino

This in the end translates into 2 subsystems that need to be designed. A power regulator circuit to power RFduino from 12V and an amplifier or a relay that could drive the LEDs.

###Voltage Regulator for the RFduino 12V to 3V

This was the hardest part to figure out for me. I didn't want anything overly complicated and in the end I've settled for the [LP2950-33](http://www.ti.com/product/lp2950-33) ([Datasheet](http://www.onsemi.com/pub_link/Collateral/LP2950-D.PDF)). It looks like a transistor, has 3 legs, one for input, one for output and one for ground. The usual usage example I found involved capacitors between output and ground and optionally between input and ground to further stabilize the voltage. LP2950 comes in different varietes, so I chose the one that had it's output voltage closest to RFduino's 3V.

###Darlington Array to drive the LED Strip

The last thing to do was to bring the PWM pin output from RFduino into the strip. The way the strip is connected is that there is a +12V cable and three different grounds, one for each of the RGB channels. So basically what the darlington does, is connect each of the RGB channels to the ground such, that the amount of current flowing through them can be controlled by RFduino.

![Finished prototype board - wiring]({{ site.baseurl }}/images/lamp-hw/finished-wiring.jpg)

##The Prototype

I have built the prototype using an universal board with headers bought from [Aliexpress](http://www.aliexpress.com/snapshot/6468939297.html?orderId=65605779553704) so that I can plug the RFduino in and out as I please. This is what it looks like when I turn it on:

![Finished prototype turned on]({{ site.baseurl }}/images/lamp-hw/finished-on.jpg)
