
@app.route('/reattempt', methods=['POST'])
def reattempt_test():
    data = request.json
    test_invitation_id = data.get('testInvitationId')
    start_datetime = data.get('StartDateTime')
    end_datetime = data.get('EndDateTime')
    timezone_id = data.get('TimeZoneId')
    callback_url = data.get('CallbackUrl', '')
    redirect_url = data.get('RedirectUrl', '')
    hide_instruction = data.get('hideInstruction', 0)
    send_email = data.get('sendEmail', 'no')

    # Construct the API request payload
    payload = {
        "StartDateTime": start_datetime,
        "EndDateTime": end_datetime,
        "TimeZoneId": timezone_id,
        "CallbackUrl": callback_url,
        "redirectURL": redirect_url,
        "hideInstruction": hide_instruction,
        "sendEmail": send_email
    }

    # API endpoint URL
    api_url = f"https://apiv3.imocha.io/v3/invitations/{test_invitation_id}/reattempt"

    # Make the API request
    response = requests.post(api_url, json=payload)

    # Check the response status and return accordingly
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify(response.json()), response.status_code
