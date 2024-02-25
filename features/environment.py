from environments.core_environment import *


def before_all(context):
    core_before_all(context)


def before_feature(context, feature):
    core_before_feature(context, feature)


def before_scenario(context, scenario):
    core_before_scenario(context, scenario)


def after_feature(context, feature):
    core_after_feature(context, feature)


def after_scenario(context, scenario):
    core_after_scenario(context, scenario)
