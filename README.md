# Medical-Data-Extraction
## Project Objective
The objective of this project is to capture the vital information of a patient from the given patient details files and the prescription files.
## Approach 
Now, let's talk about the process of what happens inside this project.
Take a look at the below flowchart. These are the steps we'll discuss one by one. 


![image](https://github.com/PriyaYalla-7/Medical-Data-Extraction/assets/91936598/2989bba3-cdc5-406d-8c22-fa32e3dd621d)

### 1) convert pdf file into an image file
To apply some image processing techniques and to extract the text better, we convert the PDF file into an image file, using the Python module **pdf2image**.

The **convert_from_path** module in the pdf2image library provides a convenient way to convert PDF file into a list of image objects.

### 2) image processing
For normal images, we can directly extract the text from the image. But for some images, for example, an image of a prescription taken with a phone, but with the shadow of a hand or a phone on the image. The text that falls under the shadow region will not be extracted.

So, we have to do some image processing before extracting the text. For that, we use **OpenCV**. We use the process of thresholding. Thresholding converts a normal image into a grayscale black and white image. 
Generally, there are two types of thresholding. 
1. Simple Thresholding
2. Adaptive Thresholding.

In **Simple Thresholding**, the image is represented as a grid of numbers, starting from 0 to 255. And this Simple Thresholding works well with normal images. 

In **Adaptive Thresholding**, the image is divided into different segments with different thresholds. Contrary to Simple Thresholding, in which we use a global threshold for the whole image, here in Adaptive Thresholding, we divide the image into segments and use different thresholds for different segments.   

### 3) extracting text from image
We extract the text from the image using **pytesseract** module. This module is a Python wrapper for Google's Tesseract OCR engine. It enables developers to easily integrate OCR, which is Optical Character Recognition, capabilities into their Python applications.

### 4) converting text into JSON format
Once the text is extracted, we utilize regular expressions, also known as **regex**, to transform the data into JSON format. 
We write various regular expressions to extract different details of the patient.

-----------------------------------------------------------------------------------------------------------------

***- technologies used :***

💡 pdf2image

💡 opencv

💡 pytesseract

💡 regex

💡 fastapi
