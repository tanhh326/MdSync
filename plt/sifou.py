from DrissionPage.common import Keys
from DrissionPage import ChromiumPage
from common import MdFile, publish_interceptor


@publish_interceptor(plt='思否')
def publish(md_file: MdFile):
    page = ChromiumPage()
    tab = page.new_tab('https://segmentfault.com/write')
    title_input = tab('x://*[@id="title"]')
    title_input.input(md_file.name)
    content_div = tab(
        'x://*[@id="__next"]/div[3]/div[2]/div/div/div/div[1]/div[2]/div[1]/div[3]/div/div/div[1]/textarea')
    content_div.click()
    content_div.input(Keys.CTRL_V)
