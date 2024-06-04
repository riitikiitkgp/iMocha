@app.route('/get_test_settings', methods=['GET'])
def get_test_settings():
    test_id = request.args.get('testId')
    if not test_id:
        return jsonify({"error": "testId is required"}), 400

    api_url = f"https://apiv3.imocha.io/v3/tests/{test_id}/settings"

    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({"error": "Failed to retrieve test settings"}), response.status_code