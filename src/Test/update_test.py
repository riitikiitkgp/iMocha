@app.route('/get_test_settings/<int:test_id>', methods=['GET'])
def get_test_settings(test_id):
    # Call the API to get the current test settings
    response = requests.get(f"{BASE_URL}/{test_id}/settings")
    return jsonify(response.json())


@app.route('/update_test_settings/<int:test_id>', methods=['POST'])
def update_test_settings(test_id):
    # Fetch current settings
    current_settings_response = requests.get(f"{BASE_URL}/{test_id}/settings")
    if current_settings_response.status_code != 200:
        return jsonify({"error": "Failed to fetch current test settings"}), current_settings_response.status_code

    current_settings = current_settings_response.json()

    # Get new settings from the request body
    new_settings = request.json

    # Update the current settings with the new values
    updated_settings = current_settings.copy()
    updated_settings.update(new_settings)

    # Send updated settings to the API
    response = requests.post(f"{BASE_URL}/{test_id}/settings", json=updated_settings)
    return jsonify(response.json()), response.status_code