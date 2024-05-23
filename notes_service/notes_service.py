# notes_service.py
from flask import Flask, request, jsonify

app = Flask(__name__)
notes = {}

@app.route('/notes', methods=['POST'])
def create_note():
    data = request.json
    note_id = data['idEstudiante']
    note = data['notaEstudiante']
    notes[note_id] = note
    return jsonify({"message": "Note created successfully"}), 201

@app.route('/notes/<idEstudiante>', methods=['GET'])
def get_note(idEstudiante):
    if idEstudiante in notes:
        return jsonify({"idEstudiante": idEstudiante, "notaEstudiante": notes[idEstudiante]}), 200
    return jsonify({"message": "Note not found"}), 404

@app.route('/notes/<idEstudiante>', methods=['PUT'])
def update_note(idEstudiante):
    if idEstudiante in notes:
        data = request.json
        notes[idEstudiante] = data['notaEstudiante']
        return jsonify({"message": "Note updated successfully"}), 200
    return jsonify({"message": "Note not found"}), 404

@app.route('/notes/<idEstudiante>', methods=['DELETE'])
def delete_note(idEstudiante):
    if idEstudiante in notes:
        del notes[idEstudiante]
        return jsonify({"message": "Note deleted successfully"}), 200
    return jsonify({"message": "Note not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
