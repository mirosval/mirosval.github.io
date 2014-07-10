---
layout: single
title: Performance of the unwrapIris()
categories: [master-thesis,english]
tags: [master-thesis,opencv,python,performance]
---

After the performance improvement from yesterday, I wanted to try some more things,
because the speed of this was still not satisfactory (I spent an hour processing 2000 images).

So I've whipped up line_profiler again:

{% highlight bash %}
kernprof.py -l main.py && python -m line_profiler main.py.lprof
{% endhighlight %}

This gave me the following trace:

{% highlight text %}
File: main.py
Function: main at line 10
Total time: 23.1351 s

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    10                                           @profile
    11                                           def main():
    12         1       167798 167798.0      0.7      cv2.namedWindow("Eye")
    13         1        28931  28931.0      0.1      cv2.namedWindow("Iris")
    14                                           
    15         1        21107  21107.0      0.1      cv2.moveWindow("Eye", 0, 0)
    16         1        27887  27887.0      0.1      cv2.moveWindow("Iris", 800, 0)
    17                                           
    18         1            6      6.0      0.0      i = 0
    19        12       247887  20657.2      1.1      for f in os.listdir(data_dir):
    20        12       240693  20057.8      1.0          image = cv2.imread(os.path.join(data_dir, f))
    21        12          106      8.8      0.0          if image is None:
    22         1            3      3.0      0.0              continue
    23                                           
    24        11        31933   2903.0      0.1          gray = cv2.cvtColor(image, cv2.cv.CV_BGR2GRAY)
    25                                           
    26        11       179806  16346.0      0.8          pupil = functions.findPupil(gray, show=True)
    27                                           
    28        11           51      4.6      0.0          if not pupil:
    29                                                       print("No pupil found")
    30                                                       continue
    31                                           
    32        11           39      3.5      0.0          center, ellipse = pupil
    33                                           
    34        11           33      3.0      0.0          pupil_width = ellipse[1][0]
    35                                           
    36        11      1755948 159631.6      7.6          iris_radius = functions.findIris(gray, center, pupil_width, pupil_ellipse=ellipse, show=True)
    37        11           77      7.0      0.0          if iris_radius > 0:
    38        11     20144018 1831274.4     87.1              polar = functions.unwrapIris(gray, center, iris_radius, show=True)
    39                                           
    40        11        51121   4647.4      0.2              cv2.imwrite(os.path.join(dest_dir, f.replace('.png', '') + "_polar.png"), polar)
    41        11          369     33.5      0.0              print("Written %s" % f)
    42                                           
    43        11       237059  21550.8      1.0          if cv2.waitKey(1) == ord('q'):
    44                                                       break
    45                                           
    46        11          108      9.8      0.0          if i == 10:
    47         1           61     61.0      0.0              break
    48                                           
    49        10           37      3.7      0.0          i += 1
{% endhighlight %}

Hmmm, 87% of the time is spent in `unwrapIris()`. Lets take a look at what that looks like:

{% highlight python linenos %}
def unwrapIris(image, iris_center, iris_radius, nsamples=360, show=False):
    samples = np.linspace(0, 2 * np.pi, nsamples)[:-1]
    polar = np.zeros((iris_radius, nsamples), dtype=np.uint8)

    for r in range(iris_radius):
        for theta in samples:
            x = r * np.cos(theta) + iris_center[0]
            y = r * np.sin(theta) + iris_center[1]
            try:
                polar[r][theta * nsamples / 2.0 / np.pi] = image[y][x]
            except IndexError:
                polar[r][theta * nsamples / 2.0 / np.pi] = 0

    if show:
        cv2.imshow("Iris", polar)

    return polar
{% endhighlight %}

And its profile:

{% highlight text %}
File: functions.py
Function: unwrapIris at line 145
Total time: 34.5483 s

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
   145                                           @profile
   146                                           def unwrapIris(image, iris_center, iris_radius, nsamples=360, show=False):
   147        11         1305    118.6      0.0      samples = np.linspace(0, 2 * np.pi, nsamples)[:-1]
   148        11          294     26.7      0.0      polar = np.zeros((iris_radius, nsamples), dtype=np.uint8)
   149                                           
   150      1331         4389      3.3      0.0      for r in range(iris_radius):
   151    475200      1935876      4.1      5.6          for theta in samples:
   152    473880     10479969     22.1     30.3              x = r * np.cos(theta) + iris_center[0]
   153    473880     10187509     21.5     29.5              y = r * np.sin(theta) + iris_center[1]
   154    473880      1476839      3.1      4.3              try:
   155    473880     10431987     22.0     30.2                  polar[r][theta * nsamples / 2.0 / np.pi] = image[y][x]
   156                                                       except IndexError:
   157                                                           polar[r][theta * nsamples / 2.0 / np.pi] = 0
   158                                           
   159        11           28      2.5      0.0      if show:
   160        11        30015   2728.6      0.1          cv2.imshow("Iris", polar)
   161                                           
   162        11           52      4.7      0.0      return polar
{% endhighlight %}

So we can see that the load here is distributed between 3 lines, 2 trigonometric calculations
and one array access and some arithmetic. But the main problem is that these 3 lines are run for
each pixel, for 10 images processed in this sample this is 475 200 hits. If I have learned anything
about Python performance in the past year, it is to move all loops to an external library if possible.
In this case we'll look at how could this be moved over to either Numpy or OpenCV. Since these
libraries are written in C or C++, they can perform the same loop much faster than plain Python.

