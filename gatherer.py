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

def getImages(url):
    links = urllib.request.urlopen(url).read().decode()
    links = links.split('\n')

    idx = 1
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


if __name__ == '__main__':
    # URL of image dataset. Obtained from image-net.org. 
    url = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02715513'
    
    # Start getting images
    print('[+] Gathering Images...')
    getImages(url)
    print('[+] Done Gathering Images.')
