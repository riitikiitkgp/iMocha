@app.route('/invite', methods=['POST'])
def invite_candidate():
    data = request.json

    # Required fields
    email = data.get('email')
    name = data.get('name')
    testId = data.get('testId')

    if not email or not name or not testId:
        return jsonify({"error": "email, name, and testId are required"}), 400

    # Optional fields
    callbackUrl = data.get('callbackUrl')
    redirectUrl = data.get('redirectUrl')
    disableMandatoryFields = data.get('disableMandatoryFields', 0)
    hideInstruction = data.get('hideInstruction', 0)
    sendEmail = data.get('sendEmail', "no")
    stakeholderEmails = data.get('stakeholderEmails')
    startDateTime = data.get('startDateTime')
    endDateTime = data.get('endDateTime')
    timeZoneId = data.get('timeZoneId')
    proctoringMode = data.get('proctoringMode', "disabled")

    # Prepare request payload
    payload = {
        "email": email,
        "name": name,
        "callbackUrl": callbackUrl,
        "redirectUrl": redirectUrl,
        "disableMandatoryFields": disableMandatoryFields,
        "hideInstruction": hideInstruction,
        "sendEmail": sendEmail,
        "stakeholderEmails": stakeholderEmails,
        "startDateTime": startDateTime,
        "endDateTime": endDateTime,
        "timeZoneId": timeZoneId,
        "proctoringMode": proctoringMode
    }

    # Remove keys with None values
    payload = {k: v for k, v in payload.items() if v is not None}

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {IMOCHA_API_KEY}"
    }

    # Send POST request to iMocha API
    response = requests.post(IMOCHA_API_URL.format(testId=testId), json=payload, headers=headers)

    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify(response.json()), response.status_code