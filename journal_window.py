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
        self.mode_button = QPushButton("Viewing")
        self.new_entry_button = QPushButton("+")

        # Vertical entry list layout
        entry_list_layout = QVBoxLayout()
        entry_list_layout.addWidget(self.entry_list)
        entry_list_layout.addWidget(self.new_entry_button)

        # Vertical content layout
        content_layout = QVBoxLayout()
        content_layout.addWidget(self.content)
        content_layout.addWidget(self.mode_button)

        # Basic window layout
        layout = QHBoxLayout(window_container)
        layout.addWidget(self.sidebar, 1)
        layout.addLayout(entry_list_layout, 1)
        layout.addLayout(content_layout, 4)

        # "Journals/"
        self.journals_path = Path(__file__).parent / "Journals"

        # Set content to Viewing Mode by default
        self.content.setReadOnly(True)
        # Set Mode Button to Disabled (grayed out) by default
        self.mode_button.setEnabled(False)
        #! Also disable new entry button?

        # Populate sidebar with real journals from disk
        for journal_name in list_journals(self.journals_path):
            self.sidebar.addItem(journal_name)

        # Add interactivity to clicking journal
        self.sidebar.itemClicked.connect(self.on_journal_clicked)
        # Add interactivity to clicking entries
        self.entry_list.itemClicked.connect(self.on_entry_clicked)
        # Add interactivity to clicking mode button
        self.mode_button.clicked.connect(self.on_mode_button_clicked)
        # Add interactivity to clicking "+" (new entry)
        self.new_entry_button.clicked.connect(self.on_new_entry_clicked)

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
        self.entry_text = self.entry_path.read_text()
        self.content.setMarkdown(self.entry_text)

        # Enable button and set mode to Viewing
        self.mode_button.setEnabled(True)
        self.mode_button.setText("Viewing")
        self.content.setReadOnly(True)

    def on_new_entry_clicked(self):
        print("new entry clicked")

    def on_mode_button_clicked(self):
        if self.content.isReadOnly():
            # Currently viewing -> set to editing
            self.content.setReadOnly(False)
            self.content.setPlainText(self.entry_text)
            self.mode_button.setText("Editing")
        else:
            # Currently editing -> set to viewing
            self.content.setReadOnly(True)
            self.content.setMarkdown(self.entry_text)
            self.mode_button.setText("Viewing")
            
