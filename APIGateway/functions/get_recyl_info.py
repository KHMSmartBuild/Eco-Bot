from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/get_recycling_info', methods=['GET'])
def api_get_recycling_info():
    item = request.args.get('item')
    location = request.args.get('location')
    
    if not item or not location:
        return jsonify({"error": "Missing item or location parameter"}), 400
    
    result = get_recycling_info(item, location)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
