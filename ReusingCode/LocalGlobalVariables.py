global_var = 'I am global'

def demo_scope():
    local_var = 'I am local'
    print(global_var)
    print(local_var)

# Call the function
demo_scope()
