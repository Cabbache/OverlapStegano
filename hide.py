from PIL import Image
import random
import sys

if len(sys.argv) != 2:
	print(f'Usage: {sys.argv[0]} [input image]')
	sys.exit(1)

parts = [
	0b0011, 0b1100,
	0b1001, 0b0110,
	0b1010, 0b0101,
]

sb = '\uFF38'
sw = '\uFF40'

def get_pair(dark):
	choice = random.choice(parts)
	if dark:
		return choice, ~choice & 0xFF
	else:
		return choice, choice

def print_squares(squares):
	for row in squares:
		l1 = ''
		l2 = ''
		for block in row:
			l1 += sb if block & 0b1000 else sw
			l1 += sb if block & 0b0100 else sw
			l2 += sb if block & 0b0010 else sw
			l2 += sb if block & 0b0001 else sw
		print(l1)
		print(l2)

def is_dark(pix):
	return sum(pix) / 3 >= 128

mat1 = [[]]
mat2 = [[]]

with Image.open(sys.argv[1]) as img:
	pix = img.load()
	for y in range(img.height):
		for x in range(img.width):
			b1, b2 = get_pair(is_dark(pix[x,y]))
			mat1[-1].append(b1)
			mat2[-1].append(b2)
		mat1.append([])
		mat2.append([])

print_squares(mat1)
print_squares(mat2)
