from rembg import remove
from PIL import Image

# Replace 'Add Image URL' with the actual URL or file path of your image
input_path = 'your_image.jpg'
output_path = 'r.png'

input_image = Image.open(input_path)
output_image = remove(input_image)
output_image.save(output_path)
