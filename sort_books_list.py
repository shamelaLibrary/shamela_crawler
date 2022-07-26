from pathlib import Path

import json

books = json.loads(Path("books_list.json").read_text())

# order the list of dicts by book link
books.sort(key=lambda x: x["link"].split("/")[-1].zfill(20))
# write the new list to the file
Path("books_list.json").write_text(json.dumps(books, indent=1, ensure_ascii=False))
