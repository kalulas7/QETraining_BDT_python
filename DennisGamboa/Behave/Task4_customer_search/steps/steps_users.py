from behave import given, when, then
from compare import expect

@given(u'A {user:w} and {userid:d} to search')
def step_impl(context, user, userid):
    context.user = user
    context.userid = userid

@when(u'I want to search by {amount:d}')
def step_impl(context, amount):
    context.amount = amount
    #print("entra al if")
    if context.amount in context.user_purchase.values():
        #print("entro")
        expect(context.user_purchase[context.u_id]).to_equal(context.amount)

@then(u'I get the {user:w} and the {amount:d}')
def step_impl(context, user, amount):
    #print("final")
    if context.userid in context.user_purchase.keys():
        print("User: ", context.users.key[context.userid], "\n")
        print("Amount", context.user_purchase[context.userid])
