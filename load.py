from PIL import Image





img = Image.open("screenshot_0.png")
# cropped = img.crop((0,0,1280,800))
cropped = img.crop((911,415,966,430))
cropped.save("green.png")


