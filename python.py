class Note:
    def __init__(self, id, title, body, timestamp):
        self.id = id
        self.title = title
        self.body = body
        self.timestamp = timestamp



import json

# Создание новой заметки
def create_note(id, title, body):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return Note(id, title, body, timestamp)

# Сохранение заметок в файл
def save_notes(notes, filename):
    with open(filename, "w") as file:
        json.dump([note.__dict__ for note in notes], file)

# Загрузка заметок из файла
def load_notes(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            notes = [Note(**note_data) for note_data in data]
            return notes
    except FileNotFoundError:
        return []

# Редактирование заметки по идентификатору
def edit_note(notes, id, new_title, new_body):
    for note in notes:
        if note.id == id:
            note.title = new_title
            note.body = new_body
            note.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return True
    return False

# Удаление заметки по идентификатору
def delete_note(notes, id):
    for note in notes:
        if note.id == id:
            notes.remove(note)
            return True
    return False
