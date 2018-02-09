'''
    File to download all images and perform the following operations on them:
        - Download
        - Resize
        - Greyscale
        - Check for uglies and delete them. Noone likes uglies.

    Use python3
'''

import cv2
import urllib.request
import os
import numpy as np

def getImages(url):
    links = urllib.request.urlopen(url).read().decode()
    links = links.split('\n')

    idx = 645
    for link in links:
        try:
            print('[*] Fetching: '+str(link))
            fname = 'neg/'+str(idx)+'.jpg'
            urllib.request.urlretrieve(link,fname)
            img = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)     # Makes image grayscale upon reading.
            rsize = cv2.resize(img, (100,100))
            cv2.imwrite(fname, rsize)
            print('[*] Wrote image: '+fname)
            idx += 1
        except Exception as e:
            print('[!] Error at index: '+str(idx)+'\n'+str(e))

def killUglies():
    '''
        Uglies are the images that are of no use to the training or in anyway useful. 
        The most common example of uglies is a 404 image from flickr. It is one of the uglies we have chosen to be deleted.
    '''
    uglies = os.listdir('uglies')
    imgs = os.listdir('neg')
    for img in imgs:
        for ugly in uglies:
            try:
                cimgp = 'neg/'+str(img)
                ugimg = cv2.imread('uglies/'+str(ugly))
                check = cv2.imread(cimgp)
                if ugimg.shape == check.shape and not (np.bitwise_xor(ugimg, check).any()):
                    # Ugly image detected. Remove it.
                    print('[!] Ugly image detected: '+str(cimgp))
                    print('[!] Deleting image...')
                    os.remove(cimgp)
            except Exception as e:
                print('[-] Error: ' + str(e))


if __name__ == '__main__':
    # URL of image dataset. Obtained from image-net.org. 
    # url = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02715513'
    
    # URL of outdoor images
    url = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n08613733'

    
    # Start getting images
    print('[+] Gathering Images...')
    getImages(url)
    print('[+] Done Gathering Images.')
    
    # Identify and remove all ugly images
    print('[+] Removing ugly images...')
    killUglies()
    print('[+] Done.')
