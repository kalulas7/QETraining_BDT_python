from behave import given, when, then
from compare import expect
@given(u'I have ${total_amount} in my account')
def step_impl(context, total_amount):
    context.total_amount = int(total_amount)

@when(u'I choose to withdraw the fixed amount of ${capture_amount}')
def step_impl(context, capture_amount):
    context.capture_amount = int(capture_amount)

@then(u'I should receive ${optain_amount} cash')
def step_impl(context, optain_amount):
    print("it is your cash", optain_amount)

@then(u'the balance of my account should be ${balance_total}')
def step_impl(context, balance_total):
    remaining = context.total_amount - context.capture_amount
    expect(remaining).to_equal(int(balance_total))
    print("it is your balance", remaining)
