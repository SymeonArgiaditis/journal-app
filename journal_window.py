from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout

# Temporary import of QPushButton and QListWidget
from PySide6.QtWidgets import QPushButton, QListWidget

class JournalWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window title and size
        self.setWindowTitle("Journal")
        self.resize(900, 600)

        # Set central window container QWidget containing layout
        window_container = QWidget()
        self.setCentralWidget(window_container)

        # Create widgets
        sidebar = QListWidget()
        content = QPushButton("content")

        # Create basic layout
        layout = QHBoxLayout(window_container)
        layout.addWidget(sidebar, 1)
        layout.addWidget(content, 3)

        # Fill ListWidget with temporary entries
        sidebar.addItem("2025 Journal")
        sidebar.addItem("Travel Journal")
