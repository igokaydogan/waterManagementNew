from data import Data
from gamspy import Container, Set, Parameter, Variable, Equation, Model, Sum, Sense, Options


def create_model(_data : Data):
    container = Container()



    """Create Sets"""
    i = container.addSet(name="i", records= _data.coef_matrix.columns.tolist(), description='groups')
    j = container.addSet(name = "j", records= _data.coef_matrix.index.values.tolist(), description='components')

    """Create Params"""
    csm = Parameter(container= container, name = 'csm', domain = [i,j], records = _data.current_state_matrix.unstack(), description = 'current state matrix')
    c = container.addParameter(name = 'c', domain= [i,j], records = _data.coef_matrix.unstack(), description = 'coefficient matrix')


    return container