Thanks to Numpy's operator overloading, it is possible to write code that looks really weird at the
first glance, if you're used to loops from other languages. Look at the lines 6 and 7. `magnitude`
is an array, `angle` is an array and `iris_center` is an `int` as it is used here. Numpy can
calculate this correctly and the loops are now in the library, yay!

So what changed? Line 4 makes two arrays, one with angles and one with magnitudes, both of dimensions
`iris_radius&times;nsamples` which is about `359x130` for most of my images. The angle array is
basically just a single row of radian values from 0 to 2pi repeated 130 times, and magnitude is
a column from 0 to 129 repeated horizontally 359 times.

The lines 6 and 7 convert these two arrays to X,Y coordinates in the image, from which we will be
sampling later. `convertMaps()` converts the them further to improve performance of `cv2.remap()`.
And finally `cv2.remap()` maps these coordinate maps from the original image into the polar image.

{% highlight python linenos %}
def unwrapIris(image, iris_center, iris_radius, nsamples=360, show=False):
    samples = np.linspace(0, 2 * np.pi, nsamples)[:-1]

    angle, magnitude = np.meshgrid(samples, np.arange(iris_radius))

    x = magnitude * np.cos(angle) + iris_center[0]
    y = magnitude * np.sin(angle) + iris_center[1]

    x, y = cv2.convertMaps(x.astype('float32'), y.astype('float32'), cv2.CV_32FC1)
    return cv2.remap(image, x, y, cv2.INTER_LINEAR)
{% endhighlight %}

And now lets take a look at what that did to the performance:

{% highlight text %}
File: functions.py
Function: unwrapIris at line 145
Total time: 0.090496 s

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
   145                                           @profile
   146                                           def unwrapIris(image, iris_center, iris_radius, nsamples=360, show=False):
   147        11         1445    131.4      1.6      samples = np.linspace(0, 2 * np.pi, nsamples)[:-1]
   148                                           
   149        11        11660   1060.0     12.9      angle, magnitude = np.meshgrid(samples, np.arange(iris_radius))
   150                                           
   151        11        30335   2757.7     33.5      x = magnitude * np.cos(angle) + iris_center[0]
   152        11        29815   2710.5     32.9      y = magnitude * np.sin(angle) + iris_center[1]
   153                                           
   154        11         5195    472.3      5.7      x, y = cv2.convertMaps(x.astype('float32'), y.astype('float32'), cv2.CV_32FC1)
   155        11        12046   1095.1     13.3      return cv2.remap(image, x, y, cv2.INTER_LINEAR)

File: main.py
Function: main at line 10
Total time: 3.99889 s

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    10                                           @profile
    11                                           def main():
    12         1       160876 160876.0      4.0      cv2.namedWindow("Eye")
    13         1        11790  11790.0      0.3      cv2.namedWindow("Iris")
    14                                           
    15         1        26153  26153.0      0.7      cv2.moveWindow("Eye", 0, 0)
    16         1        25946  25946.0      0.6      cv2.moveWindow("Iris", 800, 0)
    17                                           
    18         1            9      9.0      0.0      i = 0
    19        12         3073    256.1      0.1      for f in os.listdir(data_dir):
    20        12        88505   7375.4      2.2          image = cv2.imread(os.path.join(data_dir, f))
    21        12          124     10.3      0.0          if image is None:
    22         1            4      4.0      0.0              continue
    23                                           
    24        11         9028    820.7      0.2          gray = cv2.cvtColor(image, cv2.cv.CV_BGR2GRAY)
    25                                           
    26        11        38994   3544.9      1.0          pupil = functions.findPupil(gray, show=True)
    27                                           
    28        11          187     17.0      0.0          if not pupil:
    29                                                       print("No pupil found")
    30                                                       continue
    31                                           
    32        11           68      6.2      0.0          center, ellipse = pupil
    33                                           
    34        11           63      5.7      0.0          pupil_width = ellipse[1][0]
    35                                           
    36        11      3202228 291111.6     80.1          iris_radius = functions.findIris(gray, center, pupil_width, pupil_ellipse=ellipse, show=True)
    37        11          100      9.1      0.0          if iris_radius > 0:
    38        11        91645   8331.4      2.3              polar = functions.unwrapIris(gray, center, iris_radius, show=True)
    39                                           
    40        11        28406   2582.4      0.7              cv2.imwrite(os.path.join(dest_dir, f.replace('.png', '') + "_polar.png"), polar)
    41        11          563     51.2      0.0              print("Written %s" % f)
    42                                           
    43        11       310859  28259.9      7.8          if cv2.waitKey(1) == ord('q'):
    44                                                       break
    45                                           
    46        11          120     10.9      0.0          if i == 10:
    47         1           92     92.0      0.0              break
    48                                           
    49        10           57      5.7      0.0          i += 1
{% endhighlight %}

Nice! Now `unwrapIris()` is taking just 2.3% of the total time! And we have reduced time needed to process
10 images from ~34s to about 4s, that's an order of magnitude improvement! Now the `findIris()` is the 
slowest, maybe next time we'll look at that.
