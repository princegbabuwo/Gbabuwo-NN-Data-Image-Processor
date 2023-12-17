# Gbabuwo-NN-Data-Image-Processor
The scope of this project has evolved and I have decided to write an application that would process my data in the raw folder to a consitent data structure that will be feed into my Neural Network.

# PSEUDOCODE
1. get list of all files in the raw folder
2. Compare list in raw folder to processed list
 - Remove processed files already recorded to Cat Mapper processed list then work with the remaining files on raw list
3. View file and take necessary actions to process file

# How the App Works
1. Supply a file location where raw files are saved
2. The application shows returns individual media file from a list of unprocessed files
3. The user tells whether its a cat-face image, a dog-face image or neither
4. The application compressed the image into a 64 x 64 px image
5. The rgb matrix of the data is collected and stored as column vector along side other meta-data information that tell which of the files has been processed, and how they identify as a cat-face or dog-face image.
6. This data is stored in a file in a folder created into the raw files folder