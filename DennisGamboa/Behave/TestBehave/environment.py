import yaml

global generic_data
generic_data = yaml.load(open('settings/config.yml'))

def before_all(context):
    context.host = generic_data['host']
    context.method = generic_data['method']
    context.code = generic_data['code']
    print("*************BEFORE ALL*************", context.host, context.method, context.code)

def before_feature(context, feature):
    if 'try' in feature.tags:
        print("/////////FEATURE TRY ///////")
    if 'Withdraw' in feature.name:
        print("***************************test feature************")

def before_scenario(context, scenario):
    if 'scenario' in scenario.tags:
        print("//////////scenario/////////")
    if 'Withdraw fixed amount' in scenario.name:
        print("/////////scenario2//////////")

def before_step(context, steps):
    if 'I should' in steps.name:
        print("**************step1**********")