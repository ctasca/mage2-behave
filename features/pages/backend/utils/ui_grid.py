from stere.areas import Areas


def reset_all_active_filters(active_filters: Areas):
    """ Reset all active filters in a UI grid """
    for active_filter in active_filters:
        active_filter.remove_button.click()
