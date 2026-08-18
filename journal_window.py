from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QTextEdit, QListWidget, QListWidgetItem
from pathlib import Path

from journal_data import list_journals, list_entries

# Temporary import of QVBoxLayout and QPushButton!
from PySide6.QtWidgets import QVBoxLayout, QPushButton

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
        self.entry_list = QListWidget()
        self.content = QTextEdit()
        self.mode_button = QPushButton("Edit")

        # Vertical content layout
        content_layout = QVBoxLayout()
        content_layout.addWidget(self.content)
        content_layout.addWidget(self.mode_button)

        # Basic window layout
        layout = QHBoxLayout(window_container)
        layout.addWidget(self.sidebar, 1)
        layout.addWidget(self.entry_list, 1)
        layout.addLayout(content_layout, 4)

        # "Journals/": Set path
        self.journals_path = Path(__file__).parent / "Journals"

        # Populate sidebar with real journals from disk
        for journal_name in list_journals(self.journals_path):
            self.sidebar.addItem(journal_name)

        # Add interactivity to journal button on click
        self.sidebar.itemClicked.connect(self.on_journal_clicked)
        # Add interactivity to entry button on click
        self.entry_list.itemClicked.connect(self.on_entry_clicked)


    def on_journal_clicked(self, item: QListWidgetItem):
        self.entry_list.clear()
        # "Journals/[current_journal]"
        self.journal_path = self.journals_path / item.text()
        entries = list_entries(self.journal_path)

        for entry in entries:
            self.entry_list.addItem(entry)

    def on_entry_clicked(self, item: QListWidgetItem):
        # "Journals/[current_journal]/[entry.md]"
        self.entry_path = self.journal_path / item.text()
        # Read current entry and display in content menu
        entry_text = self.entry_path.read_text()
        # Text will be editable for now, implementing viewing and editing toggle in later iteration
        self.content.setMarkdown(entry_text)

    # Implement toggle to change between edit and viewing modes
    # Freeze/Lock markdown for viewing -> Unfreeze for editing
