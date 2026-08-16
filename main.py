from PySide6.QtWidgets import QApplication
from journal_window import JournalWindow

import sys

app = QApplication()

window = JournalWindow()
window.show()

sys.exit(app.exec())
