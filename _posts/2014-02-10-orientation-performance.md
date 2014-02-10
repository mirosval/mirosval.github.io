---
layout: single
title: Performance of the getOrientationAndMagnitude()
categories: [master-thesis]
tags: [master-thesis,opencv,python,performance]
---

I normally don't do premature performance optimizations, and I was planning on optimizing the whole eye tracker
later, when I felt I had all of the functionality I wanted, but from time to time, you still want to check your 
code, particularly when it's suspiciously slow. So I did examine the code I had written so far using 
[line_profiler](http://packages.python.org/line_profiler/) (Abysmal documentation btw.) like so:

{% highlight bash %}
kernprof.py -l test.py && python -m line_profiler test.py.lprof
{% endhighlight %}

I have found that the most time is being spent in one function, `getOrientationAndMagnitude`, you'll recall it
looked like this:

{% highlight python linenos %}
def getOrientationAndMagnitude(image, show=False):
    sobelHorizontal = cv2.Sobel(image, cv2.CV_32F, 1, 0)
    sobelVertical = cv2.Sobel(image, cv2.CV_32F, 0, 1)

    h = sobelHorizontal
    v = sobelVertical

    orientation = np.empty(image.shape)
    magnitude = np.empty(image.shape)

    height, width = h.shape
    for y in range(height):
        for x in range(width):
            orientation[y][x] = cv2.fastAtan2(h[y][x], v[y][x])

    magnitude = cv2.magnitude(h, v)

    return orientation, magnitude
{% endhighlight %}

I wrote this code some time ago, when I was less familiar with OpenCV than I am now, and you can quickly see
the hotspot. Yes, the line `14`. I probably did it like this because I hadn't noticed the 
[`phase()`](http://docs.opencv.org/modules/core/doc/operations_on_arrays.html#phase) function OpenCV has.

But this will serve the purpose of showing how such a small oversight can have a dramatic effect on performance.
Armed with the [`phase()`](http://docs.opencv.org/modules/core/doc/operations_on_arrays.html#phase) function,
we can do the following:

{% highlight python linenos %}
def getOrientationAndMagnitude(image, show=False):
    h = cv2.Sobel(image, cv2.CV_32F, 1, 0)
    v = cv2.Sobel(image, cv2.CV_32F, 0, 1)

    orientation = cv2.phase(h, v, angleInDegrees=True)
    magnitude = cv2.magnitude(h, v)

    return orientation, magnitude
{% endhighlight %}

Now this much shorter and simpler function will also run much faster, thanks to OpenCV. And here's how I tested
it:

{% highlight python linenos %}
import cProfile

image = cv2.imread('eye.png')
image = cv2.cvtColor(image, cv2.cv.CV_BGR2GRAY)
image2 = np.copy(image)

cProfile.runctx("refGetOrientationAndMagnitude(image)", globals=globals(), locals=locals())
cProfile.runctx("newGetOrientationAndMagnitude(image)", globals=globals(), locals=locals())
{% endhighlight %}

Which yielded the following results:

{% highlight text %}

201309 function calls in 1.022 seconds

Ordered by: standard name

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     1    0.000    0.000    1.022    1.022 <string>:1(<module>)
     1    0.823    0.823    1.022    1.022 test.py:7(refGetOrientationAndMagnitude)
     2    0.004    0.002    0.004    0.002 {cv2.Sobel}
201000    0.192    0.000    0.192    0.000 {cv2.fastAtan2}
     1    0.001    0.001    0.001    0.001 {cv2.magnitude}
     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     2    0.000    0.000    0.000    0.000 {numpy.core.multiarray.empty}
   301    0.002    0.000    0.002    0.000 {range}


7 function calls in 0.004 seconds

Ordered by: standard name

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    1    0.000    0.000    0.004    0.004 <string>:1(<module>)
    1    0.000    0.000    0.003    0.003 test.py:26(candidateGetOrientationAndMagnitude)
    2    0.002    0.001    0.002    0.001 {cv2.Sobel}
    1    0.000    0.000    0.000    0.000 {cv2.magnitude}
    1    0.001    0.001    0.001    0.001 {cv2.phase}
    1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

{% endhighlight %}

So 1.022s to 0.004, 255&times; faster with just replacing a double `for` loop with an OpenCV call.
