from time import sleep
from urllib.request import urlopen, urlretrieve

img_count = 0;
while True:
    image_name = "images/" + img_count + ".jpg"
    urlretrieve('http://www.snowgrass.co.nz/cust/otakaro/convention/images/webcam.jpg', image_name)
    img_count += 1
    sleep(16 * 60)