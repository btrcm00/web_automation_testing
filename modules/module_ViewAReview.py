import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class TestVisitareview():
    def setup_method(self, method):
        self.driver = webdriver.Chrome(self.driver_path)
        self.driver.get(self.web_url)
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def wait_for_window(self, timeout = 2):
        time.sleep(round(timeout / 1000))
        wh_now = self.driver.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()

    def test_bthreadG(self):
        self.driver.get(self.web_url)
        self.driver.execute_script("window.scrollTo(0,2003)")
        self.driver.find_element(By.CSS_SELECTOR, ".jsx-1560371842:nth-child(1) > .jsx-1560371842 > .thread-title").click()
        self.driver.find_element(By.CSS_SELECTOR, ".hidden-xs > .jsx-725335046 svg").click()
        self.driver.find_element(By.CSS_SELECTOR, ".burger > .jsx-3867722346:nth-child(2)").click()

    def test_bthreadU(self):
        self.driver.get(self.web_url)
        self.driver.set_window_size(976, 1040)
        self.driver.find_element(By.CSS_SELECTOR, ".first > .jsx-3501530503 > .jsx-3808261869 > .jsx-3808261869").click()
        self.driver.find_element(By.CSS_SELECTOR, ".hidden-xs > .jsx-725335046 svg").click()

    def test_rLoveG(self):
        self.driver.get(self.web_url)
        self.driver.set_window_size(974, 1047)
        self.driver.find_element(By.LINK_TEXT, "Thử soi da, mắt từ chế độ Chân Dung Studio trên iPhone 14 Pro").click()
        self.driver.find_element(By.CSS_SELECTOR, ".thread-like").click()
        self.driver.find_element(By.CSS_SELECTOR, ".jsx-171388687 > svg").click()

    def test_rLoveU(self):
        self.driver.get(self.web_url)
        self.driver.set_window_size(976, 1040)
        self.driver.find_element(By.LINK_TEXT, "Pod 2: Món phụ kiện đáng và nên mua nhất của anh em đang dùng đồng hồ Coros").click()
        self.driver.find_element(By.CSS_SELECTOR, ".jsx-2265512871 > .jsx-171388687 .reaction-text").click()

    def test_shareG(self):
        self.driver.get(self.web_url)
        self.driver.set_window_size(976, 1040)
        self.driver.find_element(By.LINK_TEXT, "Thử soi da, mắt từ chế độ Chân Dung Studio trên iPhone 14 Pro").click()
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.CSS_SELECTOR, ".thread-share-count").click()
        self.vars["win729"] = self.wait_for_window(2000)
        self.driver.switch_to.window(self.vars["win729"])
        self.driver.close()

    def test_shareU(self):
        self.driver.get("https://tinhte.vn/thread/pod-2-mon-phu-kien-dang-va-nen-mua-nhat-cua-anh-em-dang-dung-dong-ho-coros.3612617/?ta_from_block=home_featured_threads")
        self.driver.set_window_size(976, 1040)
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.CSS_SELECTOR, ".thread-share > .jsx-2265512871:nth-child(2)").click()
        self.vars["win1008"] = self.wait_for_window(2000)

    def test_shareULC(self):
        self.driver.get("https://tinhte.vn/thread/hau-world-cup-cac-cau-thu-va-hlv-deo-dong-ho-gi-toi-qatar.3612625/?ta_from_block=home_featured_threads")
        self.driver.set_window_size(976, 1040)
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.CSS_SELECTOR, ".thread-share > .jsx-2265512871:nth-child(2)").click()
        self.vars["win4901"] = self.wait_for_window(2000)
        self.vars["root"] = self.driver.current_window_handle
        self.driver.switch_to.window(self.vars["win4901"])
        self.driver.find_element(By.ID, "u_0_u_5x").click()
        self.driver.find_element(By.ID, "u_0_u_5x").send_keys("qưesadf")
        self.driver.find_element(By.ID, "u_0_26_bY").click()
        self.driver.close()
        self.driver.switch_to.window(self.vars["root"])
        self.driver.close()

    def test_shareUNC(self):
        self.driver.get(self.web_url)
        self.driver.set_window_size(976, 1040)
        self.driver.find_element(By.CSS_SELECTOR, ".jsx-2206250852:nth-child(1) > .jsx-2206250852 > .jsx-2206250852 > .jsx-2206250852 > .jsx-2206250852").click()
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.CSS_SELECTOR, ".thread-share > .jsx-2265512871:nth-child(2)").click()
        self.vars["win6350"] = self.wait_for_window(2000)
        self.vars["root"] = self.driver.current_window_handle
        self.driver.switch_to.window(self.vars["win6350"])
        self.driver.find_element(By.ID, "u_0_u_S8").send_keys("1")
        self.driver.find_element(By.ID, "u_0_27_3i").click()
        self.driver.close()
        self.driver.switch_to.window(self.vars["root"])
        self.driver.close()

    def test_subcribeG(self):
        self.driver.get(self.web_url)
        self.driver.set_window_size(976, 1040)
        self.driver.find_element(By.CSS_SELECTOR, ".jsx-3834913322:nth-child(1) > .jsx-3501530503 > .jsx-3501530503 > .jsx-3501530503 > .jsx-3501530503:nth-child(1) > .jsx-3501530503:nth-child(1)").click()
        self.driver.find_element(By.LINK_TEXT, "Thử soi da, mắt từ chế độ Chân Dung Studio trên iPhone 14 Pro").click()
        self.driver.find_element(By.CSS_SELECTOR, ".follow-button").click()
        self.driver.find_element(By.CSS_SELECTOR, ".follow-button").click()
        self.driver.find_element(By.CSS_SELECTOR, ".hidden-xs > .jsx-396757025 path").click()

    def test_subcribeU(self):
        self.driver.get(self.web_url)
        self.driver.set_window_size(976, 1040)
        element = self.driver.find_element(By.CSS_SELECTOR, ".jsx-1328309378:nth-child(4) .preview-mask")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.LINK_TEXT, "Thử soi da, mắt từ chế độ Chân Dung Studio trên iPhone 14 Pro").click()
        self.driver.execute_script("window.scrollTo(0,688)")
        self.driver.execute_script("window.scrollTo(0,3375)")
        self.driver.find_element(By.CSS_SELECTOR, ".hidden-xs > .jsx-396757025 svg").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".hidden-xs > .jsx-396757025 > .jsx-396757025")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.close()

    def test_uBthreadU(self):
        self.driver.get("https://tinhte.vn/thread/hau-world-cup-cac-cau-thu-va-hlv-deo-dong-ho-gi-toi-qatar.3612625/?ta_from_block=home_featured_threads")
        self.driver.set_window_size(976, 1040)
        self.driver.find_element(By.CSS_SELECTOR, ".jsx-2265512871:nth-child(1) > .jsx-725335046 g:nth-child(2) > path").click()
        
    def test_vPcom(self):
        self.driver.get(self.web_url)
        self.driver.set_window_size(1936, 1056)
        self.driver.find_element(By.CSS_SELECTOR, "#ontheroad .jsx-131847778:nth-child(2)").click()

    def test_vTasGH(self):
        self.driver.get(self.web_url)
        self.driver.set_window_size(974, 1040)
        self.driver.find_element(By.LINK_TEXT, "Mời tham gia bình chọn Điện thoại trong TTBC22, cơ hội nhận giải đặc biệt và combo quà 28 triệu").click()

    def test_vTasGI(self):
        self.driver.get(self.web_url)
        self.driver.set_window_size(976, 1040)
        element = self.driver.find_element(By.CSS_SELECTOR, ".jsx-934348644:nth-child(1) > .jsx-2238569880 .thread-title")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".jsx-934348644:nth-child(1) > .jsx-2238569880 .thread-title").click()

    def test_vTasUH(self):
        self.driver.get(self.web_url)
        self.driver.set_window_size(976, 1040)
        self.driver.find_element(By.LINK_TEXT, "Hậu World Cup: Các cầu thủ và HLV đeo đồng hồ gì tới Qatar?").click()

    def test_vTasUI(self):
        self.driver.get(self.web_url)
        self.driver.set_window_size(976, 1040)
        self.driver.find_element(By.CSS_SELECTOR, ".first > .jsx-3501530503 > .jsx-3808261869 > .jsx-3808261869").click()

    def test_vTauthor(self):
        self.driver.get(self.web_url)
        self.driver.set_window_size(974, 1040)
        self.driver.execute_script("window.scrollTo(0,2011)")
        self.driver.execute_script("window.scrollTo(0,2383)")
        self.driver.find_element(By.CSS_SELECTOR, ".jsx-934348644:nth-child(1) > .jsx-2238569880 > .jsx-2238569880 > .jsx-2238569880 > .jsx-2238569880 > .jsx-2238569880").click()
        self.driver.find_element(By.CSS_SELECTOR, ".jsx-934348644:nth-child(1) > .jsx-2238569880 .jsx-131847778:nth-child(2)").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".first-menu > .jsx-2166383770 > .jsx-2166383770 > .jsx-2166383770")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()

    def test_vads(self):
        self.driver.get(self.web_url)
        self.driver.set_window_size(976, 1040)
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.CSS_SELECTOR, ".jsx-306557543 > .jsx-306557543").click()
        self.vars["win2974"] = self.wait_for_window(2000)
        self.driver.switch_to.window(self.vars["win2974"])

    def test_vauthor(self):
        self.driver.get(self.web_url)
        self.driver.set_window_size(976, 1040)
        self.driver.execute_script("window.scrollTo(0,554)")
        self.driver.find_element(By.LINK_TEXT, "Pod 2: Món phụ kiện đáng và nên mua nhất của anh em đang dùng đồng hồ Coros").click()
        self.driver.find_element(By.LINK_TEXT, "Trần Hoàng Long.").click()

    if __name__ == "__main__":
        PATH = "chromedriver/chromedriver.exe"
        WEB_URL = "https://tinhte.vn/"
        suite = unittest.TestSuite()
        suite.addTest(TestProfileSuite(testcase_name="changeAvatar", driver_path=PATH, web_url=WEB_URL))
        unittest.TextTestRunner().run(suite)