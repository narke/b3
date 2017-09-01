# -*- coding: utf-8 -*-
"""
GTK GUI.
"""
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.0')
from gi.repository import Gtk, WebKit2
import pkg_resources


webkit_renderer = None
urlentry = None

class Handler:
    """Events handler."""
    def back_button_clicked(self, button):
        """On 'back' button click load the previous page."""
        global webkit_renderer
        webkit_renderer.go_back()

    def forward_button_clicked(self, button):
        """On 'forward' button click load the next page."""
        global webkit_renderer
        webkit_renderer.go_forward()

    def refresh_button_clicked(self, button):
        """On 'refresh' button click refresh the page."""
        global webkit_renderer
        webkit_renderer.reload()

    def enter_key_hit(self, button):
        """On 'Enter' key hit load the typed url."""
        global webkit_renderer
        webkit_renderer.load_uri(urlentry.get_text())


def main():
    global webkit_renderer
    global urlentry
    builder = Gtk.Builder()
    glade_file = pkg_resources.resource_filename(__name__, 'ui.glade')
    builder.add_from_file(glade_file)
    builder.connect_signals(Handler())
    window = builder.get_object("main_window")

    webkit_renderer = WebKit2.WebView()

    # Settings
    settings = WebKit2.Settings()
    user_agent = settings.get_property('user-agent')
    try:
        webkit_version = user_agent.split()[4]
    except IndexError:
        webkit_version = ''
    settings.set_property('user-agent', 'b3/0.0 ' + webkit_version)
    webkit_renderer.set_settings(settings)

    # The default URL to be loaded
    webkit_renderer.load_uri("https://duckduckgo.com")
    urlentry = builder.get_object("address_bar")
    urlentry.set_text("https://duckduckgo.com")

    scrolled_window = builder.get_object("scrolledwindow")
    scrolled_window.add(webkit_renderer)
    webkit_renderer.show()

    window.connect("delete-event", Gtk.main_quit)
    window.show_all()
    Gtk.main()


if __name__ == '__main__':
    main()
