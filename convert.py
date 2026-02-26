from PIL import Image,ImageOps,ImageEnhance
import cv2
import os
import imgkit
import shutil

# This function reads the video frame by frame and saves it as an image in the "Images" folder. 
# The function returns the frames per second (fps) of the video and the total number of frames extracted.
def video_to_images(path):
    
    if os.path.exists('Images'):
        shutil.rmtree('Images')

    os.mkdir('Images')
    video = cv2.VideoCapture(path)
    fps = video.get(cv2.CAP_PROP_FPS)
    success, image = video.read()
    counter = 1
    
    while success:
        cv2.imwrite("Images/Image{0}.jpg".format(str(counter)), image)
        success, image = video.read()
        counter+=1
    
    return fps, (counter-1)

# This function opens the image, resizes the width to 105% of its original
def get_image(image_path):
    initial_image = Image.open(image_path)
    width,height = initial_image.size
    initial_image = initial_image.resize((round(width*1.05),height))
    return initial_image 

# This function pixelates the image by resizing it to a smaller size and then resizing it back to the original size.
def pixelate_image(image, final_width = 75):
    width, height = image.size
    final_height = int(height*(final_width/width))
    image = image.resize((final_width,final_height))
    return image

# This function converts the image to grayscale using the ImageOps.grayscale() method from the PIL library.
def grayscale_image(image):
    image_bw = ImageOps.grayscale(image)
    return image_bw

# This function converts the monochrome image into brightness values and appends ascii based on this. 
# It returns a list of ascii characters that represent the image.
def ascii_conversion(bw_image,ascii_string = [" ",".",":","-","=","+","*","#","%","@","&"]): 
    pixels = bw_image.getdata()
    ascii_image_list = []

    for pixel in pixels:
        ascii_converted = int(len(ascii_string) * (pixel/256))
        ascii_image_list.append(ascii_string[ascii_converted])
    
    return ascii_image_list

# Creates a list with the RGB value for each pixel
def get_color(image):
    pixels = image.getdata()
    return pixels

# Requires the list of the ASCII characters, the pixelated image, the color list created, and the position of the image in the video
# Creates HTML files for each image with the ASCII characters colored according to the original image
def print_ascii(ascii_list, image, color,image_pos):
    file = open('HtmlImages/Html{0}.html'.format(str(image_pos)),"w")
    file.write("""
               <!DOCTYPE html>
               <html>
               <body style='background-color:black'>
               <pre style='display: inline-block; border-width: 4px 6px; border-color: black; border-style: solid; background-color:black; font-size: 32px ;font-face: Montserrat;font-weight: bold;line-height:60%'>
               """)
    width, height = image.size
    counter = 0
    
    # loop through each ascii character and writes it in the HTML with the corresponding colour
    for j in ascii_list:
        # convert the RGB value to a hex value for the HTML
        color_hex = '%02x%02x%02x' % color[counter]
        counter+=1
        if (counter % width) != 0:
            file.write("<span style=\"color: #{0}\">{1}</span>".format(color_hex,j))
        else:
            file.write("<br />")

    file.write("""</pre></body>
               </html>""")
    file.close()

def main(video_path):
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    
    config = imgkit.config(wkhtmltoimage='/usr/local/bin/wkhtmltoimage')
    ascii_string = [" ",".",":","-","=","+","*","#","%","@","&"]

    fps, frames = video_to_images(video_path)
    
    # create folders
    for folder in ['HtmlImages', 'TextImages']:
        if os.path.exists(folder):
            shutil.rmtree(folder)
        os.mkdir(folder)
    
    # loop through each image frame, convert to ASCII and save as HTML
    for i in range(1, frames+1):
        image = get_image('Images/Image{0}.jpg'.format(str(i)))
        right_size_image = pixelate_image(image)
        
        # retrieve monochrome, ascii and colour list
        bw_image = grayscale_image(right_size_image)
        converted_list = ascii_conversion(bw_image, ascii_string)
        color_list = get_color(right_size_image)
        
        # create the HTML file for the image with the coloured ascii
        print_ascii(converted_list, right_size_image,color_list,i)
        
        # convert HTML into a photo
        imgkit.from_file('HtmlImages/Html{0}.html'.format(str(i)), 'TextImages/Image{0}.jpg'.format(str(i)), config = config)

    res = Image.open('TextImages/Image1.jpg').size
    video = cv2.VideoWriter('final_{0}.mp4'.format(video_name),cv2.VideoWriter_fourcc('m', 'p', '4', 'v'),int(fps),res)

    for j in range(1, frames+1):
        video.write(cv2.imread('TextImages/Image{0}.jpg'.format(str(j))))
    
    video.release()

main("video/example.mp4")