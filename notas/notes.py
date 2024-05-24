# notes_service.py
from flask import Flask, request, jsonify, render_template

app = Flask(__name__, template_folder='./templates')
notes = {}

@app.route('/notes/index')
def index():
    return render_template("note_index.html")

@app.route('/notes/index/note', methods=['POST'])
def create_note():
    data = request.json
    note_id = data['idEstudiante']
    try: #check if id is a number
        note_id = int(note_id)
    except ValueError:
        return jsonify({"message": "Value idEstudiante must be a number", "Value": note_id})

    note = data['notaEstudiante']
    try: #check if note is a float
        note = float(note)
    except ValueError:
        return jsonify({"message": "Value notaEstudiante must be a number", "Value": note})
    
    if note_id in notes:
        return jsonify({"errorMessage": "ID already in Database"})
    else:
        notes[note_id] = note
        return jsonify({"message": "Note created successfully"}), 201

#@app.route('/notes/index/note', methods=['GET'])
#def get_all_notes():
#    return jsonify({"all entries": notes}),200

@app.route('/notes/index/note/<idEstudiante>', methods=['GET'])
def get_note(idEstudiante):
    idEstudiante = int(idEstudiante)
    if idEstudiante in notes:
        return jsonify({"notaEstudiante": notes[idEstudiante]}), 200
    else:
        return jsonify({"message": "Note not found", "value":idEstudiante}), 404

@app.route('/notes/index/note/<idEstudiante>', methods=['PUT'])
def update_note(idEstudiante):
    idEstudiante = int(idEstudiante)
    if idEstudiante in notes:
        data = request.json
        newNote = data['notaEstudiante']
        try:
            newNote = float(newNote)
        except ValueError:
            return jsonify({"message": "Value notaEstudiante must be a number", "Value": newNote})

        notes[idEstudiante] = newNote
        return jsonify({"message": "Note updated successfully", "Value": idEstudiante}), 200
    else:
        return jsonify({"message": "Note not found", "Value": idEstudiante}), 404

@app.route('/notes/index/note/<idEstudiante>', methods=['DELETE'])
def delete_note(idEstudiante):
    idEstudiante = int(idEstudiante)
    if idEstudiante in notes:
        del notes[idEstudiante]
        return jsonify({"message": "Note deleted successfully", "Value": idEstudiante}), 200
    return jsonify({"message": "Note not found"}), 404

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5002)
