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
SIZE = 9
START_HEIGHT = 10
START_X = 350
START_Y = 200
BLOCK_WIDTH = 64
BLOCK_HEIGHT = 24

def main():
	pygame.init()
	pygame.display.set_caption('bg_s' + str(SIZE) + '_sh' + str(START_HEIGHT) + '_sx' + str(START_X) + '_sy' + str(START_Y) + '_bw' + str(BLOCK_WIDTH) + '_bh' + str(BLOCK_HEIGHT))
	size = width, height = 700, 700
	d_surf = pygame.display.set_mode(size)
	clock = pygame.time.Clock()

	bgss = block_grid_space_manager.BlockGridSpaceSpecification(START_X, START_Y, BLOCK_WIDTH, BLOCK_HEIGHT)
	selector = block_grid_selector.BlockGridSelector(bgss)

	grid = block_grid.BlockGrid(size=SIZE, start_height=10)
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
			elif event.type == pygame.MOUSEBUTTONUP:
				grid_editor.handle_mouse_button_up(grid, event)
			elif event.type == pygame.KEYDOWN:
				grid = grid_editor.handle_key_down(grid, event)

		grid_hoverer.update(grid, pygame.mouse.get_pos())

		clock.tick(30)
		d_surf.fill(BG_COL)
		grid_drawer.draw_fill(grid, d_surf)
		grid_hoverer_drawer.draw(grid, grid_hoverer, d_surf)
		grid_editor_drawer.draw(grid, grid_editor, d_surf)
		pygame.display.update()
	

if __name__ == '__main__':
	main()
