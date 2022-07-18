import pyscreenshot as ImageGrab

if __name__ == '__main__':
    im = ImageGrab.grab(bbox=(1200, 600, 1900, 700))
    im.save('im.png')

#for the itechdevices website we can get the hyperlink of the image from <img> and open that page and use coordinates to capture just the righ amount we need.

#so far it needs to have access of the webpage to take a screenshot. Either it opens the page or take the screenshot of whatever is already opened.
