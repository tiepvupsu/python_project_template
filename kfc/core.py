# -*- coding: utf-8 -*-
from kfc import helpers


def get_hmm():
    """Get a thought."""
    return "hmmm..."


def hmm():
    """Contemplation..."""
    if helpers.get_answer():
        print(get_hmm())
