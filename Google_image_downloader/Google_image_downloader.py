from icrawler.builtin import GoogleImageCrawler

from icrawler.builtin import BingImageCrawler
import os
from pathlib import Path

escape_key="1"  ##initial value of pressed key
while(True):

	escape_key = str(input("Enter a 0 to exit: "))
	if(escape_key=="0"): ##if pressed key is 0, the program stops
		break
	
	collection = os.getcwd()+"\\" ##actual directory to save collection of images
	images_to_download = int(input("Enter a number of images you want to download: ")) ##number of images to download
	

	
	word = str(input("Enter a name: ")) ##topic of the images
	
	

	

	google_Crawler = GoogleImageCrawler(storage = {'root_dir': r'H:\Videojuegos'}) ##google image crawler to search images with the corresponding topic
	google_iterator = google_Crawler.crawl(keyword = word, max_num = images_to_download)

	if google_iterator is None: ##if google seach fails
		bing_Crawler = BingImageCrawler(storage = {'root_dir': r'H:\Videojuegos'}) ##bing image crawler to search images with the corresponding topic
		bing_iterator = bing_Crawler.crawl(keyword = word, max_num = images_to_download)		
	

	
	filename=""
	#images_to_download=100
	for i in range(1,images_to_download+1): ##loop images to change name with the topic word
		filename=str(i).zfill(7-len(str(i)))
		
		if(Path(filename+".jpg").is_file()): ##if image exists yet and it has jpg extension it will be removed
			os.remove(collection + str(word) + str(i) + ".jpg")	
			
		if(Path(filename+".png").is_file()): ##if image exists yet and it has png extension it will be removed
			os.remove(collection + str(word) + str(i) + ".png")				
			
		if(Path(filename+".jpg").is_file()): ##change names of images to the topic word
			if(Path(collection + str(word) + str(i) + ".jpg").is_file()==False):
				os.rename(collection + filename + ".jpg", collection + str(word) + str(i) + ".jpg")
		else:
			if(Path(collection + str(word) + str(i) + ".png").is_file()==False):
				os.rename(collection + filename + ".png", collection + str(word) + str(i) + ".png")
				
				
