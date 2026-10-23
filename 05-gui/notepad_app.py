"""
Notepad Application — Learning GUI Development with PyQt5
Author: Gökhan Arda Borulu
Topic: PyQt5, Widgets, Layouts, File Dialogs, Menu Bars, Keyboard Shortcuts

A functional text editor application built with PyQt5:
- Open and save text files
- Clear the text area
- Menu bar with keyboard shortcuts (Ctrl+O, Ctrl+S, Ctrl+D, Ctrl+Q)

Demonstrates PyQt5 widget composition, layouts, signals/slots, and menus.
"""

import os
import sys

from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QFileDialog,
    QHBoxLayout,
    QMainWindow,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
    qApp,
)


class Notepad(QWidget):
    """Main notepad widget with text area and action buttons."""

    def __init__(self):
        super().__init__()
        self._init_ui()

    def _init_ui(self) -> None:
        """Initialize the notepad UI components."""
        self.text_area = QTextEdit()

        # Action buttons
        self.btn_clear = QPushButton("Temizle")
        self.btn_open = QPushButton("Aç")
        self.btn_save = QPushButton("Kaydet")

        # Button layout
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.btn_clear)
        button_layout.addWidget(self.btn_open)
        button_layout.addWidget(self.btn_save)

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.text_area)
        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)

        # Connect signals
        self.btn_clear.clicked.connect(self.clear_text)
        self.btn_open.clicked.connect(self.open_file)
        self.btn_save.clicked.connect(self.save_file)

        self.setWindowTitle("NotePad — Arda")

    def clear_text(self) -> None:
        """Clear the text area."""
        self.text_area.clear()

    def open_file(self) -> None:
        """Open a file dialog and load the selected file."""
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Dosya Aç", os.getenv("HOME", ".")
        )
        if file_path:
            with open(file_path, "r", encoding="utf-8") as f:
                self.text_area.setText(f.read())

    def save_file(self) -> None:
        """Open a save dialog and write the text to the selected file."""
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Dosya Kaydet", os.getenv("HOME", ".")
        )
        if file_path:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(self.text_area.toPlainText())


class MenuBar(QMainWindow):
    """Main window with menu bar wrapping the Notepad widget."""

    def __init__(self):
        super().__init__()
        self.notepad = Notepad()
        self.setCentralWidget(self.notepad)
        self._create_menus()

    def _create_menus(self) -> None:
        """Create the File menu with actions and shortcuts."""
        menubar = self.menuBar()
        file_menu = menubar.addMenu("Dosya")

        # File → Open
        open_action = QAction("Dosya Aç", self)
        open_action.setShortcut("Ctrl+O")

        # File → Save
        save_action = QAction("Dosya Kaydet", self)
        save_action.setShortcut("Ctrl+S")

        # File → Clear
        clear_action = QAction("Dosyayı Temizle", self)
        clear_action.setShortcut("Ctrl+D")

        # File → Exit
        exit_action = QAction("Çıkış", self)
        exit_action.setShortcut("Ctrl+Q")

        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addAction(clear_action)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)

        file_menu.triggered.connect(self._handle_menu_action)

        self.setWindowTitle("Metin Editörü — Arda")
        self.resize(800, 600)
        self.show()

    def _handle_menu_action(self, action: QAction) -> None:
        """Handle menu action clicks."""
        action_text = action.text()

        if action_text == "Dosya Aç":
            self.notepad.open_file()
        elif action_text == "Dosya Kaydet":
            self.notepad.save_file()
        elif action_text == "Dosyayı Temizle":
            self.notepad.clear_text()
        elif action_text == "Çıkış":
            qApp.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = MenuBar()
    sys.exit(app.exec_())
