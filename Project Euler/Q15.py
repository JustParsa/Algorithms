dim = input ("Please enter the dimensions of an X by X lattice:")

class grid:

	def __init__ (self, x = 0, y = 0):
		grid.x = x
		grid.y = y

grd = grid(dim,dim)

def recurse (x = 0,y = 0, num_paths =0):
	if x != grd.x:
		num_paths += 1
		recurse (x + 1, y, num_paths)
	if y != grd.y:
		num_paths += 1
		recurse (x, y + 1, num_paths)

print (num_paths)