from behave import given, when, then
@given(u'I have 2 and 2')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I have 2 and 2')

@when(u'I select "sum"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I select "sum"')

@then(u'My result should be "4"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then My result should be "4"')
