# Testing Plan

## Scope

The application has three main components, which will all be tested. They are:
1. The classification model
2. The app frontend. This will be a page that  displays a map of Anchorage that shows road conditions and camera information.
3. The app backend. This includes Python code to pull images from cameras and run classification, as well as a node.js api for serving information (images, road conditions, image metadata) to the client.


## Objective

### Classification model
The test objective for the classification model is to determine that it is usefully accurate. This will be done in two steps:
1. Training evaluation - how well the model performs on the training data, including:
    a. Overall accuracy on the training set
    b. Accuracy per class on the training set

3. Generalization evaluation - how well the model performs on unseen images pulled from different webcams. 
    a. Overall accuracy on the validation set
    b. Accuracy per class on the validation set
    c. Accuracy per image source on the validation set (time permitting)

### App frontend
The objective for testing the frontent is to be sure that the page displays as intended, is responsive to programmed inputs, and updates regularly as new images are classified.


### App backend
The objective for testing the backend is to verify that the various backend components work as intended. This includes:
1. The server can pull an image from a camera in its sources list, or report when a camera is down.
2. The server can perform classification on a newly obtained image
3. The /cameras api endpoint is able to report a list of available cameras and their locations to the client
4. the /:camera_id api endpoint provides the latest image and classification for a given camera

## Methodology

### Classification model
Accuracy for both training and validation will be determined using the testing functions that come with TensorFlow and Keras. Results for the final model will be posted.

### App frontend
Manually go through the following checklist of items by loading and interacting with the page:
* page displays map of anchorage at a resolution to show all geomarkers and the map fills the page
* geotags display on map
* geotags are clickable and display an information box when clicked
* information box displays datetime of last update, address of camera, road condition, road condition confidence score
* information box displays an error message when camera has been reported as unreachable
* information box can be collapsed
* information box has icon to display latest image in a popup
* image popup can be collapsed
* information and image are updated on page when updated on server 


### App backend

A shell script will be used to verify that each known camera is reachable. It will also attempt to pull the latest image from that camera and check that it is different from the last image.

Test cases:
* camera down - server reports camera down but still has image and classification from last image from that camera
* image unchanged from last download - server reports that the camera has not been updated, keeps data from latest image
* camera live and updated - server updates latest image, metadata for that camera

A Python script will be used to test that a given image can be classified with reasonable confidence.

Test cases:
* Image classification below confidence threshold - report image as not classifiable
* Image classification meets confidence threshold - update classification for that camera

The api endpoints will be tested using the Jest testing framework.

Test cases:
* GET request to /cameras - get a JSON response containing all avaiable cameras and their locations
* GET request to /:camera_id w/ valid camera_id - get a JSON response containing the latest image, road condition, and datetime of image
* GET request to /:camera_id w/ invalid camera_id - get an "camera id invalid" error response

