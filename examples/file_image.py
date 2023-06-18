# Load an image from a file and display it
# Import the required module
#import PIL
import PIL
# Import the image class from PIL
from PIL import Image

# Open an image file
image = Image.open("history.jpg")

# Display basic information about the image
print("Image format:", image.format)
print("Image size:", image.size)
print("Image mode:", image.mode)

# Show the image
image.show()

# Save the image in a different format
image.save("history.png")
#here we save the image in png format