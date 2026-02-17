import pygame
import sys

# Import the visual classes
from view.classes.Button import Button
from view.classes.TextContainer import TextContainer
from view.classes.ImageContainer import ImageContainer
from view.classes.StackBar import StackBar

# Import backend related stuff
from modelView.Types import Option, NodeType
from modelView.nodes.NodeCharacter import NodeCharacter


# Return the loaded pygame font for a given size
def get_font(font_size):
    return pygame.font.Font(f"view/assets/fonts/Webcomic.ttf", font_size)

# Keep the text of a container within the image's boundaries
def get_font_size(string, standard_size, max_len):
    size = standard_size
    text_lem = len(string)
    if text_lem>max_len:
        size = int((max_len*standard_size)/len(string))
    return size


class GameInterface:
    def __init__(self, rick_instance = None):
        pygame.init()

        self.rick_instance = rick_instance

        # Screen initialization
        self.display_size = [1280, 720]
        self.screen = pygame.display.set_mode(self.display_size)

        self.choice_buttons = []

        self.stack_bar = StackBar(
            background_image=("view/assets/materials/stack_bar.png"),
            center_coordinates_pair=((self.display_size[0]/10)+80, (self.display_size[1]/2)-1)
        )

        # Executable customizations
        pygame.display.set_caption("Rick y Morty")
        pygame.display.set_icon(pygame.image.load("view/assets/misc/logo.png"))


    # Setter to define the rick instance
    def set_rick(self, rick_class):
        self.rick_instance = rick_class

    # Update the screen's background given an image route
    def set_background(self, image_route: str):
        new_background = pygame.image.load(image_route)
        self.screen.blit(new_background, (0, 0))


    def button_identifier(self, mouse_position):
        clicked_button = None

        # Identify the processed button
        for button_obj in self.choice_buttons:
            if button_obj.check_mouse_hover(mouse_position):
                clicked_button = button_obj.id
                break

        # Return if no button was found
        if not clicked_button:
            return

        # Execute the action related to that button
        if clicked_button == "Deadbook":
            self.display_deadbook()
        elif clicked_button == Option.LEFT or clicked_button == Option.RIGHT:
            self.rick_instance.choose(clicked_button)


    # Deals with all events in each frame
    def core_event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.button_identifier(pygame.mouse.get_pos())


    # The function that loads the starting menu
    def start_gui(self):
        start_game_button = Button(
            background_image="view/assets/buttons/start_button.png",
            center_coordinates_pair=[
                (self.display_size[0]/2),
                (self.display_size[1]/2)+183
            ],
            text_input=None,
            text_color="White",
            font=get_font(0),
            text_hovering_color="White",
            uuid="Start_Button"
        )

        # Cycle to run per frame
        while True:
            self.set_background("view/assets/backgrounds/start_menu_bg.png")

            start_game_button.display_button_update(self.screen)

            # Check for user inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if start_game_button.check_mouse_hover(pygame.mouse.get_pos()):
                        self.load_introduction()

            # Show the changes
            pygame.display.flip()

        # Function that displays the series of introductory cutscenes
    def load_introduction(self):
        cutscenes_iterator = 1

        # Cycle to run per frame
        while True:
            self.set_background(f"view/assets/backgrounds/introduction/intro-0{cutscenes_iterator}.png")

            # Check for user inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if cutscenes_iterator == 10:
                        # When the last intro image is reached, move to whatever is next
                        return self.rick_instance.start()
                    cutscenes_iterator += 1

            # Show the changes
            pygame.display.flip()

    def set_buttons(self, data_node):
        
        options = data_node.getOptions()
        
        if data_node.type == NodeType.STORY or data_node.type == NodeType.DIALOGUE or data_node.type == NodeType.SPECIAL:
            
            if len(options) >= 2:
                # === Caso 1: Dos o más opciones (Botones Izquierda/Derecha) ===
                left_choice_button = Button(
                    background_image="view/assets/buttons/choice_left_button.png",
                    center_coordinates_pair=[292+35+(434/2), 316+258+(85/2)],
                    text_input=options[0],
                    text_color="White",
                    font=get_font(get_font_size(options[0], 50, 22)),
                    text_hovering_color="Gray",
                    uuid=Option.LEFT
                )

                right_choice_button = Button(
                    background_image="view/assets/buttons/choice_right_button.png",
                    center_coordinates_pair=[292+490+(434/2), 316+258+(85/2)],
                    text_input=options[1],
                    text_color="White",
                    font=get_font(get_font_size(options[1], 50, 22)),
                    text_hovering_color="Gray",
                    uuid=Option.RIGHT
                )

                self.choice_buttons = [left_choice_button, right_choice_button]
            
            elif len(options) == 1:
                # === Caso 2: Solo una opción (Botón Central) ===
                # Reutilizamos la lógica del botón central para evitar el IndexError
                choice_central_button = Button(
                    background_image="view/assets/buttons/choice_central_button.png",
                    center_coordinates_pair=[292+(964/2), 316+258+(85/2)],
                    text_input=options[0],
                    text_color="White",
                    font=get_font(get_font_size(options[0], 50, 22)),
                    text_hovering_color="Gray",
                    uuid=Option.LEFT # Usamos LEFT para que siga al primer child
                )
                self.choice_buttons = [choice_central_button]
                
            else:
                # Caso 3: Cero opciones (No debería pasar en STORY/DIALOGUE/SPECIAL, pero por seguridad)
                self.choice_buttons = []

        elif data_node.type == NodeType.FIGHT:
            # La lógica de FIGHT ya estaba bien, ya que asume y tiene una sola opción [0]
            choice_central_button = Button(
                background_image="view/assets/buttons/choice_central_button.png",
                center_coordinates_pair=[292+(964/2), 316+258+(85/2)],
                text_input=options[0],
                text_color="White",
                font=get_font(get_font_size(options[0], 50, 22)),
                text_hovering_color="Gray",
                uuid=Option.LEFT
            )

            self.choice_buttons = [choice_central_button]
        
        elif data_node.type == NodeType.BLANK:
            # La lógica de BLANK ya estaba bien
            next_story_batch_button = Button(
                background_image="view/assets/buttons/blank_next_button.png",
                center_coordinates_pair=[1150, 630],
                text_input=None,
                text_color="White",
                font=get_font(0),
                text_hovering_color="White",
                uuid=Option.LEFT
            )

            self.choice_buttons = [next_story_batch_button]

        # Regardless of the type of node, add the deadbook
        deadbook_button = Button(
            background_image="view/assets/buttons/deadbook.png",
            center_coordinates_pair=[1177,215],
            text_input=None,
            text_color="White",
            font=get_font(0),
            text_hovering_color="White",
            uuid="Deadbook"
        )

        self.choice_buttons.append(deadbook_button)

    def display_deadbook(self):
        from model.Characters import Characters

        char_list = []
        for character_iterator in Characters:
            if Characters[character_iterator].state:
                char_list.append(pygame.image.load(Characters[character_iterator].miniatureRoute))
            else:
                char_list.append(pygame.image.load(Characters[character_iterator].minDeadRoute))


        while True:
            deadbook_bg = ImageContainer(
                background_image="view/assets/backgrounds/deadbook_bg.png",
                center_coordinates_pair=[self.display_size[0]/2, self.display_size[1]/2]
            )

            deadbook_bg.image_only_render(self.screen)

            # Render all characters
            for character_it in range(len(char_list)):
                self.screen.blit(char_list[character_it], Characters[character_it].coords)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if not deadbook_bg.check_mouse_hover(mouse_pos):
                        self.set_background("view/assets/backgrounds/nodes_bg.png")
                        return

            # Show the changes
            pygame.display.flip()


    def display_story_node(self, story_node):
        self.set_background("view/assets/backgrounds/nodes_bg.png")

        story_text_box = TextContainer(
            background_image="view/assets/backgrounds/text_container_bg.png",
            center_coordinates_pair=[292+(964/2), 316+(373/2)],
            text_input=story_node.getContent(),
            text_color="Black",
            font=get_font(25)
        )

        self.set_buttons(story_node)

        # stack bar stuff :D
        self.stack_bar.load_assets(self.rick_instance.blessings)
        if story_node.type is NodeType.SPECIAL:
            self.stack_bar.materials_add(self.rick_instance.blessings, story_node.stack)

        while True:
            story_text_box.multiline_text_render(self.screen, 0)

            for button in self.choice_buttons:
                button.display_button_update(self.screen)

            self.stack_bar.graph_stackbar(self.screen)
            self.core_event_handler()

            # Show the changes
            pygame.display.flip()

    def display_character_node(self, char_node):
        self.set_background("view/assets/backgrounds/nodes_bg.png")

        story_text_box = TextContainer(
            background_image="view/assets/backgrounds/text_container_bg.png",
            center_coordinates_pair=[292+(964/2), 316+(373/2)],
            text_input=char_node.getContent(),
            text_color="Black",
            font=get_font(25)
        )

        character_icon = ImageContainer(
            background_image=char_node.getCharacterPictureRoute(),
            center_coordinates_pair=[story_text_box.rect.topleft[0]+61, story_text_box.rect.top-31]
        )

        character_label = TextContainer(
            background_image="view/assets/characters/character_label.png",
            center_coordinates_pair=[story_text_box.rect.topleft[0]+(164*3/2), story_text_box.rect.top-11],
            text_input=char_node.getCharacterName(),
            text_color="White",
            font=get_font(42)
        )

        self.set_buttons(char_node)

        # stack bar stuff :D
        self.stack_bar.load_assets(self.rick_instance.blessings)
        if char_node.type is NodeType.SPECIAL:
            self.stack_bar.materials_add(self.rick_instance.blessings, char_node.stack)

        while True:
            story_text_box.multiline_text_render(self.screen, 31)
            character_label.character_label_render(self.screen)
            character_icon.image_only_render(self.screen)

            for button in self.choice_buttons:
                button.display_button_update(self.screen)

            self.stack_bar.graph_stackbar(self.screen)
            self.core_event_handler()

            # Show the changes
            pygame.display.flip()

    def display_final_node(self, final_node):

        final_box = ImageContainer(
            background_image="view/assets/backgrounds/final_bg.png",
            center_coordinates_pair=[292+(964/2), 316+(373/2)],
        )

        while True:
            final_box.image_only_render(self.screen)

            self.core_event_handler()

            # Show the changes
            pygame.display.flip()
