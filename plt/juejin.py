from DrissionPage.common import Keys
from DrissionPage import ChromiumPage
from common import MdFile, publish_interceptor


@publish_interceptor(plt='掘金')
def publish(md_file: MdFile):
    page = ChromiumPage()
    tab = page.new_tab('https://juejin.cn/editor/drafts/new?v=2')
    title_input = tab('x://*[@id="juejin-web-editor"]/div[2]/div/header/input')
    title_input.input(md_file.name)

    content_ele = tab('x://*[@id="juejin-web-editor"]/div[2]/div/div/div/div[2]/div[1]/div/div[1]/textarea')
    content_ele.click()
    # 粘贴进去自动转换
    content_ele.input(Keys.CTRL_V)
