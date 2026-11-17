import krita
from .spritesheetgeneratoractiongen import SpritesheetGeneratorExtension

Scripter.addExtension(SpritesheetGeneratorExtension(krita.Krita.instance()))
