---
layout: single
title: Unwrapping the iris
categories: [master-thesis,english]
tags: [master-thesis,opencv,python,iris]
---

In the previous installments we've looked at [Pupil Detection]({% post_url 2014-01-29-pupil-detection %})
and [Iris Detection]({% post_url 2014-01-30-iris-detection %}). Now we'll look at unwrapping the image
of the iris from a circular pattern to a rectangular one. We will use this later for some other 
algorithms. 

So by applying the above mentioned algorithms we got two bits of information: the center of the pupil and
the estimated radius of the iris. We can see them on the image below.

![Pupil center and iris radius]({{ site.url }}/images/003-unwrap/001-original.png)

In order to transform this circular iris into a rectangular image, we do the following:

{% highlight python linenos %}
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('003/eye.png')

center = (376, 184)
iris_radius = 115

nsamples = 360
samples = np.linspace(0, 2 * np.pi, nsamples)[:-1]

polar = np.zeros((iris_radius, nsamples))

for r in range(iris_radius):
    for theta in samples:
        x = r * np.cos(theta) + center[0]
        y = r * np.sin(theta) + center[1]
        
        polar[r][theta * nsamples / 2.0 / np.pi] = image[y][x][0]

plt.figure(figsize=(10, 5))
plt.imshow(polar, cmap='gray')
{% endhighlight %}

We create an empty image with resolution `iris_radius * 360` and then we iterate through this image
and calculate the corresponding position in the circular image from the angle and the radius and copy
this value to the new image.

![Pupil center and iris radius]({{ site.url }}/images/003-unwrap/002-unwrapped.png)

This post is also available as an [iPython Notebook](http://nbviewer.ipython.org/gist/mirosval/8754366)
