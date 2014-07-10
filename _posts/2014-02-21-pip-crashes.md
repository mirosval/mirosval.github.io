---
layout: single
title: Python Pip Crashes
categories: [python,english]
tags: [python]
---

I was upgrading my disk to SSD the other day, and to make sure all my data fit, I've done some
cleaning up, among others I've run `brew cleanup` which deletes old formulae. But apparently
somewhere along the way that has broken my Python install. Trying to run Flask server would produce
a cryptic error:

{% highlight text %}
ImportError: No module named itsdangerous
{% endhighlight %}

Hmm okay, lets try to install it:

{% highlight text %}
 % pip3 install itsdangerous
    Downloading/unpacking itsdangerous
    Downloading itsdangerous-0.23.tar.gz (46kB): 46kB downloaded
    [1]    48739 segmentation fault  pip3 install itsdangerous
{% endhighlight %}

Mmmkaay, what? I've tried to reinstall python to no avail, the search did not show anything either...
The segfault looked like this:

{% highlight text %}
Process:         Python [61249]
Path:            /usr/local/Cellar/python3/3.3.4/Frameworks/Python.framework/Versions/3.3/Resources/Python.app/Contents/MacOS/Python
Identifier:      Python
Version:         3.3.4 (3.3.4)
Code Type:       X86-64 (Native)
Parent Process:  sudo [61248]
Responsible:     Terminal [416]
User ID:         0

Date/Time:       2014-02-21 12:35:15.725 +0100
OS Version:      Mac OS X 10.9.1 (13B42)
Report Version:  11

Crashed Thread:  0  Dispatch queue: com.apple.main-thread

Exception Type:  EXC_BAD_ACCESS (SIGSEGV)
Exception Codes: KERN_INVALID_ADDRESS at 0x0000000000000011

VM Regions Near 0x11:
--> 
    __TEXT                 00000001084d7000-00000001084d9000 [    8K] r-x/rwx SM=COW  /usr/local/Cellar/python3/3.3.4/Frameworks/Python.framework/Versions/3.3/Resources/Python.app/Contents/MacOS/Python

Thread 0 Crashed:: Dispatch queue: com.apple.main-thread
0   libcrypto.1.0.0.dylib           0x0000000108f6d1ac EVP_PKEY_CTX_dup + 28
1   libcrypto.1.0.0.dylib           0x0000000108f61565 EVP_MD_CTX_copy_ex + 325
2   _hashlib.so                     0x0000000108e88933 locked_EVP_MD_CTX_copy + 78
3   _hashlib.so                     0x0000000108e887f0 EVP_hexdigest + 51
4   org.python.python               0x0000000108570bd2 PyEval_EvalFrameEx + 16052
5   org.python.python               0x000000010857512d fast_function + 186
6   org.python.python               0x0000000108570c92 PyEval_EvalFrameEx + 16244
7   org.python.python               0x000000010857512d fast_function + 186
8   org.python.python               0x0000000108570c92 PyEval_EvalFrameEx + 16244
9   org.python.python               0x000000010857512d fast_function + 186
10  org.python.python               0x0000000108570c92 PyEval_EvalFrameEx + 16244
11  org.python.python               0x000000010857512d fast_function + 186
12  org.python.python               0x0000000108570c92 PyEval_EvalFrameEx + 16244
13  org.python.python               0x000000010857512d fast_function + 186
14  org.python.python               0x0000000108570c92 PyEval_EvalFrameEx + 16244
15  org.python.python               0x000000010857512d fast_function + 186
16  org.python.python               0x0000000108570c92 PyEval_EvalFrameEx + 16244
17  org.python.python               0x000000010856cb93 PyEval_EvalCodeEx + 1579
18  org.python.python               0x00000001085751a2 fast_function + 303
19  org.python.python               0x0000000108570c92 PyEval_EvalFrameEx + 16244
20  org.python.python               0x000000010856cb93 PyEval_EvalCodeEx + 1579
21  org.python.python               0x00000001085751a2 fast_function + 303
22  org.python.python               0x0000000108570c92 PyEval_EvalFrameEx + 16244
23  org.python.python               0x000000010857512d fast_function + 186
24  org.python.python               0x0000000108570c92 PyEval_EvalFrameEx + 16244
25  org.python.python               0x000000010857512d fast_function + 186
26  org.python.python               0x0000000108570c92 PyEval_EvalFrameEx + 16244
27  org.python.python               0x000000010857512d fast_function + 186
28  org.python.python               0x0000000108570c92 PyEval_EvalFrameEx + 16244
29  org.python.python               0x000000010856cb93 PyEval_EvalCodeEx + 1579
30  org.python.python               0x0000000108506099 function_call + 345
31  org.python.python               0x00000001084ea67a PyObject_Call + 111
32  org.python.python               0x0000000108571486 PyEval_EvalFrameEx + 18280
33  org.python.python               0x000000010856cb93 PyEval_EvalCodeEx + 1579
34  org.python.python               0x00000001085751a2 fast_function + 303
35  org.python.python               0x0000000108570c92 PyEval_EvalFrameEx + 16244
36  org.python.python               0x000000010856cb93 PyEval_EvalCodeEx + 1579
37  org.python.python               0x00000001085751a2 fast_function + 303
38  org.python.python               0x0000000108570c92 PyEval_EvalFrameEx + 16244
39  org.python.python               0x000000010856cb93 PyEval_EvalCodeEx + 1579
40  org.python.python               0x00000001085751a2 fast_function + 303
41  org.python.python               0x0000000108570c92 PyEval_EvalFrameEx + 16244
42  org.python.python               0x000000010856cb93 PyEval_EvalCodeEx + 1579
43  org.python.python               0x000000010856c562 PyEval_EvalCode + 63
44  org.python.python               0x000000010858d6cf run_mod + 58
45  org.python.python               0x000000010858d8e4 PyRun_FileExFlags + 142
46  org.python.python               0x000000010858d1b9 PyRun_SimpleFileExFlags + 875
47  org.python.python               0x000000010859eaab Py_Main + 3123
48  org.python.python               0x00000001084d8e3f 0x1084d7000 + 7743
49  libdyld.dylib                   0x00007fff91ea55fd start + 1

