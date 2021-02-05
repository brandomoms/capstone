## Road Condition Classification in Anchorage

## Project Overview

The purpose of this project is to use openly available imagery to automatically determine winter road conditions (clear pavement, plowed, slush, snow, ice, etc.). Classification will be done using a Convolutional Neural Net trained on the image set. 

Once the classifier is trained, an automated process will be created to regularly pull images from their source, run the classification, and update a map of Anchorage (to be added to this page) to display road conditions at various sites. 

## Data
The data will come from street cameras hosted by Borealis Broadband, and will include images of the Potter's Marsh weigh station, at least three downtown sites, and at least one midtown site. Most of these cameras capture new images as frequently as once every five minutes. This is very useful as it means 1) a large volume of data can be scraped 2) this high temporal resolution can provide a lot of useful information e.g. how pixel values change for images of a plowed street  as it begins to snow.

![Image](https://webcams.borealisbroadband.net/shipcreek/shipcreekmega.jpg)
Sample image, Ship Creek Bridge (Downtown)

## Timeline
Item | Status | Completion Date
-----|--------|----------------
Scrape training data from Borealis Broadband | working | ongoing, preliminary training set by Feb 8
Create pixel map for each camera for determining road location and ignoring irrelevent pixels | working | Feb 11
Manually label training images | not started | ongoing, preliminary training set by Feb 8
Train multiclass classifier and post preliminary results | not started | March 1
Add map of Anchorage to this page with geotags for each camera | not started | March 8
Automate process of scraping images from borealis broadband, performing classification, and updating geotag labels on the map | not started | March 21
Tune classifier and add optimizations to improve accuracy, post final results | not started | End of semester

