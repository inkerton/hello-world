# Copyright 2009 Simon Schampijer
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

"""HelloWorld Activity: A case study for developing an activity. Ported version from GTK3 to GTK4."""

import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

from gettext import gettext as _

from sugar3.activity import activity


class HelloWorldActivity(activity.Activity):
    """HelloWorldActivity class as specified in activity.info"""

    def __init__(self, handle):
        """Set up the HelloWorld activity using GTK4 widgets."""
        activity.Activity.__init__(self, handle)

        self.max_participants = 1

        # Main window and box for layout
        self.window = Gtk.Window(title="Hello World")
        self.box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)

        activity_button = Gtk.Button(label=_("Activity"))
        self.box.pack_start(activity_button, False, False, 0)

        separator = Gtk.Separator(orientation=Gtk.Orientation.VERTICAL)
        self.box.pack_start(separator, False, False, 0)
        
        stop_button = Gtk.Button(label=_("Stop"))
        stop_button.connect("clicked", self.on_stop_clicked)  # Connecting to stop function
        self.box.pack_start(stop_button, False, False, 0)

        label = Gtk.Label(_("Hello World!"))
        self.box.pack_start(label, True, True, 0)  # Make label expandable

        # Adding box to window and show all widgets
        self.window.add(self.box)
        self.window.show_all()

    def on_stop_clicked(self, button):
        # Implementing stop functionality (close window)
        self.window.destroy()

        self.set_toolbar_box(toolbar_box)
        toolbar_box.show()

        # making the string translatable
        label = Gtk.Label(_("Hello World!"))
        self.set_canvas(label)
        label.show()
