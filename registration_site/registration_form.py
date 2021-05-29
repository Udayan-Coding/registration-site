from flask_wtf import FlaskForm
from wtforms import SelectField, validators, StringField, RadioField, TextAreaField, BooleanField, \
    FloatField, IntegerField as NumberField
from wtforms.fields.html5 import DateField, EmailField, IntegerField

chapters = ["North Delhi",
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
            ]

countries = ['India']

states = ['Andhra Pradesh',
          'Arunachal Pradesh',
          'Assam',
          'Bihar',
          'Chhattisgarh',
          'Delhi',
          'Goa',
          'Gujarat',
          'Haryana',
          'Himachal Pradesh',
          'Jharkhand',
          'Karnataka',
          'Kerala',
          'Madhya Pradesh',
          'Maharashtra',
          'Manipur',
          'Meghalaya',
          'Mizoram',
          'Nagaland',
          'Odisha',
          'Punjab',
          'Rajasthan',
          'Sikkim',
          'TamilNadu',
          'Telangana',
          'Tripura',
          'Uttar Pradesh',
          'Uttarakhand',
          'West Bengal']

union_territories = [
    'Andaman and Nicobar Islands',
    'Chandigarh',
    'Dadra and Nagar Haveli and Daman and Diu',
    'Jammu and Kashmir',
    'Ladakh',
    'Lakshadweep',
    'Puducherry'
]


class RegistrationForm(FlaskForm):
    chapter = SelectField('Chapter', [validators.DataRequired()], choices=chapters)

    first_name = StringField('First Name', [validators.DataRequired()])
    middle_name = StringField('Middle Name')
    last_name = StringField('Last Name')

    gender = RadioField('Gender', [validators.DataRequired()], choices=['Female', 'Male'])
    date_of_birth = DateField('Date of Birth', [validators.DataRequired()])
    contact_number = StringField('Contact Number', [validators.DataRequired()],
                                 description="Please provide your WhatsApp number if you use "
                                             "WhatsApp")

    home_address = TextAreaField('Home address', [validators.DataRequired()],
                                 description='Please add a landmark')
    pin_code = NumberField('PIN Code', [validators.DataRequired(), validators.Length(min=6, max=8)])

    country = SelectField('Country', [validators.DataRequired()], choices=countries)
    state = SelectField('State', [validators.DataRequired()], choices=states)
    city = StringField('City', [validators.DataRequired()])

    email = EmailField('Email ID', [validators.DataRequired()])

    religion = StringField('Religion', [validators.DataRequired()],
                           description='For information only')

    caste = StringField('Caste', [validators.DataRequired()], )

    reservation = RadioField('Do you fall under any reservation category of government',
                             [validators.DataRequired()],
                             choices=['General', 'SC', 'ST', 'OBC'])

    has_disability = RadioField('Disability', description='For information only',
                                choices=['Yes', 'No'])
    disability = StringField('Type of disability (if any)',
                             description='If selected \'Yes\' to above question please state')

    marital_status = StringField('Marital status',
                                 description='Please state if you are single, married or any other')

    identification_type = RadioField('Identification Type', [validators.DataRequired()],
                                     choices=['Aadhar card'])

    aadhar_card_number = StringField('Aadhar Card Number.',
                                     [validators.DataRequired(), validators.Length(min=12, max=12)])

    # field = StringField('Add your passport size photograph here', [validators.DataRequired()])

    school = StringField('School ', [validators.DataRequired()])
    additional_school = StringField('Any other school')

    stream = RadioField('Stream', [validators.DataRequired()],
                        choices=['Science', 'Commerce', 'Arts', 'Vocational'])

    vocational_course_details = StringField('Vocational course details',
                                            description='If you have taken a vocational course,'
                                                        ' add details here')

    school_address = TextAreaField('Address of School', [validators.DataRequired()])

    applied_before = BooleanField('Applied Before?', [validators.DataRequired()])

    recent_10th_12th = BooleanField('Recently passed 10th/12th Std in 2021?',
                                    [validators.DataRequired()])

    matric_pct = FloatField('Percentage of 10th Board Examination', [validators.DataRequired()])

    distinction_subjects_10th = StringField('Distinction in any subject',
                                            description='Mention subjects with 75 marks and above')

    passing_year_10th = IntegerField('Passing Year (10th)', [validators.DataRequired()])

    school_10th = StringField('Name of school from where you passed class 10th',
                              [validators.DataRequired()])
    board_10th = StringField(' Name of the Board', [validators.DataRequired()])

    current_class = StringField('Current Class', [validators.DataRequired()])

    excellence_field = StringField('Excellence in any other Field',
                                   [validators.DataRequired()],
                                   description='(Sports, Arts, Debates, etc.)')

    hobbies = StringField('Hobbies', [validators.DataRequired()])

    # field = StringField('Add copy of your 10th Marksheet', [validators.DataRequired()])
    # field = StringField('Add fee slip if any of class 11th', [validators.DataRequired()])

    fathers_name = StringField("Father's Name", [validators.DataRequired()])
    fathers_age = IntegerField("Father's Age", [validators.DataRequired()])

    fathers_gender = StringField("Father's Gender", [validators.DataRequired()])
    fathers_qualification = StringField("Father's Qualification", [validators.DataRequired()])

    fathers_marital_status = StringField('Marital status of Father', [validators.DataRequired()])

    fathers_occupation = StringField('Occupation', [validators.DataRequired()],
                                     description='What work your father does')
    fathers_monthly_income = IntegerField("Father's monthly income", [validators.DataRequired()],
                                          description="Salary")

    mothers_name = StringField("Mother's Name", [validators.DataRequired()])
    mothers_age = IntegerField("Mother's Age", [validators.DataRequired()])

    mothers_gender = StringField("Mother's Gender", [validators.DataRequired()])
    mothers_qualification = StringField("Mother's Qualification", [validators.DataRequired()])

    mothers_marital_status = StringField('Marital status of Mother', [validators.DataRequired()])

    mothers_occupation = StringField('Occupation', [validators.DataRequired()],
                                     description='What work your mother does')
    mothers_monthly_income = IntegerField("Mother's monthly income", [validators.DataRequired()],
                                          description="Salary")

    has_single_parents = BooleanField('Single Parents/No Parents')
    who_is_single_parent = RadioField('If case of Single parent, Who is the parent?',
                                      choices=['Mother', 'Father'])

    guardian_details = StringField('Details about Guardian',
                                   description='Details like age, education, married?, occupation')

    has_sibling = BooleanField('Do you have brother/sister?', [validators.DataRequired()])

    sibling_details = TextAreaField('Details about Brothers & Sisters (if any)',
                                    description='Details like age, education, married or not,'
                                                ' working or not')

    annual_family_income = StringField('Annual Family Income', [validators.DataRequired()])
    sibling_beneficiary = StringField(
        'Is any of your sibling has been a beneficiary of the Udayan Shalini Fellowships?',
        description='(If yes, give details)')

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
