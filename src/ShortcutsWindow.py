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
    def __init__(self, transient_for=None):
        builder = Gtk.Builder()
        builder.add_from_resource('/it/mijorus/smile/ui/shortcuts.ui')
        self.shortcut_window = builder.get_object('shortcuts')
        # Store parent for proper presentation
        self._parent = transient_for

        settings = Gio.Settings.new('it.mijorus.smile')

        add_em_to_selection_label = _('Add an emoji to selection')
        copy_quit_label = _('Copy the selected emoji and hide the window')

        mouse_multi_select = settings.get_boolean('mouse-multi-select')
        left_click_item = builder.get_object('left-click-item')
        shift_left_click_item = builder.get_object('shift-left-click-item')
        # AdwShortcutsItem supports setting subtitle; use it to show the action description.
        if left_click_item is not None and hasattr(left_click_item, 'set_subtitle'):
            left_click_item.set_subtitle(add_em_to_selection_label if mouse_multi_select else copy_quit_label)
        if shift_left_click_item is not None and hasattr(shift_left_click_item, 'set_subtitle'):
            shift_left_click_item.set_subtitle(copy_quit_label if mouse_multi_select else add_em_to_selection_label)

    def open(self):
        # Prefer presenting with parent when available for correct sizing/placement
        try:
            if self._parent is not None:
                self.shortcut_window.present(self._parent)
            else:
                self.shortcut_window.present()
        except TypeError:
            # Older bindings may not require/accept the parent argument
            self.shortcut_window.present()
