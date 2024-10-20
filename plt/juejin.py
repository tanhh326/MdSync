from DrissionPage.common import Keys
from DrissionPage import ChromiumPage
from common import MdFile, publish_interceptor


@publish_interceptor(plt='掘金')
def publish(md_file: MdFile):
    page = ChromiumPage()
    tab = page.new_tab('https://juejin.cn/editor/drafts/new?v=2')
    title_input = tab('x://*[@id="juejin-web-editor"]/div[2]/div/header/input')
    title_input.input(md_file.name)
    content_div = tab('x://*[@id="juejin-web-editor"]/div[2]/div/div[1]/div')
    # 粘贴进去自动转换
    content_div.input(Keys.CTRL_V)
