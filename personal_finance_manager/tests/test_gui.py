# tests/test_gui.py

import unittest
from ..app.gui.main_window import MainWindow
from PyQt5.QtWidgets import QApplication
import sys

class TestGUI(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.window = MainWindow()

    def test_window_title(self):
        self.assertEqual(self.window.windowTitle(), "Personal Finance Manager")

    def test_window_size(self):
        self.assertEqual(self.window.width(), 1000)
        self.assertEqual(self.window.height(), 800)