import os
from PIL import Image

# Crops the image and saves it as "new_filename"
def crop_image(img, crop_area, new_filename):
    cropped_image = img.crop(crop_area)
    cropped_image.save(new_filename)

# The x, y coordinates of the areas to be cropped. (x1, y1, x2, y2)
crop_areas = []

#image size
image_x = 4608
image_y = 3072

#crop size
crop_x = 512
crop_y = 512

#images path
path = "{imagesPath}"

for i in range(int(image_y/crop_y)):
    for j in range(int(image_x/crop_x)):
        crop_areas.append((j*crop_x,i*crop_y,(j+1)*crop_x,(i+1)*crop_y))

dirs = os.listdir(path)
for item in dirs:
    if os.path.isfile(path + item):
        f, e = os.path.splitext(path + item)
        if e != '.txt':
            image_name = item + '.jpg'
            img = Image.open(path+item)
            for i, crop_area in enumerate(crop_areas):
                filename = os.path.splitext(image_name)[0]
                ext = os.path.splitext(image_name)[1]
                new_filename = f + '_cropped' + str(i) + ext

                crop_image(img, crop_area, new_filename)