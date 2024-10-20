from common import MdFile, publish_interceptor
from DrissionPage import ChromiumPage


@publish_interceptor(plt='知乎')
def publish(md_file: MdFile):
    page = ChromiumPage()
    tab = page.new_tab('https://zhuanlan.zhihu.com/write')
    title_textarea = tab('x://*[@id="root"]/div/main/div/div[2]/div[2]/div[1]/label/textarea')
    title_textarea.input(md_file.name)
    # 打开文档导入modal
    file_menu = tab('x://*[@id="root"]/div/main/div/div[2]/div[1]/div/div/div/div[2]/div/div')
    file_menu.click()
    tab.wait.eles_loaded('x://*[@id="Popover5-content"]/div/button[1]')
    upload_menu_item = tab('x://*[@id="Popover5-content"]/div/button[1]')
    upload_menu_item.click()
    # 点击上传，打开文件选择器
    tab.wait.eles_loaded('x:/html/body/div[6]/div/div/div/div[2]/div/div[1]/form/div/div')
    uploader_div = tab('x:/html/body/div[6]/div/div/div/div[2]/div/div[1]/form/div/div')
    uploader_div.click.to_upload(md_file.abs_path)
