#!/usr/bin/env python
"""
Colors

This module handles the TTY terminal colorization using ANSI ESC codes.

add_colorcode(color_name, color_code)     - adds a new color code to the set of colors.
get_color(color_name, terminal_type)      - gets the color string based on terminal type.
colorize(color_name, text, terminal_type) - apply color codes to a text string based on
                                            terminal type.
"""

colors = {"none":  "\033[0m",
          "cyan":  "\033[1;36m",
          "green": "\033[0;32m",
          "red":   "\033[0;31m",
          "yellow": "\033[0;33m",
          "brightgreen": "\033[1;32m",
          "brightyellow": "\033[1;33m",
          }



def add_colorcode(color_name, color_code):
    """
    Add a new color code to the set of allowable color codes.

    @param color_name: The name of the color (i.e., "Green", "Blue", etc.)
    @param color_code: The ESC code for the color (i.e., "\033[0m", "\033[1;36m", etc.)
    """
    global colors

    if not isinstance(color_name, str):
        raise TypeError, "color_name parameter must be a string."

    if not isinstance(color_code, str):
        raise TypeError, "color_code parameter must be a string."

    # TODO: Add some regex checking to make sure color code appears valid.
    colors[color_name] = color_code



def get_color(color_name, terminal_type=None):
    """
    Retrieve the color code from the list if we need to apply colors.

    @param color_name:    The name of the color (i.e., "Green", "Blue", etc.)
    @param terminal_Type: Do we return a color code or empty string?  If
                          this is "tty" then we return the color code.  If
                          it's None (or just -not- "tty"), then we return
                          an empty string.
    """
    output = ""
    if terminal_type is not None and terminal_type.lower() in ["tty"]:
        try:
            output = colors[str(color_name).lower()]
        except:
            # if something went wrong, just return an empty string.
            output = ""
    return output



def colorize(color_name, text, terminal_type=None):
    """
    Colorize a string of text.

    @param color_name: The name of the color (i.e., "Green", "Blue", etc.)
    @param text: The text to colorize.
    @param apply_color: Do we return a color code or empty string?  If
                        this is "tty" then we return the color code.  If
                        it's None (or just -not- "tty"), then we return
                        an empty string.
    """
    return "%s%s%s"%( get_color(color_name, terminal_type), text, get_color("none", terminal_type) )


