---
layout: single
title: Macbook Pro SSD Upgrade
categories: [other,english]
tags: [hardware]
---

I have a Macbook Pro from mid 2010. Its coming up on 4 years, so some would say that it's quite old,
but I've upgraded its RAM to 8GB and it has been working for me quite nicely until recently when I felt
that it's starting to get slow.

###Dust cleaning

The first problem appeared in the summer, when I've installed Mavericks. At the time I've been using
Google Chrome as my primary web browser and it has become unbearable. The machine would run hot and
with fans at full speed with a lot of noise. So at the time I switched back to Safari which helped 
tremendously, but Safari has many other shortcomings (Horrible PDF support, Reddit's RES didn't work, etc.)
so I wanted to switch back to Chrome, and now after Christmas they seem to have released a new version
(I'm using the Beta channel, so now it's 33) which does not suffer from the performance issues of the
old one, so I switched back and everything seemed fine, with just occasional fan rampage.

But it still bothered me, it seemed that the fans would go crazy for no reason (low CPU and energy use,
and still, fans were running at 6000rpm). So I've removed the back cover and cleaned all the dust from
the fans, that has helped incredibly, now it runs much cooler (up to 10&deg;C cooler) and much more
quiet (most of the time just 2000rpm).

###New SSD
I still wanted to improve the performance, and the SSD looked like a good option. After looking it
up briefly I decided on Samsung 840 EVO 250GB SSD, it was faster than what my Macbook could handle
(SATA III vs SATA II on my Macbook Pro), but not much more expensive than the lower options. At about
150&euro; it wasn't too expensive either. I got the Laptop Upgrade kit.

The kit comes with just a SATA to USB connector and some useless CD with software. It does not have
any screw drivers, but I had that covered. You only need a Phillips screwdriver luckily.

The annoying part was that my HD was 500GB and I needed to reduce that to about 200GB if I wanted
to fit into the SSD comfortably. I've moved all my photos to an external HDD, that took some good
3-4 hours.

I first formatted the SSD to `Mac OS Extended Journaled` and to move the filesystem to the SSD 
I've used the [Carbon Copy Cloner](http://www.bombich.com/). It allows you to create the Mavericks
recovery partition on the drive as well, so you could just use that to make a clean install. But
I've copied my whole system over using the CCC, about 200GB took around 4 hours to complete.

I've encountered an issue with Time Machine local backups, they will use up the empty space on 
the drive, so I've deleted almost 300GB of data and only had 70GB free on a 500GB drive. But it
was sufficient to just run the Time Machine and it would remove these local backups during the
Preparing Backup phase.

The actual HW swap went well, the SSD is much lighter and a bit smaller than the original HDD.
I've used the [iFixit guide](http://www.ifixit.com/Guide/MacBook+Pro+15-Inch+Unibody+Mid+2010+Hard+Drive+Replacement/3030),
but I haven't removed the battery and to unscrew the HDD screws on the side I've just used pliers
to unscrew them carefully and then screw them back on the SSD. This is necessary to hold it in
place, since it is slightly smaller than the original.

After the replacement I've used [Trim Enabler](http://www.cindori.org/software/trimenabler/) to
enable TRIM support, because apparently Apple only enables TRIM on their own SSDs by default.

###Performance
I have measured my disk performance before and after the upgrade using [Blackmagic Disk Speed Test](https://itunes.apple.com/us/app/blackmagic-disk-speed-test/id425264550?mt=12)
and this is what I got:

{% highlight text %}
Before:
    Write:  42.5 MB/s   Read:   39.9 MB/s
After:
    Write: 202.0 MB/s   Read:  256.5 MB/s
{% endhighlight %}

Subjectively it feels a lot faster, especially opening apps is almost instantaneous. The
main bottleneck now is probably the 3Gb/s SATA II interface, because the SSD should give
around 500MB/s on SATA III. Over all I think this was a good investment and a relatively
painless upgrade (apart from all the slow copying, ugh).

Here are the Speed Test Screen Shots:

####Before upgrade
![Before SSD Upgrade]({{ site.baseurl }}/images/ssd/old.png)
####After upgrade
![After SSD Upgrade]({{ site.baseurl }}/images/ssd/new.png)
