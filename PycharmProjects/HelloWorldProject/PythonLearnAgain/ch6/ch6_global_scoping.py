i = 10
def increment_By_one():
    print('from- increment_By_one() ',i) # this will work because it first referes to local scope and if the value is not present it refres to
    #global scope. To make this work comment out hte

def does_not_work():
    try:
        i = i + 1  # this will not work because you are tring to assing a value by not initializing
        print(i)

    except Exception as e:
        print('ERRRRRORRRRR',e)



def referring_to_variable_in_global_scope():
    global i
    i = i + 1 # this will work since we have referred to global i
    print('Value from the Global Scope Method: ',i)

def global_value_is_changed():
    global i
    print('Value from the global Value that is changed after the function called above: ',i)
    print('Value is change to 11 no since we incremented the global scope')

if __name__ == '__main__':
    print(increment_By_one())
    does_not_work()
    referring_to_variable_in_global_scope()
    global_value_is_changed()
    # here is the order of where the value are looked up.
    '''
    1. Local function definition scope
    2. Global - which is at the module level
    3. Built-in Namespace
    '''