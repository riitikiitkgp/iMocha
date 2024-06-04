@app.route('/retrieve_test_report/<int:test_invitation_id>', methods=['GET'])
def retrieve_test_report(test_invitation_id):
    # Endpoint URL
    url = f"https://apiv3.imocha.io/v3/reports/{test_invitation_id}?reportType=3"

    # Set headers with API key
    headers = {"Authorization": f"Bearer {API_KEY}"}

    # Make the request to the API
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Return the JSON response from the API
        return jsonify(response.json())
    else:
        # Return an error message if request fails
        return jsonify({"error": "Failed to retrieve test report"}), response.status_code