from environments.core_environment import *
import utils.database_manager as db_manager
from utils.behave_m2_env import verify_env, copy_and_modify_env_db_data, reset_env_db_data
from utils.docker_env import docker_bin_magento


def before_all(context):
    context.keep_test_db = bool(context.config.userdata.get('keep-test-db'))
    verify_env()
    core_before_all(context)
    db_manager.tear_up(context)
    copy_and_modify_env_db_data(context)
    docker_bin_magento('cache:flush')
    use_fixture(warden_maria_db_connect, context)


def before_feature(context, feature):
    core_before_feature(context, feature)


def before_scenario(context, scenario):
    core_before_scenario(context, scenario)


def after_feature(context, feature):
    core_after_feature(context, feature)


def after_scenario(context, scenario):
    core_after_scenario(context, scenario)


def after_all(context):
    db_manager.tear_down(context)
    reset_env_db_data(context)
