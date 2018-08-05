import os
import click

from .online_medical_dictionary import store_omd_terms


if __name__ == '__main__':
    directory = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'data')
    store_omd_terms(directory)
