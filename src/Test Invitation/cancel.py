
@app.route('/cancel_invitation/<int:testInvitationId>', methods=['POST'])
def cancel_invitation(testInvitationId):
    # Define the API endpoint
    api_url = f'https://apiv3.imocha.io/v3/invitations/{testInvitationId}/cancel'

    # Make the POST request to the API
    response = requests.post(api_url)

    # Check the response status
    if response.status_code == 200:
        return jsonify(response.json()), 200
    elif response.status_code == 400:
        return jsonify(response.json()), 400
    else:
        return jsonify({"message": "An error occurred while cancelling the invitation."}), response.status_code