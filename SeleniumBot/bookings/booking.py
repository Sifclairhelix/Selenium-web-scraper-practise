import os
import bookings.constant as CONST
from selenium import webdriver

class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:/SeleniumDrivers", teardown=False):
        self.driver_path=driver_path
        self.teardown = teardown
        os.environ['PATH'] += r"C:/SeleniumDrivers"
        #super was to instiate not 100% sure yet
        super(Booking, self).__init__()
        self.implicitly_wait(30)
        self.maximize_window()
        
    def __exit__(self, *args) -> None:
        if self.teardown:
            self.quit()
    
    def land_first_page(self):
        self.get(CONST.BASE_URL)
        
    def change_cur(self, currency=None):
        currency_but = self.find_element_by_css_selector(
            'button[data-tooltip-text="Choose your currency"]'
        )
        currency_but.click()
        selc_cur_element = self.find_element_by_css_selector(
            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
        )
        selc_cur_element.click()
        
        
    def initial_place(self, choose_loc):
        intial_search = self.find_element_by_id("ss")
        intial_search.clear()
        intial_search.send_keys(choose_loc)
        
        result_1 = self.find_element_by_css_selector(
            'li[data-i="0"]'
        )
        result_1.click()
    
    def select_date(self, check_in, check_out):
        chec_in_el = self.find_element_by_css_selector(
            f'td[data-date="{check_in}"]'
        )
        chec_in_el.click()
        
        chec_out_el = self.find_element_by_css_selector(
            f'td[data-date="{check_out}"]'
        )
        chec_out_el.click()