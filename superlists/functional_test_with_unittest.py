from selenium import webdriver
import unittest

# browser = webdriver.Firefox();

#刘枣听说有一个很酷的在线待办事项应用
#他去看了这个网站首页
# browser.get("http://localhost:8000");

#他注意到网页的标题和头部都包含"To-Do"这个词
# assert "To-Do" in browser.title
#
# browser.quit();

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox();

    def tearDown(self):
        self.browser.quit();

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 刘枣听说有一个很酷的在线待办事项应用
        # 他去看了这个网站首页
        self.browser.get("http://localhost:8000")

        # 他注意到网页的标题和头部都包含"To-Do"这个词
        self.assertIn("To-Do",self.browser.title)

        self.fail('Finish the test!')


if __name__ == "__main__":
    # unittest.main(warnings="ignore");
    pass