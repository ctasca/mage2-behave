from environments.core_environment import *
import utils.database_manager as db_manager
from utils.behave_m2_env import verify_env, copy_and_modify_env_db_data, reset_env_db_data
from utils.docker_env import docker_bin_magento


def before_all(context):
    _environment_bootstrap(context)


def before_feature(context, feature):
    core_before_feature(context, feature)


def before_scenario(context, scenario):
    core_before_scenario(context, scenario)


def after_feature(context, feature):
    core_after_feature(context, feature)


def after_scenario(context, scenario):
    core_after_scenario(context, scenario)


def after_all(context):
    if not context.keep_test_db:
        db_manager.tear_down()
    reset_env_db_data()


def _environment_bootstrap(context):
    context.keep_test_db = True if bool(context.config.userdata.get('keep-test-db')) is True else False
    context.keep_cache = True if bool(context.config.userdata.get('keep-cache')) is True else False
    context.keep_last_db_dump = True if bool(context.config.userdata.get('keep-db-dump')) is True else False
    verify_env()
    core_before_all(context)
    db_manager.tear_up(context.keep_last_db_dump)
    copy_and_modify_env_db_data(context)
    if not context.keep_cache:
        docker_bin_magento('cache:flush')
    use_fixture(warden_maria_db_connect, context)
    context.take_screenshots = False
