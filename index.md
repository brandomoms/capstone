## Road Condition Classification in Anchorage

## Project Overview

The purpose of this project is to use openly available imagery to automatically determine winter road conditions (clear pavement, slush, snow, etc.). Classification will be done using a Convolutional Neural Net trained on the image set. 

Once the classifier is trained, an automated process will be created to regularly pull images from their source, run the classification, and update a map of Anchorage (to be added to this page) to display road conditions at various sites. 

## Data
The data was collected from street cameras hosted by Borealis Broadband, and will include images of the Potter's Marsh weigh station, the Glenn Hwy weigh station, the Midtown Mall, and four downtown sites. Most of these cameras capture new images as frequently as once every five minutes. This is very useful as it means 1) a large volume of data can be scraped 2) this high temporal resolution can provide a lot of useful information e.g. how pixel values change for images of a plowed street as it begins to snow.

![Image](https://webcams.borealisbroadband.net/shipcreek/shipcreekmega.jpg)
Sample image, Ship Creek Bridge (Downtown)

## Manual Classification
Training a supervised classifier requires the input data to be labelled with the appropriate classes, and this had to be done manually. Labelling the data is tricky, it is not obvious from an overhead image what the exact road conditions are...

## Timeline
Item | Status | Completion Date
-----|--------|----------------
Scrape training data from Borealis Broadband | done ✅ | ongoing, preliminary training set by Feb 8
Create pixel map for each camera for determining road location and ignoring irrelevent pixels | done ✅ | Feb 11
Manually label training images | done ✅ | ongoing, preliminary training set by Feb 8
Upload notebook detailing data exploration/analysis/visualization | working 🚧 | March 2
Train multiclass classifier and post preliminary results | not started ❌ | March 16
Add map of Anchorage to this page with geotags for each camera | not started ❌ | March 23
Automate process of scraping images from borealis broadband, performing classification, and updating geotag labels on the map | not started ❌ | March 30
Tune classifier and work to improve accuracy, post final results | not started ❌ | End of semester

