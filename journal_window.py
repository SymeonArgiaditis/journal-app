from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QTextEdit, QListWidget, QListWidgetItem
from pathlib import Path

from journal_data import list_journals, list_entries

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
        self.sidebar = QListWidget()
        self.content = QTextEdit()

        # Create basic layout
        layout = QHBoxLayout(window_container)
        layout.addWidget(self.sidebar, 1)
        layout.addWidget(self.content, 3)

        # Fill ListWidget with real journals from disk
        self.journals_path = Path(__file__).parent / "Journals"

        for journal_name in list_journals(self.journals_path):
            self.sidebar.addItem(journal_name)

        self.sidebar.itemClicked.connect(self.on_journal_clicked)

    def on_journal_clicked(self, item: QListWidgetItem):
        journal_path = self.journals_path / item.text()
        entries_text = list_entries(journal_path)

        self.content.setPlainText('\n'.join(entries_text))
