# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 18:24:28 2021

@author: Ali İhsan Sarı
"""
# Importing Packages
from PIL import Image
import os
import random
import site
import sys


class photo():

    def __init__(self):
        pass

    def resize(self, im_path, x, y):
        image = Image.open(im_path)
        image = image.resize((x, y))
        image.save(f'temp_photo/{im_path.split("/")[-1]}')


class tasks(photo):
    
    progress = 0
    
    def photo_to_pdf(self, paths, separate, savedir="pdf/", name="converted"):
        
        multiple, length = self.multiple(paths)
        
        if multiple and separate:
            try:
                progress_increase = length / 100
            except:
                tasks.progress = 'Bilinmiyor'
            
            for i in range(length):
                
                sdir = savedir+name+str(i)+'.pdf'
                image1 = Image.open(paths[i])
                img1 = image1.convert('RGB')
                
                if os.path.exists(sdir):
                    img1.save(savedir+name+str(i+1)+'.pdf')
                    tasks.progress += progress_increase
                else:
                    img1.save(sdir)
                    tasks.progress += progress_increase
                
                
        elif not multiple:
            
            try:
                progress_increase = length / 100
            except:
                tasks.progress = 'Bilinmiyor'
            
            
            sdir = savedir+name+'.pdf'
            image1 = Image.open(paths[0])
            img1 = image1.convert('RGB')
            
            
            if os.path.exists(sdir):
                img1.save(savedir+sdir+str(random.randint(100,500))+'.pdf')
                tasks.progress += progress_increase
            else:
                img1.save(sdir)
                tasks.progress += progress_increase
            
            
        elif multiple and not separate:
            
            try:
                progress_increase = length / 100
            except:
                tasks.progress = 'Bilinmiyor'
            
            im_list = []
            sdir = savedir+name+'.pdf'
            
            try:
                
                for i, path in enumerate(paths):
                    
                    if i == 0:
                        img = Image.open(path)
                        img = img.convert('RGB')
                        
                    else:
                        i = Image.open(path)
                        im_list.append(i.convert('RGB'))
                
                if os.path.exists(sdir):
                    img.save(savedir+name+str(random.randint(500, 900))+'.pdf', save_all = True, append_images = im_list)
                    tasks.progress += progress_increase
                else:
                    img.save(sdir, save_all = True, append_images = im_list)
                    tasks.progress += progress_increase
                    
            except Exception as e:
                
                print(f'Program hata ile karşılaştı hata:{e}')
            
    
    def multiple(self, paths):
                
        multiple = None
        length = len(paths)
        
        if length > 1:
            multiple = True
        
        else:
            multiple = False
        
        return multiple, length