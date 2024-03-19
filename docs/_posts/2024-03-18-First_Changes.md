---
title: First Changes
date: 2024-03-18 18:00:00 +0100
tags: [bt studio]     # TAG names should always be lowercase
categories: [improvements, visual]
author: javier
img_path: /assets/img/
toc: true
comments: true
---

## Indicator when action or node is selected

As I was trying BT Studio for the first time I was confused about what node I had selected because when I clicked on one it didn't change or anything.

So in order to solve this problem I just added to the already existing click callback and ability to change the action border color and padding making it easier to know which node was selected.

![Before](select_indicator/before.png)
_Before_

![After](select_indicator/after.png)
_After_

## Icons not loading properly in Vivaldi

I do not know if this problem was in general with Chromium based browsers or not because this did not happen with Firefox but it did with Vivaldi.

The solution here was really simple, just change the svg size from 512x512 to 25x25.

![Before](correct_icons_vivaldi/before.png)
_Before_

![After](correct_icons_vivaldi/after.png)
_After_

## Project dropdown list

This allows the user to not need to memorize every single project name and just select in a more visually pleassing way the project that they want to switch to.

Here is the before and after:

![Before and After off](project_list/after_off.png)
_Before and After Off_

![Before On](project_list/before.png)
_Before On_

![After On](project_list/after_on.png)
_After On_
