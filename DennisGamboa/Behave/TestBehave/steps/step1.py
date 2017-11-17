from behave import given
@given("User navigates {amount:d} to the Google home page")
def step_impl(context, amount):
    print(amount)




