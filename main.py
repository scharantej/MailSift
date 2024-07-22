
# main.py

from flask import Flask, render_template, request, redirect, url_for
import googleapiclient.discovery

app = Flask(__name__)

# Gmail API Discovery
gmail_service = googleapiclient.discovery.build('gmail', 'v1', credentials=googleapiclient.file.Storage('credentials.json').get())

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    sender_address = request.form.get('sender_address')
    subject_line = request.form.get('subject_line')
    body_keywords = request.form.get('body_keywords')
    
    filter_params = {'criteria': {}}
    if sender_address:
      filter_params['criteria']['from'] = sender_address
    if subject_line:
      filter_params['criteria']['subject'] = subject_line
    if body_keywords:
      filter_params['criteria']['body'] = body_keywords
    
    try:
      filter_response = gmail_service.users().filters().insert(userId='me', body=filter_params).execute()
    except Exception as e:
      print(f"An error occurred: {e}")
      return render_template('index.html', error=e)

    return redirect(url_for('filters'))

  return render_template('index.html')

@app.route('/filters')
def filters():
  try:
    filters_response = gmail_service.users().filters().list(userId='me').execute()
  except Exception as e:
    print(f"An error occurred: {e}")
    return render_template('filters.html', error=e)

  return render_template('filters.html', filters=filters_response['filters'])

if __name__ == '__main__':
  app.run(debug=True)
