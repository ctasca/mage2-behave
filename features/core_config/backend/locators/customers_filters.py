from typing import Dict

from features.core_config.strategies import STRATEGY_KEY, XPATH_STRATEGY, LOCATOR_KEY

CUSTOMERS_FROM_ID_INPUT_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//input[@name=\"entity_id[from]\"]"}
CUSTOMERS_TO_ID_INPUT_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//input[@name=\"entity_id[to]\"]"}
CUSTOMERS_CREATED_FROM_INPUT_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//input[@name=\"created_at[from]\"]"}
CUSTOMERS_CREATED_TO_INPUT_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//input[@name=\"created_at[to]\"]"}
CUSTOMERS_DOB_FROM_INPUT_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//input[@name=\"dob[from]\"]"}
CUSTOMERS_DOB_TO_INPUT_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//input[@name=\"dob[to]\"]"}
CUSTOMERS_EMAIL_INPUT_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "(//input[@name=\"email\"])[1]"}
CUSTOMERS_NAME_INPUT_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "(//input[@name=\"name\"])[1]"}
CUSTOMERS_TAX_VAT_INPUT_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//input[@name=\"taxvat\"]"}
CUSTOMERS_TELEPHONE_INPUT_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//input[@name=\"billing_telephone\"]"}
CUSTOMERS_POSTCODE_INPUT_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//input[@name=\"billing_postcode\"]"}
CUSTOMERS_REGION_INPUT_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//input[@name=\"billing_region\"]"}
CUSTOMERS_GROUP_SELECT_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "//(select[@name=\"group_id\"])[1]"}
CUSTOMERS_COUNTRY_SELECT_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "(//select[@name=\"billing_country_id\"])[1]"}
CUSTOMERS_WEBSITE_SELECT_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "(//select[@name=\"website_id\"])[1]"}
CUSTOMERS_GENDER_SELECT_FILTER_LOCATOR: Dict[str, str] = \
    {STRATEGY_KEY: XPATH_STRATEGY, LOCATOR_KEY: "(//select[@name=\"gender\"])[1]"}
