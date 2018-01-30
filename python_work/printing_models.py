def print_models(unprinted_designs, completed_models):
    """
    mock print every design, until have no unprited design
    after printing every design, move it in the list where named completed_models
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # mock the process which according to design making a 3D print model
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """ show all the print complete model """
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


