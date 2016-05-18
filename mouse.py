#Pyjsdl - Copyright (C) 2013 James Garnon <http://gatc.ca/>
#Released under the MIT License <http://opensource.org/licenses/MIT>

#from __future__ import division
import env
import pyjsdl.event
from pyjsobj import DOM

__docformat__ = 'restructuredtext'


class Mouse(object):
    """
    **pyjsdl.mouse**
    
    * pyjsdl.mouse.get_pressed
    * pyjsdl.mouse.get_pos
    * pyjsdl.mouse.get_rel
    * pyjsdl.mouse.set_visible
    * pyjsdl.mouse.set_cursor
    * pyjsdl.mouse.get_cursor
    """

    def __init__(self):
        """
        Provides methods to access the mouse function.
        
        Module initialization creates pyjsdl.mouse instance.
        """
        self.mousePress = pyjsdl.event.mousePress
        self.mouseMove = pyjsdl.event.mouseMove
        self.mouseMoveRel = pyjsdl.event.mouseMoveRel
        self._cursorVisible = True
        self._cursorType = 'default'
        self._nonimplemented_methods()

    def get_pressed(self):
        """
        Return state of mouse buttons as a tuple of bool for button1,2,3.
        """
        return (self.mousePress[0], self.mousePress[1], self.mousePress[2])

    def get_pos(self):
        """
        Return x,y of mouse pointer.
        If the pointer is not in canvas, returns -1,-1
        """
        if self.mouseMove['x'] != -1:
            return (self.mouseMove['x']+env.frame.scrollLeft, self.mouseMove['y']+env.frame.scrollTop)
        else:
            return (self.mouseMove['x'],  self.mouseMove['y'])

    def get_rel(self):
        """
        Return relative x,y change of mouse position since last call.
        """
        try:
            rel = (self.mouseMove['x']-self.mouseMoveRel['x'], self.mouseMove['y']-self.mouseMoveRel['y'])
            self.mouseMoveRel['x'], self.mouseMoveRel['y'] = self.mouseMove['x'], self.mouseMove['y']
        except TypeError:
            rel = (0, 0)
            if self.mouseMove['x'] != -1:
                self.mouseMoveRel['x'], self.mouseMoveRel['y'] = self.mouseMove['x'], self.mouseMove['y']
        return rel

    def set_visible(self, visible):
        """
        Set visibility of mouse cursor. Return bool of previous state.
        """
        visible_pre = self._cursorVisible
        if visible:
            DOM.setStyleAttribute(env.canvas.getElement(), 'cursor', self._cursorType)
            self._cursorVisible = True
        else:
            DOM.setStyleAttribute(env.canvas.getElement(), 'cursor', 'none')
            self._cursorVisible = False
        return visible_pre

    def set_cursor(self, *cursor):
        """
        Set mouse cursor. Refer to cursors.py for details.
        """
        if len(cursor) == 1:
            self._cursorType = cursor[0]
            if self._cursorVisible:
                DOM.setStyleAttribute(env.canvas.getElement(), 'cursor', self._cursorType)

    def get_cursor(self):
        """
        Get mouse cursor.
        """
        return self._cursorType

    def _nonimplemented_methods(self):
        """
        Non-implemented methods.
        """
        self.set_pos = lambda *arg: None
        self.get_focused = lambda *arg: True

