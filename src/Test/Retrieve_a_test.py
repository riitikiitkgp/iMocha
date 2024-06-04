@app.route('/tests/<int:testId>', methods=['GET'])
def get_test(testId):
    if not is_authorized():
        return jsonify({
            "statusCode": 401,
            "message": "Access denied due to invalid subscription key."
        }), 401

    # Retrieve the test from the database
    test = db.get(testId)
    if test is None:
        abort(404)  # Not Found

    return jsonify(test)

def is_authorized():
    # Placeholder function for checking authorization
    # Replace with actual logic to verify the subscription key or token
    return True