---
layout: single
title: Lamp Project
categories: [lamp,english]
tags: [hardware,arduino,ios]
---

In this series I will share my experiences with building an Rfduino-based RGB LED lamp from start to finish, including iOS and other apps for remote control.

---

I've had this idea for a project for quite some time now, but now I've actually come around to some real progress. The project specificaton is simple: I wanted to build an RGB LED lamp that could be controlled wirelessly. That idea in and of itself is not particularly new or unprecedented, however when I was looking at ready-made solutions online, I couldn't find anything that would work for me. I really just wanted something that could be programmed or controlled remotely. 

##The Vision

I really just want a smart lamp, that would be able to do things like change color and intensity of light according to various outside stimuli, such as direct control via a mobile phone, automatic lighting up and dimming according to my sleep cycle, audio input, temperature and so on. I would like to be able to control multiple lamps from one place and optionally have "groups" of lamps that could be controlled separately. I could not find anything that would be both inexpensive and flexible enough for my programming needs (most of these cheap RGB LED strips come with an IR remote control, but that is a joke). I thought I could build something that would work for me from the following components:

* IKEA Lamp
* Arduino
* RGB LED Strip
* Power supply
* iOS Device
* Raspberry PI

##The current state of things

![Current state of the RGB LED Lamp]({{ site.url }}/images/lamp/lamp-1.jpg){: .pull-left .half}

I've built a lamp using an Arduino and a Bluetooth chip that could be controlled by Bluetooth 2.0 back in 2012. This was good, but not good enough. The RGB strip worked well, but Bluetooth connection was unreliable and prone to problems (unable to find the device, unable to connect, etc.)

In the summer of 2014 I have built another prototype based on the [Rfduino](http://www.rfduino.com/), the new hot platform that includes Arduino and Bluetooth 4.0 (or BLE) in one package. This prototype works flawlessly, the connection is stable and easily established, which is a huge plus.

I currently have 1 Rfduino-based lamp with a 1m RGB LED strip attached to it. The LED strip I'm currently using is something like [this](http://www.amazon.co.uk/Waterproof-300LEDs-Flexible-Lighting-Decoration/dp/B009ZOLW04/ref=sr_1_46?s=lighting&ie=UTF8&qid=1421617842&sr=1-46&keywords=5050+rgb+led+strip). The key parameters are 12V, ~1A/m, 5050 LEDs 60 pieces per meter. The cool part is that the strip can be cut every 5cm (every 3 LEDs). So I have bought a 5m roll and I'm going to cut it into 5 1m long strips for use in 5 lamps.

The 1m LED strip I have draws 1.2A at 12V, which means it has a wattage of 14.4W. This determines all of the other components that are needed. For power supply I have used something like [this](http://uk.farnell.com/powerpax/sw3526/ac-dc-power-supply-12v-1-25a-euro/dp/1971795). At 15W it supplies enough power for the LED strip,  Rfduino and the remaining circuitry. 

I have designed a simple protocol that is able to send the RGB color to the lamp and is able to address up to 255 lamps. iOS is limited to 10 simmultaneous BT connections, so 255 is more than could be realistically adressed anyways. 

And lastly I have built an iOS app that is able to set a solid color on a lamp, or alternatively can use the microphone to set the intensity of the light, while the user can pick the hue. I will discuss all these points in depth in future posts.

##Immediate future of the project

Currently I have 1 lamp that works with the iOS app. I've recently received a shipment of 7 new Rfduinos and I've ordered more parts online which should arrive shortly. In the next weeks I'm going to build another prototype and test how the iOS app and the protocol cope with 2 or 3 lamps. I would also like to employ my Raspberry pi in the project, so that it could control the lamps without the need to use an iOS device. This would be perfect for things like morning alarm light, afternoon automatic lights and so on.

Another little subproject I have researched and would like to do is having PCBs printed. I have started designing the board using [Eagle](http://www.cadsoftusa.com/), but I have to wait until I can finalize the component list. I found an interesting place that could print my PCBs, [OSHPark](https://oshpark.com/) and I would like to see how it works.

##Long term ideas

There are a couple of things that I can see as a long term / low priority goals for the project:

* Have some sort of switch that would disentangle the lamp from the iOS controller
* Have printed PCBs and a box with everything nicely contained inside

