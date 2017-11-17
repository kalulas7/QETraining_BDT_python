from behave import given
@given(u'only numbers zipcode: {zipcode:d}')
def step_impl(context, zipcode):
    #raise NotImplementedError(u'STEP: Given only numbers zipcode: 452630')
    print(zipcode)

@given(u'letters or underscore: {country_city:w}')
def step_impl(context, country_city):
    #raise NotImplementedError(u'STEP: Given letters or underscore: Brasil_SaoPaulo')
    print(country_city)

@given(u'numbers with thousands separator: {thousands:f}')
def step_impl(context, thousands):
    #raise NotImplementedError(u'STEP: Given numbers with thousands separator: 1.000')
    print(thousands)
