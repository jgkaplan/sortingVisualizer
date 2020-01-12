from PIL import Image, ImageDraw

bar_size = 5
bar_gap = 2

padding = 5

size_x = 100
size_y = 100

color_start = 0
color_stop = 70

highlight_color = 200

end_delay = 3000

ims = []

def setup(size):
	global size_x,size_y
	size_x = 2 * padding + bar_size * size + bar_gap * (size-1)
	size_y = 2 * padding + bar_size * size

def reset():
	global ims
	ims = []

def add_step(arr, highlight):
	im = Image.new('RGB', (size_x,size_y), (0,0,0))
	draw = ImageDraw.Draw(im)
	x = padding
	for i, el in enumerate(arr):
		color = highlight_color if i in highlight else (color_start+color_stop)/len(arr)*el
		draw.rectangle([(x,size_y - padding),(x+bar_size,size_y - (padding+el*bar_size))], fill="hsv({},100%,100%)".format(color))
		x += bar_gap + bar_size
	ims.append(im)

def render(filename, delay):
	delays = [delay] * len(ims)
	delays[0] = end_delay
	ims[0].save('{}.gif'.format(filename), format='GIF', append_images=ims[1:], save_all=True, duration=delays, optimize=True)
