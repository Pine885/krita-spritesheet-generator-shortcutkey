import krita
# Action id, tooltip and .action file install live in their own module.
from .spritesheetgeneratoraction import create_action, install_action_file
from .uispritesheetgenerator import UISpritesheetGenerator

# No __init__ on purpose: no instance state and the inherited
# krita.Extension.__init__(parent) runs unchanged.
class SpritesheetGeneratorExtension(krita.Extension):

    def setup(self):
        # Copy spritesheet_generator.action into Krita's actions folder so the
        # action is listed (and remappable) under Keyboard Shortcuts.
        install_action_file()

    def createActions(self, window):
        # Stable id "spritesheet_generator" keeps assigned shortcuts working.
        create_action(window, self.showUI)

    def showUI(self):
        self.userInterface = UISpritesheetGenerator()
        self.userInterface.show()
