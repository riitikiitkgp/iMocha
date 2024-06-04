@app.route('/tests/<int:test_id>', methods=['GET'])
def retrieve_test(test_id):
    try:
        # Fetch test details from iMocha API
        data = get_test_details(test_id)

        # Return the data in JSON format
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500