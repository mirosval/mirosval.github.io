---
layout: single
title: Lamp Project&#58; Arduino Software
categories: [lamp,english]
tags: [arduino,ble]
---

Bluetooth 4 Low Energy protocol implementation on the Lamp

---

1. [Project Overview]({% post_url 2015-01-18-lamp-project %})
1. [Hardware]({% post_url 2015-03-07-lamp-project-2 %})
1. [Arduino Software]({% post_url 2015-03-12-lamp-project-3%})
1. [Printed Circuit Boards]({% post_url 2015-03-19-lamp-project-4%})
1. [Assembly Timelapse]({% post_url 2015-04-01-lamp-project-5%})


Below you can find the whole source code for the Arduino sketch uploaded to RFduino. It's pretty simple for now, it contains mappings to the pins that output [PWM](http://en.wikipedia.org/wiki/Pulse-width_modulation) for the LEDs. It also contains definitions of 2 modes that are supported: *MODE_RESET* and *MODE_HOLD*. The reset mode will turn of the light on disconnect, while the hold mode will keep the color even if the remote disconnects. It can then be changed if someone send it a new color.

The most interesting I guess is the onReceive function that is called by the RFduino stack when it has received new data. It receives a pointer to the data array and its length. This also defines the lamp protocol, so the data format is as follows:

* One data packet is 4 bytes long
* Position 0 is the mode, currently only values 0 and 1 are supported, 0 will reset color after the client disconnects, 1 will keep the color until changed
* Position 1-3 are RGB values to be written to the output

The mode is finally resolved in the RFduinoBLE_onDisconnect function.

{% highlight c linenos %}

#include <RFduinoBLE.h>

// Lamp Modes
const byte MODE_RESET = 0 << 0;
const byte MODE_HOLD = 1 << 0;

// pin 3 on the RGB shield is the red led
// (can be turned on/off from the iPhone app)
int led_r = 3;
int led_g = 4;
int led_b = 2;

byte mode = 0;

void setup() {
  // led turned on/off from the iPhone app
  pinMode(led_r, OUTPUT);
  pinMode(led_g, OUTPUT);
  pinMode(led_b, OUTPUT);

  RFduinoBLE.advertisementData = "mlamp";
  
  // start the BLE stack
  RFduinoBLE.begin();
}

void loop() {

}

void RFduinoBLE_onDisconnect()
{
  if(mode & MODE_HOLD) {
    Serial.println("Mode was set to MODE_HOLD, so will leave LEDs on");
  } else {
    // MODE_RESET
    Serial.println("Mode was set to MODE_RESET, so turning off LEDs");
    // don't leave the led on if they disconnect
    analogWrite(led_r, 0);
    analogWrite(led_g, 0);
    analogWrite(led_b, 0);
  }
}

void RFduinoBLE_onReceive(char *data, int len)
{
  if(len != 4) {
    return;
  }
  
  // 2nd byte is mode
  mode = (byte)data[0];
  
  // 3rd, 4th, 5th are r,g,b
  byte r = data[1];
  byte g = data[2];
  byte b = data[3];
  
  // set the color
  analogWrite(led_r, r);
  analogWrite(led_g, g);
  analogWrite(led_b, b);
}
{% endhighlight %}
