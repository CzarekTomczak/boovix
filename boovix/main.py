# Copyright (c) 2014, The Boovix authors that are listed
# in the AUTHORS file. All rights reserved. Use of this
# source code is governed by the BSD 3-clause license that
# can be found in the LICENSE file.

"""Main module"""

import wx

# Pylint tests:
# import asd.xyz
# asd.xyz.Frame(None, -1, "Hello World")
# asd.xyz.Frame2(None, -1, "Hello World")


def main():
    """Main function"""
    app = wx.App()
    frame = wx.Frame(None, -1, "Hello World")
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
