import sys
import pygame
import block_grid
import block_grid_drawer
import block_grid_editor
import block_grid_editor_drawer
import block_grid_space_manager
import block_grid_selector
import block_grid_hoverer
import block_grid_hoverer_drawer

BG_COL = (220, 220, 220)
SIZE = 5
START_X = 350
START_Y = 200
BLOCK_WIDTH = 128
BLOCK_HEIGHT = 48
HEIGHT_MODIFIER = 10

def main():
	pygame.init()
	pygame.display.set_caption('bg_s' + str(SIZE) + '_sx' + str(START_X) + '_sy' + str(START_Y) + '_bw' + str(BLOCK_WIDTH) + '_bh' + str(BLOCK_HEIGHT) + '_hm' + str(HEIGHT_MODIFIER))
	size = width, height = 700, 700
	d_surf = pygame.display.set_mode(size)
	clock = pygame.time.Clock()

	bgss = block_grid_space_manager.BlockGridSpaceSpecification(START_X, START_Y, BLOCK_WIDTH, BLOCK_HEIGHT, HEIGHT_MODIFIER)
	selector = block_grid_selector.BlockGridSelector(bgss)

	grid = block_grid.BlockGrid(size=SIZE)
	grid_drawer = block_grid_drawer.BlockGridDrawer(bgss)
	grid_editor = block_grid_editor.BlockGridEditor(bgss, selector)
	grid_editor_drawer = block_grid_editor_drawer.BlockGridEditorDrawer(bgss)
	grid_hoverer = block_grid_hoverer.BlockGridHoverer(selector)
	grid_hoverer_drawer = block_grid_hoverer_drawer.BlockGridHovererDrawer(bgss)

	while True:
		delta_ms = clock.tick(30)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			else:
				grid = grid_editor.handle_event(grid, event)

		grid_hoverer.update(grid, pygame.mouse.get_pos())

		clock.tick(30)
		d_surf.fill(BG_COL)
		grid_drawer.draw_fill(grid, d_surf)
		grid_hoverer_drawer.draw(grid, grid_hoverer, d_surf)
		grid_editor_drawer.draw(grid, grid_editor, d_surf)
		pygame.display.update()
	

if __name__ == '__main__':
	main()
