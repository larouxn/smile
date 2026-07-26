import sys
import gi
import time
import os
import csv
import re
from .assets.emoji_list import emojis

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Gtk, Gio, Gdk, Adw  # noqa

class ShortcutsWindow():
    def __init__(self):
        Adw.init()
        builder = Gtk.Builder()
        builder.add_from_resource('/it/mijorus/smile/ui/shortcuts.ui')
        self.shortcut_window = builder.get_object('shortcuts')

        settings = Gio.Settings.new('it.mijorus.smile')

        add_em_to_selection_label = _('Add an emoji to selection')
        copy_quit_label = _('Copy the selected emoji and hide the window')

        mouse_multi_select = settings.get_boolean('mouse-multi-select')
        builder.get_object('shift-left-click-item').set_title(copy_quit_label if mouse_multi_select else add_em_to_selection_label)
        builder.get_object('left-click-item').set_title(add_em_to_selection_label if mouse_multi_select else copy_quit_label)

    def open(self, parent=None):
        self.shortcut_window.present(parent)

