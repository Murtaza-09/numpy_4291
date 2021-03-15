
from PIL import Image
from numpy import asarray 

img= Image.open("num4291.jpg")
numpydata = asarray(img) 


print(numpydata)
def crop_center(img,cropx,cropy):
    y,x,c = img.shape
    startx = x//2 - cropx//2
    starty = y//2 - cropy//2    
    return img[starty:starty+cropy, startx:startx+cropx, :]

im2=crop_center(numpydata,750,750)
print(im2)

img = Image.fromarray(im2, 'RGB')
img.save('my.png')
img.show()

