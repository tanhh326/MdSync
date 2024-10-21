from DrissionPage.common import Keys
from DrissionPage import ChromiumPage
from common import MdFile, publish_interceptor


# 设置->默认编辑器->Markdown编辑器
@publish_interceptor(plt='简书')
def publish(md_file: MdFile):
    page = ChromiumPage()
    tab = page.new_tab('https://www.jianshu.com/writer#')
    tab('x://*[@id="root"]/div/div[2]/div[1]/div/div/div/div[1]').click()
    tab.wait.eles_loaded('x://*[@id="root"]/div/div[2]/div[2]/div/div/div/div/input')
    title_input_xpath = 'x://*[@id="root"]/div/div[2]/div[2]/div/div/div/div/input'
    title_input = tab(title_input_xpath)
    # 新建文章后，这里会先删除原来的标题，再重新生成
    title_input.wait.deleted()
    tab.wait.eles_loaded(title_input_xpath, any_one=True)
    title_input = tab(title_input_xpath)
    title_input.click()
    title_input.input(md_file.name)
    content_ele = tab('x://*[@id="arthur-editor"]')
    content_ele.input(Keys.CTRL_V)
