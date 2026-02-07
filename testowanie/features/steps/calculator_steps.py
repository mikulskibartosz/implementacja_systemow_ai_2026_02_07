from behave import given, when, then
import numpy as np

class Calculator:
    def add(self, a, b):
        return a + b


    def subtract(self, a, b):
        return a - b


@given(u'I have a calculator')
def step_impl(context):
    context.calculator = Calculator()


@when(u'I add {a:d} and {b:d}')
def step_impl(context, a, b):
    context.result = context.calculator.add(a, b)

@when(u'I subtract {b:d} from {a:d}')
def step_impl(context, a, b):
    context.result = context.calculator.subtract(a, b)

@when(u'I perform the following additions')
def step_impl(context):
    context.results = []
    for row in context.table:
        a = int(row['a'])
        b = int(row['b'])
        expected = int(row['result'])
        result = context.calculator.add(a, b)
        context.results.append(result == expected)



@then(u'the result should be {expected:d}')
def step_impl(context, expected):
    assert context.result == expected

@then(u'the result should be greater than 0')
def step_impl(context):
    assert context.result > 0

@then(u'all results should be correct')
def step_impl(context):
    assert np.all(context.results)