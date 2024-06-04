@app.route('/callback', methods=['POST'])
def callback():
    try:
        # Parse the JSON data from the request
        data = request.get_json()

        # Log the received data (for debugging purposes)
        print(f"Received notification: {data}")

        # Extract necessary fields
        candidate_email = data.get("CandidateEmailId")
        status = data.get("Status")
        attempted_on = data.get("AttemptedOn")
        total_score = data.get("TotalScore")
        candidate_score = data.get("CandidateScore")
        report_pdf_url = data.get("ReportPDFUrl")
        test_invitation_id = data.get("TestInvitationId")
        performance_category = data.get("PerformanceCategory")

        # Process the data as needed (e.g., save to database, trigger other actions)
        # Here, you can add your custom logic to handle the notification

        # Return a success response
        return jsonify({"message": "Notification received successfully"}), 200

    except Exception as e:
        # Log the error (for debugging purposes)
        print(f"Error processing notification: {e}")

        # Return an error response
        return jsonify({"message": "Failed to process notification"}), 500