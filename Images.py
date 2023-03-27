import pygame
import os

tile_size = (29, 29)

VOID_TILE = pygame.image.load(os.path.join("Assets", "Images", "Void tile.png"))
VOID_TILE = pygame.transform.scale(VOID_TILE, tile_size)
NORMAL_TILE = pygame.image.load(os.path.join("Assets", "Images", "Normal tile.png"))
NORMAL_TILE = pygame.transform.scale(NORMAL_TILE, tile_size)
BRIDGE_TILE_SOFT = pygame.image.load(os.path.join("Assets", "Images", "Bridge tile (soft).png"))
BRIDGE_TILE_SOFT = pygame.transform.scale(BRIDGE_TILE_SOFT, tile_size)
FINISH_TILE = pygame.image.load(os.path.join("Assets", "Images", "Finish tile.png"))
FINISH_TILE = pygame.transform.scale(FINISH_TILE, tile_size)
BLOCK = pygame.image.load(os.path.join("Assets", "Images", "Block.png"))
BLOCK = pygame.transform.scale(BLOCK, tile_size)
BRIDGE_TILE_HARD = pygame.image.load(os.path.join("Assets", "Images", "Bridge tile (hard).png"))
BRIDGE_TILE_HARD = pygame.transform.scale(BRIDGE_TILE_HARD, tile_size)
BRIDGE = pygame.image.load(os.path.join("Assets", "Images", "Bridge.png"))
BRIDGE = pygame.transform.scale(BRIDGE, tile_size)
SOFT_TILE = pygame.image.load(os.path.join("Assets", "Images", "Soft tile.png"))
SOFT_TILE = pygame.transform.scale(SOFT_TILE, tile_size)