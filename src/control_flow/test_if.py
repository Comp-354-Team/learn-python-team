"""IF statement

@see: https://docs.python.org/3/tutorial/controlflow.html

There can be zero or more elif parts, and the else part is optional. The keyword ‘elif’ is
short for ‘else if’, and is useful to avoid excessive indentation.

An if … elif … elif … sequence is a substitute for the switch or case statements found
in other languages.
"""


def test_if_statement():
    """IF statement"""

    number = 15
    conclusion = ''
    description = ''

    if number < 0:
        conclusion = 'Negative number'
        description = 'The value is negative'
    elif number == 0:
        conclusion = 'Zero'
        description = 'The value is zero'
    elif number < 1:
        conclusion = 'Between zero and one'
        description = 'The value is between zero and one'
    else:
        conclusion = 'Positive number greater than or equal to one'
        description = 'The value is at least one'

    assert conclusion == 'Positive number greater than or equal to one'
    assert description == 'The value is at least one'

def test_nested_if_statement():
    """Test nested conditional statements."""

    number = 15
    conclusion = ''

    if number > 0:
        if number % 2 == 0:
            conclusion = 'Positive even number'
        else:
            conclusion = 'Positive odd number'
    else:
        conclusion = 'Zero or negative number'

    assert conclusion == 'Positive odd number'


def test_multiple_elif_statement():
    """Test multiple elif branches."""

    score = 85
    grade = ''

    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'

    assert grade == 'B'