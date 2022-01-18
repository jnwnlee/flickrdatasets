from flickr import get_urls
from downloader import download_images
import os
import time

all_species = ['car', 'car chill', 'chill', 'chill dance', 'chill night', 'chill party',
            'chill summer', 'chill work', 'club', 'dance', 'dance gym', 'dance party',
            'dance summer', 'gym', 'gym party', 'happy', 'night', 'party', 'party running',
            'party summer', 'party work', 'relax', 'running', 'sad', 'sleep', 'summer', 
            'work', 'workout'] 
             
images_per_species = 3000

def download():
    for species in all_species:
        try:
            print('Getting urls for', species)
            urls = get_urls(species, images_per_species)

            print('Downlaing images for', species)
            path = os.path.join('data', species)

            download_images(urls, path)
        except Exception as e:
                print(type(e), e)

if __name__=='__main__':

    start_time = time.time()

    download()

    print('Took', round(time.time() - start_time, 2), 'seconds')
