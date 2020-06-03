from block import Block

class BlockGrid:
	def __init__(self, size=1, blocks=None, start_height=0):
		if blocks:
			self.blocks = blocks
		else:
			self.blocks = {}
			for pos in generate_sorted_keys(size):
				self.blocks[pos] = Block(start_height)

	def raise_(self, pos, x):
		return BlockGrid(blocks={k: self.blocks[k].raise_(x if k == pos else 0) for k in self.blocks})

	def lower(self, pos, x):
		return BlockGrid(blocks={k: self.blocks[k].lower(x if k == pos else 0) for k in self.blocks})

	def raise_point(self, pos, i, x):
		return BlockGrid(blocks={k: self.blocks[k].raise_point(i, x if k == pos else 0) for k in self.blocks})

	def lower_point(self, pos, i, x):
		return BlockGrid(blocks={k: self.blocks[k].lower_point(i, x if k == pos else 0) for k in self.blocks})

	def remove(self, pos):
		return BlockGrid(blocks={k: self.blocks[k].copy() for k in self.blocks if k != pos})


def generate_sorted_keys(size):
	ls_k = [(x, y) for x in range(size) for y in range(size)]
	ls_k.sort(key = lambda k: k[0] + k[1])
	return ls_k