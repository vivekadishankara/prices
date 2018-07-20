

class CommonFunctions(object):
    @staticmethod
    def search(cls, term):
        cls.search_box.wait_element()
        cls.search_box.set_text(term)
        cls.search_button.click()
        cls.results_page.results.wait_elements()
        return cls.results_page.results.find_elements()