import ast
import json
from block_grid.src import block_grid
from block_grid.src import block


class BlockGridSaveLoader:
	def __init__(self, dest_folder):
		self.dest_folder = dest_folder 

	def save(self, bg, filename):
		with open(f"{self.dest_folder}/{filename}.bg", "w") as f:
			f.write(json.dumps(bg, cls=BlockGridEncoder))

	def load(self, filename):
		with open(f"{self.dest_folder}/{filename}.bg") as f:
			return json.load(f, cls=BlockGridEncoder)


class BlockGridEncoder(json.JSONEncoder):
		def default(self, bg):
			return {str(item[0]) : str(item[1].vertex_heights) for item in bg.blocks.items()}

		def decode(self, block_grid_json):
			str_map = json.loads(block_grid_json)
			blocks_map = {ast.literal_eval(item[0]): block.Block(ast.literal_eval(item[1])) for item in str_map.items()}
			return block_grid.BlockGrid(blocks=blocks_map)