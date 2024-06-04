@app.route('/callbacks/process', methods=['POST'])\
def process_callbacks():
    request_data = request.json

    # Check if 'testinvitationIds' is present in the request body
    if 'testinvitationIds' not in request_data:
        return jsonify({'error': 'testinvitationIds is required'}), 400

    # Retrieve testinvitationIds from the request body
    testinvitationIds = request_data['testinvitationIds']

    # Check if testinvitationIds is a list
    if not isinstance(testinvitationIds, list):
        return jsonify({'error': 'testinvitationIds must be a list of integers'}), 400

    # Check if there are any testinvitationIds to process
    if not testinvitationIds:
        return jsonify({'error': 'No testinvitationIds provided'}), 400

    # Process a maximum of 100 testinvitationIds at a time
    chunk_size = 100
    for i in range(0, len(testinvitationIds), chunk_size):
        chunk = testinvitationIds[i:i + chunk_size]
        # Process the chunk of testinvitationIds here

        # Simulated processing for demonstration
        processed_ids = chunk

        # Log the processed testinvitationIds
        print("Processed testinvitationIds:", processed_ids)

    # Return success response
    return jsonify({'result': {'testinvitationIds': {'successful': testinvitationIds, 'failed': []}}, 'errors': None})