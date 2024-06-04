# Define a route to handle the request for exporting the PDF report
@app.route('/export_pdf_report/<int:test_invitation_id>', methods=['GET'])
def export_pdf_report(test_invitation_id):
    # Assuming you have the test invitation ID from the request URL parameters
    # You can replace this with your logic to fetch the PDF report URL

    # Dummy PDF report URL for demonstration
    pdf_report_url = f"https://app.imocha.io/PDFReport?id={test_invitation_id}"

    # Return the PDF report URL in the response
    response = {
        "pdfReport": pdf_report_url
    }

    return jsonify(response)
