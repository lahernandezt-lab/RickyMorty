import pygame
from .ImageContainer import ImageContainer

class StackBar(ImageContainer):
    def __init__(self, background_image, center_coordinates_pair):
        super().__init__(background_image, center_coordinates_pair)

        self.background = pygame.image.load(background_image)
        self.asset_list = []
        self.asset_coords = []


    def load_assets(self, gem_status_dict):
        for gem_object in gem_status_dict:
            if gem_status_dict[gem_object]["obtained"]:
                self.asset_list.append(pygame.image.load(gem_status_dict[gem_object]["image_path"]))
                self.asset_coords.append(gem_status_dict[gem_object]["coords"])

    def graph_stackbar(self, screen):
        super().image_only_render(screen)

        for stack_iterator in range(len(self.asset_list)):
            screen.blit(self.asset_list[stack_iterator], self.asset_coords[stack_iterator])


    def materials_add(self, rick, new_materials):
        rick[new_materials]["obtained"] = True
