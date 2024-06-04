@app.route('/tests', methods=['GET'])
def get_tests():
    # Extracting optional query parameters
    page_no = request.args.get('pageNo', 1)
    page_size = request.args.get('pageSize', 100)
    labels_filter = request.args.get('labelsFilter', '')
    status = request.args.get('status', '')

    params = {
        'pageNo': page_no,
        'pageSize': page_size,
        'labelsFilter': labels_filter,
        'status': status
    }

    response = requests.get(API_BASE_URL, params=params)

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Failed to fetch tests', 'details': response.json()}), response.status_code
