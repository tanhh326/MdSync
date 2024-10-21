from DrissionPage.common import Keys
from DrissionPage import ChromiumPage
from common import MdFile, publish_interceptor


@publish_interceptor(plt='csdn')
def publish(md_file: MdFile):
    page = ChromiumPage()
    tab = page.new_tab('https://editor.csdn.net/md')
    # 关闭模板选择弹窗
    cancel_check_template_btn = tab('x://*[@id="reset_inner"]/div/div[6]/div[4]/div[1]')
    if cancel_check_template_btn:
        cancel_check_template_btn.click()

    title_input = tab('x:/html/body/div[1]/div[1]/div[1]/div/div[2]/input')
    title_input.set.value('')
    title_input.input(md_file.name)

    content_ele = tab('x:/html/body/div[1]/div[1]/div[2]/div/div[2]/div[1]/div[2]/pre')
    content_ele.click()
    content_ele.input(Keys.CTRL_V)
