import os
from flask import Flask, render_template, request, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, EmailField, URLField,SubmitField
from wtforms.validators import DataRequired
from models import db, User
import qrcode





app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv('CSRF_SECRET_KEY')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///qr_generator.db"
app.config['IMAGE_FOLDER'] = 'static/images'



db.init_app(app)

    


class PersonDetailsForm(FlaskForm):
    full_name = StringField("Name", validators=[DataRequired()])
    position = StringField("Position", validators=[DataRequired()])
    phone = StringField("Phone", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired()])
    address = TextAreaField("Address")
    company_name = StringField("Company name")
    company_tag_line = StringField("Tag line")
    company_website = URLField("Website")
    submit = SubmitField('Generate',render_kw={"class":"btn btn-primary"})

@app.route('/', methods=["POST","GET"])
def generate_code():
    form = PersonDetailsForm()
 
    if request.method == "POST":
        if form.validate_on_submit():
            new_user = User(full_name=form.full_name.data, position=form.position.data, phone=form.phone.data, 
                            email=form.email.data, address=form.address.data,
                            company_name=form.company_name.data,
                            company_tag_line=form.company_tag_line.data,
                            company_website=form.company_website.data)
            db.session.add(new_user)
            db.session.commit()
            
            if new_user.id:
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
                app_url = os.getenv("APP_URL")
                url = f"{app_url}{url_for('get_user_details', id=new_user.id)}"
                qr.add_data(url)
                qr.make(fit=True)
                img = qr.make_image(fill_color="black", back_color="white")
                
                image_folder = app.config['IMAGE_FOLDER']
                if not os.path.exists(image_folder):
                    os.makedirs(image_folder) 
                
                image_path = os.path.join(image_folder, f'{new_user.id}_business_card.png')
                img.save(image_path)
                return redirect(url_for('download_file', id=new_user.id))
             
    return render_template('generate_qr.html', form=form)

@app.route('/user/<int:id>')
def get_user_details(id):
    user = db.get_or_404(User, id)
    return render_template('user_details.html', user=user)

@app.route('/download_file/<int:id>')
def download_file(id):
    return render_template('download_file.html', id=id)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)