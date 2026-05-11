#!/usr/bin/env python3
"""SerialUI – serial-port entry point."""
import sys
import os
import logging

from .config import DEBUG_LEVEL

try:
    from PyQt5 import QtWidgets
    from PyQt5.QtGui import QIcon
except ImportError:
    from PyQt6 import QtWidgets
    from PyQt6.QtGui import QIcon

from .window import mainWindow


def main():
    root_logger = logging.getLogger("SerialUI")
    root_logger.setLevel(DEBUG_LEVEL)
    sh = logging.StreamHandler()
    fmt = "[%(levelname)-8s] [%(name)-10s] %(message)s"
    sh.setFormatter(logging.Formatter(fmt))
    root_logger.addHandler(sh)
    root_logger.propagate = False

    app = QtWidgets.QApplication(sys.argv)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    app.setWindowIcon(QIcon(os.path.join(base_dir, "assets", "icon_48.png")))

    win = mainWindow(logger=root_logger)

    screen = app.primaryScreen()
    scalingX = screen.logicalDotsPerInchX() / 96.0
    scalingY = screen.logicalDotsPerInchY() / 96.0
    win.resize(int(1280 * scalingX), int(800 * scalingY))

    win.show()
    try:
        exit_code = app.exec()
    except AttributeError:
        exit_code = app.exec_()

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
