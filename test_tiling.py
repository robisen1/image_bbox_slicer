# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 10:49:13 2020

@author: robi
"""
# slicer package

import image_bbox_slicer.image_bbox_slicer as ibs

#switch from test directory when going live.
# need to rewrite this dudes code to handle basic shit like spaces and periods
# it should at least be a warning in the readme
im_src = './src/images'
an_src = './src/annotations'
im_dst = './dst/images'
an_dst = './dst/annotations'


slicer = ibs.Slicer()
slicer.config_dirs(img_src=im_src, ann_src=an_src,img_dst=im_dst, ann_dst=an_dst)

slicer.keep_partial_labels = True

slicer.ignore_empty_tiles = True
# #save a map of the cut up images to the original
slicer.save_before_after_map = True
# # break up the image into tiles of 512X512 for faster processing.
# # window, input can be 480X480 so there is a over lap

slicer.slice_by_size(tile_size=(512,512), tile_overlap=0)



# slicer.visualize_sliced_random()