Thread 1:
0   libsystem_kernel.dylib          0x00007fff98b49e6a __workq_kernreturn + 10
1   libsystem_pthread.dylib         0x00007fff8d74af08 _pthread_wqthread + 330
2   libsystem_pthread.dylib         0x00007fff8d74dfb9 start_wqthread + 13

Thread 2:: Dispatch queue: com.apple.libdispatch-manager
0   libsystem_kernel.dylib          0x00007fff98b4a662 kevent64 + 10
1   libdispatch.dylib               0x00007fff9363143d _dispatch_mgr_invoke + 239
2   libdispatch.dylib               0x00007fff93631152 _dispatch_mgr_thread + 52

Thread 3:
0   libsystem_kernel.dylib          0x00007fff98b49e6a __workq_kernreturn + 10
1   libsystem_pthread.dylib         0x00007fff8d74af08 _pthread_wqthread + 330
2   libsystem_pthread.dylib         0x00007fff8d74dfb9 start_wqthread + 13

Thread 0 crashed with X86 Thread State (64-bit):
  rax: 0x0000000000000001  rbx: 0x00007fff57726b00  rcx: 0x0000000000000010  rdx: 0xffffffffffffffd4
  rdi: 0x00007fe6ca7bde20  rsi: 0x00007fe6ca60d490  rbp: 0x00007fff57726a90  rsp: 0x00007fff57726a70
   r8: 0x0000000000000006   r9: 0x00007fe6ca400000  r10: 0x0000000069793538  r11: 0xffffffffffe9b3a0
  r12: 0x00007fff7c009400  r13: 0x00000001092c0f38  r14: 0x00007fe6ca7bde20  r15: 0x0000000000000000
  rip: 0x0000000108f6d1ac  rfl: 0x0000000000010202  cr2: 0x0000000000000011
 
{% endhighlight %}

So libcrypto.dylib is at fault here... Lets see, Homebrew has an option to use Python
with brewed OpenSSL instead:

{% highlight text %}
  % brew info python3

python3: stable 3.3.4, HEAD
http://www.python.org/
Not installed
From: https://github.com/Homebrew/homebrew/commits/master/Library/Formula/python3.rb
==> Dependencies
Build: pkg-config ✔
Recommended: readline ✔, sqlite ✔, gdbm ✔, xz ✔
==> Options
--quicktest
    Run `make quicktest` after the build
--universal
    Build a universal binary
--with-brewed-openssl
    Use Homebrew's openSSL instead of the one from OS X
--with-brewed-tk
    Use Homebrew's Tk (has optional Cocoa and threads support)
--without-gdbm
    Build without gdbm support
--without-readline
    Build without readline support
--without-sqlite
    Build without sqlite support
--without-xz
    Build without xz support
--HEAD
    install HEAD version
==> Caveats
Setuptools and Pip have been installed. To update them
  pip3 install --upgrade setuptools
  pip3 install --upgrade pip

You can install Python packages with
  `pip3 install <your_favorite_package>`

They will install into the site-package directory
  /usr/local/lib/python3.3/site-packages

See: https://github.com/Homebrew/homebrew/wiki/Homebrew-and-Python

{% endhighlight %}

So I ran:

{% highlight text %}
  % brew uninstall python3
  % brew install python3 --with-brewed-openssl
{% endhighlight %}

And that seemed to do the trick for the pip segfaults, however it did not solve my original
problem. To do that I've uninstalled all of the Flask and related packages using pip3 and then
re-installed them in the virtual environment instead.
