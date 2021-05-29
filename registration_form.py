from flask_wtf import FlaskForm
from wtforms import SelectField, validators, StringField, RadioField
from wtforms.fields.html5 import DateField, EmailField


class RegistrationForm(FlaskForm):
    chapter = SelectField('Chapter', [validators.DataRequired()], choices=["North Delhi",
                                                                           "South Delhi",
                                                                           "Kurukshetra",
                                                                           "Dehradun",
                                                                           "Kolkata",
                                                                           "Aurangabad",
                                                                           "Phagwara",
                                                                           "Gurugram",
                                                                           "Gr. Noida",
                                                                           "Hydrabad",
                                                                           "Haridwar",
                                                                           "Jaipur",
                                                                           "South Mumbai",
                                                                           "West Mumbai",
                                                                           "Chennai",
                                                                           "Panchkula",
                                                                           "Baddi",
                                                                           "Pune",
                                                                           "Bengaluru",
                                                                           "Vadodara",
                                                                           "Noida",
                                                                           "Ahmedabad"
                                                                           ])

    first_name = StringField('First Name', [validators.DataRequired()])
    middle_name = StringField('Middle Name', [validators.DataRequired()])
    last_name = StringField('Last Name', [validators.DataRequired()])

    gender = RadioField('Gender', [validators.DataRequired()], choices=['Female', 'Male'])
    date_of_birth = DateField('Date of Birth', [validators.DataRequired()])
    contact_number = StringField('Contact Number', [validators.DataRequired()])

    home_address = StringField('Home Address', [validators.DataRequired()])
    country = StringField('Country', [validators.DataRequired()])
    state = StringField('State', [validators.DataRequired()])
    city = StringField('City', [validators.DataRequired()])

    email = EmailField('Email Address', [validators.DataRequired()])
    religion = StringField('Religion', [validators.DataRequired()])
    caste = StringField('Caste', [validators.DataRequired()])

    # field = StringField('S.NO.', [validators.DataRequired()])
    # field = StringField('First Name', [validators.DataRequired()])
    # field = StringField('Middle Name', [validators.DataRequired()])
    # field = StringField('Last Name', [validators.DataRequired()])
    # field = StringField('Gender', [validators.DataRequired()])
    # field = StringField('Age', [validators.DataRequired()])
    # field = StringField('Date of Birth' description='(MM/DD/YYYY)', [validators.DataRequired()])
    # field = StringField('Contact Number' description='(Whatsapp number if you are using whatsapp application)', [validators.DataRequired()])
    # field = StringField('Home Address with Pincode' description='( Add landmark)', [validators.DataRequired()])
    # field = StringField('Country', [validators.DataRequired()])
    # field = StringField('State', [validators.DataRequired()])
    # field = StringField('City', [validators.DataRequired()])
    # field = StringField('Email ID', [validators.DataRequired()])
    # field = StringField('Religion' description='(for information only)', [validators.DataRequired()])
    # field = StringField('Caste ', [validators.DataRequired()])
    # field = StringField('Do you fall under any reservation category of government', [validators.DataRequired()])
    # field = StringField('Disability' description='(for information only):  Yes / No ', [validators.DataRequired()])
    # field = StringField('Type of disability if any', [validators.DataRequired()])
    # field = StringField('Marital status of candidate', [validators.DataRequired()])
    # field = StringField('Identification Type', [validators.DataRequired()])
    # field = StringField('Enter your Aadhar Card  Number.', [validators.DataRequired()])
    # field = StringField('Add your passport size photograph here', [validators.DataRequired()])
    # field = StringField('Name of the School ', [validators.DataRequired()])
    # field = StringField('If any other' description='(school name)', [validators.DataRequired()])
    # field = StringField('Stream' description='(Science /Commerce /Arts/)', [validators.DataRequired()])
    # field = StringField('If Vocational Course add course details ', [validators.DataRequired()])
    # field = StringField('Address of School ', [validators.DataRequired()])
    # field = StringField('Applied Before?', [validators.DataRequired()])
    # field = StringField('Recently passed 10th/ 12th Std in 2021', [validators.DataRequired()])
    # field = StringField('Percentage of 10th Board Examination', [validators.DataRequired()])
    # field = StringField('Distinction in any subject' description='(write above 75 marks obtained subject names)', [validators.DataRequired()])
    # field = StringField('Passing Year' description='(10th class)', [validators.DataRequired()])
    # field = StringField('Name of school from where you passed class 10th', [validators.DataRequired()])
    # field = StringField(' Name of the Board' description='(Class 10th)', [validators.DataRequired()])
    # field = StringField('Current Class', [validators.DataRequired()])
    # field = StringField('Excellence in any other Field' description='(Sports, Arts, Debates, etc.)', [validators.DataRequired()])
    # field = StringField('Hobbies', [validators.DataRequired()])
    # field = StringField('Add copy of your 10th Marksheet', [validators.DataRequired()])
    # field = StringField('Add fee slip if any of class 11th', [validators.DataRequired()])
    # field = StringField('Father's Name', [validators.DataRequired()])
    # field = StringField('Father's Age ', [validators.DataRequired()])
    # field = StringField('Father's Gender', [validators.DataRequired()])
    # field = StringField('Father's Qualification ', [validators.DataRequired()])
    # field = StringField('Marital status of Father', [validators.DataRequired()])
    # field = StringField('Occupation' description='(What work your father does)', [validators.DataRequired()])
    # field = StringField('Father's monthly income' description='(Salary)', [validators.DataRequired()])
    # field = StringField('Mother's Name ', [validators.DataRequired()])
    # field = StringField('Mother's Age ', [validators.DataRequired()])
    # field = StringField('Mother's Gender', [validators.DataRequired()])
    # field = StringField('Mother's Qualification ', [validators.DataRequired()])
    # field = StringField('Mother's Marital Status ', [validators.DataRequired()])
    # field = StringField('Occupation' description='(What work your mother does)', [validators.DataRequired()])
    # field = StringField('Mother monthly income' description='(Salary)', [validators.DataRequired()])
    # field = StringField('Single Parents/No Parents', [validators.DataRequired()])
    # field = StringField('If case of Single parent, Who is the parent?', [validators.DataRequired()])
    # field = StringField('Details about Guardian  ' description='(Details like age, education, married or not, working or not)', [validators.DataRequired()])
    # field = StringField('Do you have brother /sister?', [validators.DataRequired()])
    # field = StringField('Details about Brothers & Sisters' description='(if you have any)' description='(Details like age, education, married or not, working or not)', [validators.DataRequired()])
    # field = StringField('Annual Family Income', [validators.DataRequired()])
    # field = StringField('Is any of your sibling has been a beneficiary of the Udayan Shalini Fellowships' description='(If yes, give details)', [validators.DataRequired()])
    # field = StringField('Assets owned by the family' description='(Give Details)A] Immovable property. ', [validators.DataRequired()])
    # field = StringField('Details, if any other', [validators.DataRequired()])
    # field = StringField('Attach images of your Address proof.' description='(attach Ration Card Or  Aadhar Card of father or mother)', [validators.DataRequired()])
    # field = StringField('Income certificate of Father /Mother /guardian issued by the Govt. Tehsil/ Talathi/ Or Employer/organization with the designation.' description='( Old certificate can be attached for reference). Please Note- If it's not available at the moment, form will be accepted but it is mandatory to present income certificate during interview process if selected in written exam.', [validators.DataRequired()])
    # field = StringField('Teacher’s name', [validators.DataRequired()])
    # field = StringField('Subjects taught by the teacher', [validators.DataRequired()])
    # field = StringField('No. of years taught by the teacher', [validators.DataRequired()])
    # field = StringField('Teacher's contact number', [validators.DataRequired()])
    # field = StringField('Principal's name', [validators.DataRequired()])
    # field = StringField('School's contact number ', [validators.DataRequired()])
    # field = StringField('Specify the reason for selecting the Stream in 11th class' description='(Science/Commerce/Arts) ', [validators.DataRequired()])
    # field = StringField('Your ambition ', [validators.DataRequired()])
    # field = StringField('Any Special Awards for Academics or Co-curricular Activities ', [validators.DataRequired()])
    # field = StringField('Who/What motivates you to move ahead in life?', [validators.DataRequired()])
    # field = StringField('What are your 3 strengths?', [validators.DataRequired()])
    # field = StringField('  What are your 3 weaknesses? ', [validators.DataRequired()])
    # field = StringField('Why do you think that you are a deserving candidate for this fellowship? ', [validators.DataRequired()])
    # field = StringField('Attach  Candidate Proof of Bank Account' description='(Copy of passbook)', [validators.DataRequired()])
    # field = StringField('Attach a photo of Aadhaar Card of the applicant', [validators.DataRequired()])
    # field = StringField('DECLARATION1. I, hereby, declare that all the information furnished above is true to the best of my knowledge. I also understand that if any of the above information is found to be incorrect, the fellowship will be withdrawn 2. I have read all the rules and regulations of the organization and promise to follow them. I also understand that in case my fellowship is withdrawn due to any of the reasons mentioned in Annexure1, the decision of the organization will be final and abiding', [validators.DataRequired()])

    # password = PasswordField('New Password', [
    #     validators.DataRequired(),
    #     validators.EqualTo('confirm', message='Passwords must match')
    # ])
    # confirm = PasswordField('Repeat Password')
    # accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])
