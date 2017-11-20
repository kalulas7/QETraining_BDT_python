@given(u'A register form page is loaded')
def step_impl(context):
    print("form page is displayed \n")

@when(u'User fill the FirstName field with {firtsname:w}')
def step_impl(context, firtsname):
    print("Name: ", firtsname, "\n")

@when(u'User fill the LastName field with {lastname:w}')
def step_impl(context, lastname):
    print("Last Name: ", lastname, "\n")

@when(u'User fill the Username field with {username:w}')
def step_impl(context, username):
    print("User Name: ", username, "\n")

@when(u'User fill the Password field with {password:w}')
def step_impl(context, password):
    print("Password: ", password, "\n")

@when(u'User fill the Confirm your password field with {conf_password:w}')
def step_impl(context, conf_password):
    print("Confirm Password: ", conf_password, "\n")

@when(u'User select {month:w} option on Birthday select box')
def step_impl(context, month):
    print("Birthday datas")
    print("Month: ", month, "\n")

@when(u'User fill the Day field with {day:d}')
def step_impl(context, day):
    print("Day: ", day, "\n")

@when(u'User fill the Year field with {year:d}')
def step_impl(context, year):
    print("Year: ", year, "\n")

@when(u'User select {gender:w} option on Gender select box')
def step_impl(context, gender):
    print("I am :", gender, "\n")

@when(u'User select {country:w} option on Mobile phone select box')
def step_impl(context, country):
    print("Country: ", country, "\n")

@when(u'User fill the Phone filed with {phone_number:d}')
def step_impl(context, phone_number):
    print("Phone number: ", phone_number, "\n")

@when(u'User fill the Email Address field with {email}')
def step_impl(context, email):
    print("Email: ", email, "\n")

@then(u'all data is validated')
def step_impl(context):
    print("All data are validated")