import filecmp
import os
import shutil

import krita
from PyQt5.QtCore import QStandardPaths
from .uispritesheetgenerator import UISpritesheetGenerator

class SpritesheetGeneratorExtension(krita.Extension):

    ACTION_FILE = "spritesheet_generator.action"

    def setup(self):
        self.install_action_file()

    def createActions(self, window):
        action = window.createAction("spritesheet_generator", "Spritesheet Generator")
        action.setToolTip("Export frames in the animation timeline as a spritesheet.")
        action.triggered.connect(self.showUI)

    def install_action_file(self):
        # Krita lists an action in Keyboard Shortcuts only if its .action file exists.
        try:
            actions_dir = os.path.join(
                QStandardPaths.writableLocation(QStandardPaths.AppDataLocation),
                "actions")
            os.makedirs(actions_dir, exist_ok=True)
            src = os.path.join(os.path.dirname(__file__), self.ACTION_FILE)
            dst = os.path.join(actions_dir, self.ACTION_FILE)
            if os.path.exists(src) and not (
                    os.path.exists(dst) and filecmp.cmp(src, dst, shallow=False)):
                shutil.copyfile(src, dst)
        except Exception as e:
            print("Spritesheet Generator: could not install .action file: %s" % e)

    def showUI(self):
        self.userInterface = UISpritesheetGenerator()
        self.userInterface.show()
