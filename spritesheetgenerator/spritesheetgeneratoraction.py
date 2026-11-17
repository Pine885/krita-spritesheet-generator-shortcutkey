import filecmp
import os
import shutil

from PyQt5.QtCore import QStandardPaths

ACTION_ID = "spritesheet_generator"
ACTION_TEXT = "Spritesheet Generator"
ACTION_FILE = "spritesheet_generator.action"
TOOLTIP = "Export frames in the animation timeline as a spritesheet."


def create_action(window, slot):
    """Register the menu action and connect it to ``slot``."""
    action = window.createAction(ACTION_ID, ACTION_TEXT)
    action.setToolTip(TOOLTIP)
    action.triggered.connect(slot)
    return action


def install_action_file():
    """Copy the .action file into Krita's resource folder.

    Krita lists a plugin action in Keyboard Shortcuts only when the matching
    .action file exists; it also holds the (empty) default shortcut.
    """
    try:
        actions_dir = os.path.join(
            QStandardPaths.writableLocation(QStandardPaths.AppDataLocation),
            "actions")
        os.makedirs(actions_dir, exist_ok=True)
        src = os.path.join(os.path.dirname(__file__), ACTION_FILE)
        dst = os.path.join(actions_dir, ACTION_FILE)
        if os.path.exists(src) and not (
                os.path.exists(dst) and filecmp.cmp(src, dst, shallow=False)):
            shutil.copyfile(src, dst)
    except Exception as e:
        print("Spritesheet Generator: could not install .action file: %s" % e)
