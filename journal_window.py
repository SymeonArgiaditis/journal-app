from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QTextEdit, QListWidget
from pathlib import Path

from journal_data import list_journals

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
        content = QTextEdit()

        # Create basic layout
        layout = QHBoxLayout(window_container)
        layout.addWidget(sidebar, 1)
        layout.addWidget(content, 3)

        # Fill ListWidget with real journals from disk
        journals_path = Path(__file__).parent / "Journals"

        for journal_name in list_journals(journals_path):
            sidebar.addItem(journal_name)
