from behave import *
from utils import docker_env as denv


@given("I have flushed the magento cache")
def step_impl(context):
    denv.docker_bin_magento('ca:fl')
