@app.route('/invite', methods=['POST'])
def invite_candidate():
    data = request.json
    test_id = data.get('testId')
    test_link_id = data.get('testLinkId')
    candidate_email = data.get('email')
    candidate_name = data.get('name')
    callback_url = data.get('callbackUrl', '')
    redirect_url = data.get('redirectUrl', '')
    disable_mandatory_fields = data.get('disableMandatoryFields', 0)
    hide_instruction = data.get('hideInstruction', 0)
    send_email = data.get('sendEmail', 'no')

    if not test_id or not test_link_id or not candidate_email or not candidate_name:
        return jsonify({"error": "testId, testLinkId, email, and name are required"}), 400

    api_url = f"https://apiv3.imocha.io/v3/tests/{test_id}/testlinks/{test_link_id}/invite"

    payload = {
        "email": candidate_email,
        "name": candidate_name,
        "callbackUrl": callback_url,
        "redirectUrl": redirect_url,
        "disableMandatoryFields": disable_mandatory_fields,
        "hideInstruction": hide_instruction,
        "sendEmail": send_email
    }

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(api_url, json=payload, headers=headers)

    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({"error": response.json()}), response.status_code