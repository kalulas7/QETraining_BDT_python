import steps.users

def before_all(context):
    context.users = usersList()
    context.user_purchases = user_purchases()

