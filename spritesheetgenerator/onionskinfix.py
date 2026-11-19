import time

import krita
from PyQt5.QtWidgets import QApplication

ACTION_ID = "toggle_onion_skin"
SETTING_KEY = "onionSkinState_0"
WAIT_TIMEOUT = 1.0

def _master_enabled():
    value = krita.Krita.instance().readSetting("", SETTING_KEY, "true")
    return str(value).strip().lower() == "true"


def _wait_for(enabled, timeout=WAIT_TIMEOUT):
    deadline = time.time() + timeout
    while time.time() < deadline:
        QApplication.processEvents()
        if _master_enabled() == enabled:
            return True
        time.sleep(0.01)
    return _master_enabled() == enabled


class OnionSkinsDisabled():

    def __init__(self):
        self.action = None
        self.toggled = False

    def __enter__(self):
        self.action = krita.Krita.instance().action(ACTION_ID)
        if self.action is None or not _master_enabled():
            return self
        self.action.trigger()
        self.toggled = _wait_for(False)
        return self

    def __exit__(self, exc_type, exc, traceback):
        if self.toggled:
            self.action.trigger()
            _wait_for(True)
        return False
