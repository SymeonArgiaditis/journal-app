# Journal

A simple, local, offline journal app for Windows.

## Why this exists

I wanted a plain journal app and couldn't find one that was actually plain.
Every option I found came with something I didn't want: an account to sign
up for, a subscription, a cloud sync I didn't ask for, an AI feature bolted
onto note-taking, or just general bloat from trying to be a do-everything
workspace app.

So this is the opposite of that, on purpose:

- No accounts, no login, no cloud
- No subscriptions, no payments, ever
- No AI features
- No ads, no telemetry
- Runs entirely on your machine
- Your entries are plain `.md` files, not locked into a database or a
  proprietary format

The app is just a window into a folder of markdown files sitting on your
own disk. If you stopped using the app tomorrow, your journal is still
just a folder of readable text files. Nothing is lost, nothing needs to be
"exported."

## What it does

- Organizes entries into journals (folders), e.g. a yearly journal, a
  dream journal, a travel journal — whatever you want to call them
- Lists entries within a journal, in order
- Lets you view an entry rendered (headers, code blocks, images, etc.)
- Lets you edit an entry as raw markdown
- Everything is stored as `.md` files on disk, readable by any text editor

## Installation

Requires Python 3.10+ (developed on 3.14) on Windows.

1. Clone the repository:
   ```
   git clone <repo-url>
   cd journal-app
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the app:
   ```
   python main.py
   ```

## Usage

- Journals appear in the left-hand sidebar. Click one to see its entries.
- Click an entry to open it in the content pane.
- Entries open in Viewing mode (rendered markdown, read-only). Switch to
  Editing mode to work with the raw markdown text directly.
- New entries are timestamped automatically when created.

## Data

Everything lives in a `Journals/` folder:

```
Journals/
  2025/
    2025-06-11_2000.md
    2025-06-14_1245.md
  Travel Journal/
    2026-06-01_1000.md
```

- Each journal is one folder. The folder name is whatever you named it —
  it has no special meaning to the app.
- Each entry is one `.md` file, named by the date and time it was created.
- Images referenced by an entry live alongside it and are linked with
  normal markdown image syntax.

This folder is the entire "database". You can back it up by copying it,
sync it yourself with whatever tool you already trust, or just leave it
alone on your own machine. The app never touches anything outside of it.

## Status

Actively being built as a personal project and a way to learn PySide6/Qt.
Expect rough edges. The core idea — plain files, no cloud, no nonsense —
isn't going to change.

## License

Not yet decided.
