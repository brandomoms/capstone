## Data
![Image](https://webcams.borealisbroadband.net/shipcreek/shipcreekmega.jpg)
Sample image, Ship Creek Bridge (Downtown)

**Cameras**   
The data was collected from street cameras hosted by Borealis Broadband which are setup in and around Anchorge. Most of these cameras capture new images as frequently as once every five minutes. This is very useful as it means 1) a large volume of data can be scraped 2) this high temporal resolution can provide a lot of useful information e.g. how pixel values change for images of a plowed street as it begins to snow.

The images from the cameras have a resolution of 960 X 1280 pixels, where each pixel is 3 bytes (1 byte per color channel).

**Classes**  
The different classes were selected based on how easily the images could be visually categorized. For example, snow/slush are a single category because it is difficult to distinguish between the two in an image. The classes are:
1. Track - Any other condition but with clear ruts in the road that expose either pavement or black ice
2. Snow/Slush
3. Ice
4. Clear - no snow, ice, or slush. May be wet or dry.
5. Unknown - images that could not be classified. These are not used in training or analysis.

The classes are not mutually exclusive, any image may be tagged as 1 or more of the above classes.

Examples:
1. Track
![Image](example_images/track.jpg)
2. Snow/Slush
![Image](example_images/snowslush.jpg)
3. Ice
![Image](example_images/ice.jpg)
5. Clear
![Image](example_images/clear.jpg)
6. Unknown
![Image](example_images/unknown.jpg)


**Current data set**  
Currently there are 452 usable (not labelled as unknown) training images, but over half of them are images of roads with track. I want to assemble a training set that is equally representative of each class, so I intend to collect more images of icy and clear roads so that I can have at least 150 images per class.

  
