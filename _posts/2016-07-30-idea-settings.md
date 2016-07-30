---
layout: single
title: Better IDEA Keymap
categories: [lamp,english]
tags: [hardware,video]
---

Completely overhauled keyboard shortcuts for Intellij IDEA on macOS.

---

## Boring ramblings (skip)

First of all I really want to shout out to Intellij for building such awesome tools.
I used Eclipse, Netbeans, Visual Studio but they all suck tremendously. OK, Eclipse
and Netbeans are OSS, so you can live with that. But VS? Its almost cruel how shitty
it is. It is so shitty that Intellij made a plugin to fix it. With the plugin its good.
But costs > $1000 for professional use. Its shameful, really.

IDEA is fantastic, it starts quickly, doesn't freeze up, offers all these advanced
features, code completions, rewrites and so on. I really recommend it to everyone.

And it has a community version which is free and paid version is well worth its money.
I pay monthly subscription for my PyCharm.

So why would I ramble about it in the first place? IDEA has not one but 3 shortcut sets:

* Mac OS X 10.5+ (⌃R for Run) - Not very macOS-like
* Mac OS X (F10 for Run) - WTF?
* Eclipse (Mac OS X) (⌘⇧F11 for Run) - ?????

These are just some examples, but generally the keymaps are this stupid overall.
I genuinely wonder who came up with these. F keys on macOS have been traditionally
used for media keys, screen dimming and such. I do not want to use Fn modifier for
that, and I sure as hell will not type Fn⌘⇧F11 just to Run my code, which is probably
the most common action I need a shortcut for. Stupid.

## Guiding Principles

I wanted my shortcuts to be as usable as possible, so I tried to keep to these rules:

* One handed shortcuts for the most common actions
* Two handed only if it is inevitable
* Ideally Left hand, since most people will use the mouse with the right
* Do not interfere with existing macOS shortcuts
* Try to use popular shortcuts from other editors (Atom, Sublime)

## Disclaimers and limitations

* I mainly work with Scala and Python, so the shortcuts are optimized for IDEA
and PyCharm, but I'm sure they can be used in other Intellij products.
* The multiple selection shortcut could annoy some people, because ⌘Click is
mapped to documentation or something like that by default

## Show me the shortcuts!

Multiple cursors:

* ⌘Click to place an additional cursor
* ⌘D to select the next occurrence of a selected word (same as in Atom/Sublime Text)
* Esc to cancel selection

Running tests:

* Assuming you are using a testing framework like ScalaTest
* Place cursor into the body of the test function/method/describe/it block
* If this is the first time you’re running this test (or if you have run a different test previously) start with:
    * ⌘⇧R to run the test
    * ⌘⇧T to run the test with debugger
* If this is already the second time you’re running this same test/suite:
    * ⌘R to run the test
    * ⌘T to run the test with debugger
* ⌘E while stopped in the debugger
* ⌘. to stop run/test/other running process
* ⌘[ to Step Over in the Debugger
* ⌘] to Step Into in the Debugger
* ⌘\ to Step Out in the Debugger

Navigation Around IDE:

* ⌘P Search Symbols
* ⌘⇧P Search Classes
* ⌘B Jump to definition

Navigation In the Editor:

* ⌥→ and ⌥← To move one word at a time
* ⌥⌃→ and ⌥⌃← To move one word at a time, respecting CamelHumps
* ⌥⇧→ and ⌥⇧← To select one word at a time
* ⌥⇧⌃→ and ⌥⇧⌃← To select one word at a time, respecting CamelHumps
* ⌥⌫ Delete Line

Other shortcuts:

* ⌘5 to Make/Build project, this is useful if you need to see if your project compiles
* ⇧⇧ Search Everything
* ⌘⇧A Search in actions
* ⌘, Preferences

## Download

* [My Entire IDEA Settings JAR]({{ site.baseurl }}/files/2016-07-30-idea/settings.jar)
* [Keymaps Only JAR]({{ site.baseurl }}/files/2016-07-30-idea/keymaps-only.jar)

## Share

Please take these shortcuts, use them, improve on them, share the changes. Maybe
we can convince Intellij to adopt them for the next IDEA Release.

[//]: ⌃⌘⌥⇧← ↑ → ↓⌫
