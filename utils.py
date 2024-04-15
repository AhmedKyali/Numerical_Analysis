from sympy import *
import re

def transform_expression(expression):
    terms = re.split(r'([-+*/])', expression)
    transformed_terms = []
    for term in terms:
        if 'x' in term:
            if term.startswith('x'):
                term = '1' + term  # add coefficient 1 if none exists
            term = term.replace('x', '*x')
            term = term.replace('^', '**')
        transformed_terms.append(term)

    return ''.join(transformed_terms)
