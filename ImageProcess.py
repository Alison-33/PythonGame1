import pgzrun
from PIL import Image

try:
    im = Image.open('images\\image1.jpg')
except:
    print("Error opening file.")

box = (200, 0, 950, 750)  # the cropping range, left, up, right, down
region = im.crop(box)
w, h = region.size
region.save("images\\image1_crop.jpg")

WIDTH = w
HEIGHT = h
pic = Actor('image1')


def cut_square_image(image, pieces, store_name):
    w, h = image.size
    step = w // pieces
    for i in range(pieces):
        for j in range(pieces):
            box = (i * step, j * step, (i + 1) * step, (j + 1) * step)
            region = image.crop(box)
            path = store_name + str(j * pieces + i) + ".jpg"
            region.save(path)


def add_image(image1, image2, store_name):
    w1, h1 = image1.size
    w2, h2 = image2.size
    copy_image = image1.copy()
    copy_image.paste(image2, (w1 - w2, h1 - h2))
    copy_image.save(store_name)


def tiled_image(image_to_tile, w_num, h_num, store_name):
    w, h = image_to_tile.size
    width = w * w_num
    height = h * h_num
    new_image = Image.new('RGB', (width, height), 'white')
    for i in range(w_num):
        for j in range(h_num):
            new_image.paste(image_to_tile, (i*w, j*h))
    new_image.save(store_name)


def mosaic(image, w_num, h_num, store_name):
    w, h = image.size
    mosaic_w = w//w_num
    mosaic_h = h//h_num
    actual_w_num = w//mosaic_w+1
    actual_h_num = h//mosaic_h+1
    image_copy = image.copy()
    px = image_copy.load()
    mosaic_color = []
    for i in range(actual_w_num):
        col = []
        for j in range(actual_h_num):
            if i == actual_w_num-1 or j == actual_h_num-1:
                r, g, b = px[i * mosaic_w, j * mosaic_h]
            else:
                # take the color of center pixel in one mosaic tile
                r, g, b = px[i*mosaic_w + mosaic_w//2, j*mosaic_h+mosaic_h//2]
            col.append((r, g, b))
        mosaic_color.append(col)
    for i in range(w):
        for j in range(h):
            if i % mosaic_w == 0 or j % mosaic_h == 0:
                px[i, j] = (255, 255, 255)
            else:
                px[i, j] = mosaic_color[i//mosaic_w][j//mosaic_h]
    image_copy.save(store_name)



image = Image.open("images\\image1_crop.jpg")
image2 = Image.open("images\\python.jpg")

mosaic(image, 80, 80, "images\\image_mosaic.jpg")

# tiled_image(image2, 3, 5, "images\\3x5python.jpg")
#
# add_image(image, image2, "images\\add_image.jpg")

# cut_square_image(image, 5, "images\\image_")


def draw():
    pic.draw()


pgzrun.go()
