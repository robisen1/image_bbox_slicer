# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 12:27:23 2020

@author: robi
"""

# call new main
from pathlib import Path, PurePath
import image_bbox_slicer.image_bbox_slicer

local = PurePath(Path.cwd())

#print(local)

home_path = Path.home()
print(repr(home_path))

