

class CommonFunctions(object):
    @staticmethod
    def search(cls, term):
        cls.search_box.wait_element()
        cls.search_box.set_text(term)
        cls.search_button.click()
