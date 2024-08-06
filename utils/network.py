from stere.browser_spy import FetchSpy, XHRSpy


class BrowserInteractionSpies:
    def __init__(self, action_function, activity_wait_time=120):
        self.fetch_spy = FetchSpy()
        self.xhr_spy = XHRSpy()
        self.action_function = action_function
        self.activity_wait_time = activity_wait_time

    def spy_action(self, wait_for_no_activity_before=False):
        self.fetch_spy.add()
        self.xhr_spy.add()
        if wait_for_no_activity_before:
            self.fetch_spy.wait_for_no_activity(self.activity_wait_time)
            self.xhr_spy.wait_for_no_activity(self.activity_wait_time)
        self.action_function()
        self.fetch_spy.wait_for_no_activity(self.activity_wait_time)
        self.xhr_spy.wait_for_no_activity(self.activity_wait_time)

    def continue_waiting(self):
        self.fetch_spy.wait_for_no_activity(self.activity_wait_time)
        self.xhr_spy.wait_for_no_activity(self.activity_wait_time)

