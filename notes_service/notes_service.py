from flask import Flask, request, jsonify

app = Flask(__name__)
notes = {}

@app.route('/notes', methods=['POST'])
def create_note():
    data = request.get_json()
    note_id = len(notes) + 1
    notes[note_id] = data
    return jsonify({"id": note_id}), 201

@app.route('/notes/<int:note_id>', methods=['GET'])
def get_note(note_id):
    note = notes.get(note_id)
    if note:
        return jsonify(note), 200
    return jsonify({"message": "Note not found"}), 404

@app.route('/notes/<int:note_id>', methods=['PUT'])
def update_note(note_id):
    data = request.get_json()
    if note_id in notes:
        notes[note_id] = data
        return jsonify({"message": "Note updated"}), 200
    return jsonify({"message": "Note not found"}), 404

@app.route('/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    if note_id in notes:
        del notes[note_id]
        return jsonify({"message": "Note deleted"}), 200
    return jsonify({"message": "Note not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
