import krita
from .spritesheetgeneratoraction import create_action, install_action_file
from .uispritesheetgenerator import UISpritesheetGenerator

class SpritesheetGeneratorExtension(krita.Extension):

    def setup(self):
        install_action_file()

    def createActions(self, window):
        create_action(window, self.showUI)

    def showUI(self):
        self.userInterface = UISpritesheetGenerator()
        self.userInterface.show()
