"""Provides a collection of widgets, each one representing an element in the
stream. A widget is simply a graphical element that is drawn on each frame of 
the draw routine. The widget creation functions should be called from the main
stream routine.
"""
#import config
import Queue


class Widget(object):
    """Creates a widget object that represents an element drawn to the stream.
    Provides helper functions common to all Widget objects.

    :param screen: the screen object that the widget is being drawn to
    :param position: (x, y) coordinates for the top-left corner of the widget
    """
    def __init__(self, screen, position):
        self.screen = screen
        self.position = position

    def draw(self):
        """Abstract method to be implemented by every Widget."""
        return

    def draw_label(self, position, text, font, color):
        text_label = font.render(text, 1, color)
        self.screen.blit(text_label, position)



class DonationWidget(Widget):
    
    def __init__(self, screen, position, font, width):
        Widget.__init__(self, screen, position)
        self.font = font
        self.width = width

        self.counter = 0
        self.queue = []

    def draw(self):
        if self.counter == 0:

        self.draw_label(self)
        
    def add_donation(self, name, comment):
        self.queue.append((name, comment))



class CommandQueueWidget(Widget):
    def __init__(self, screen, position, limit=):
        Widget.__init__(self, screen, position)
        self.queue = []

    def draw(self):

        return



class StatisticsWidget(Widget):
    def __init__(self, screen, position):
        Widget.__init__(self, screen, position)

    def draw(self):
        return


