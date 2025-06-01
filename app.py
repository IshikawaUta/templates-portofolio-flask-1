import os
from flask import Flask, render_template, request, flash, redirect, url_for, send_from_directory
from flask_mail import Mail, Message
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER')
app.config['MAIL_PORT'] = int(os.environ.get('MAIL_PORT'))
app.config['MAIL_USE_TLS'] = os.environ.get('MAIL_USE_TLS') == 'True'
app.config['MAIL_USE_SSL'] = os.environ.get('MAIL_USE_SSL') == 'True'
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME')

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your_secret_key_here_for_dev')

mail = Mail(app)

app.static_folder = 'static'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/robots.txt')
def serve_robots():
    return send_from_directory(app.static_folder, 'robots.txt', mimetype='text/plain')

@app.route('/sitemap.xml')
def serve_sitemap():
    return send_from_directory(app.static_folder, 'sitemap.xml', mimetype='application/xml')

@app.route('/send_message', methods=['POST'])
def send_message():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message_body = request.form['message']

        recipient_email = os.environ.get('RECIPIENT_EMAIL')

        msg = Message(
            subject=f"Pesan dari Portofolio: {subject}",
            sender=app.config['MAIL_USERNAME'],
            recipients=[recipient_email]
        )
        msg.body = f"""
        Nama: {name}
        Email: {email}
        Subjek: {subject}

        Pesan:
        {message_body}
        """

        try:
            mail.send(msg)
            flash('Pesan Anda berhasil dikirim!', 'success')
        except Exception as e:
            flash(f'Gagal mengirim pesan: {str(e)}', 'danger')

        return redirect(url_for('index', _anchor='kontak'))

if __name__ == '__main__':
    app.run(debug=True)
