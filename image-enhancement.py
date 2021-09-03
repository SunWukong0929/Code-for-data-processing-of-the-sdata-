from PIL import Image
from PIL import ImageEnhance
 
# read image
image = Image.open('timg.jpg')
# image.show()
 

# contrast enhancement
enh_con = ImageEnhance.Contrast(image)
contrast = 1.5
image_contrasted = enh_con.enhance(contrast)
# image_contrasted.show()
image_contrasted.save("contrast_test.jpg")
 
# Sharpness enhancement
enh_sha = ImageEnhance.Sharpness(image)
sharpness = 2
image_sharped = enh_sha.enhance(sharpness)
# image_sharped.show()
image_sharped.save("sharpness_test.jpg")
