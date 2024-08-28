from behave import given, when, then
import requests

@given('the API endpoint "{url}"')
def step_impl(context, url):
    context.url = url

@when('I send a GET request')
def step_impl(context):
    context.response = requests.get(context.url)

@then('the response status code should be {status_code}')
def step_impl(context, status_code):
    assert context.response.status_code == int(status_code)

@then('the response body should contain "{value}"')
def step_impl(context, value):
    assert value in context.response.text
