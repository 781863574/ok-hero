import re
from sys import intern
from time import sleep

from qfluentwidgets import FluentIcon

from src.tasks.MyBaseTask import MyBaseTask


class washa(MyBaseTask):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "挖沙"
        self.description = "挖沙"
        self.icon = FluentIcon.SYNC
        self.default_config.update({
            '下拉菜单选项': "第一",
            '是否选项默认支持': False,
            'int选项': 1,
            '文字框选项': "默认文字",
            '长文字框选项': "默认文字默认文字默认文字默认文字默认文字默认文字默认文字默认文字默认文字默认文字默认文字默认文字默认文字默认文字默认文字默认文字默认文字默认文字默认文字",
            'list选项': ['第一', '第二', '第3'],
        })
        self.config_type["下拉菜单选项"] = {'type': "drop_down",
                                      'options': ['第一', '第二', '第3']}

    def run(self):
        self.log_info('日常任务开始运行!', notify=True)
        self.sleep(1)
        self.draw_boxes('washa_chuhuo')
        self.test_find_one_feature()
        while not (self.ocr(0.40,0.29,0.45,0.31,match='0/300')):
            self.wa3ci()
            self.genghuan()
        self.sleep(1)
        self.log_info('日常任务运行完成!', notify=True)


    def find_some_text_on_bottom_right(self):
        return self.ocr(box="bottom_right",match="商城", log=True) #指定box以提高ocr速度

    def find_some_text_with_relative_box(self):
        return self.ocr(0.5, 0.5, 1, 1, match=re.compile("招"), log=True) #指定box以提高ocr速度

    def run_for_5(self):
        self.operate(lambda: self.do_run_for_5())

    def do_run_for_5(self):
        self.do_send_key_down('w')
        self.sleep(0.1)
        self.do_mouse_down(key='right')
        self.sleep(0.1)
        self.do_mouse_up(key='right')
        self.sleep(5)
        self.do_send_key_up('w')

    def wa3ci(self):
        click1 = [0.57, 0.70]
        click2 = [0.44, 0.70]
        click3 = [0.50, 0.64]
        click = [click1, click2, click3]
        for i in click:
            if (self.find_one('washa_chuhuo')) or (self.find_one('washa_chudahuo')):
                break
            self.click_relative(i[0], i[1])
            self.sleep(1.5)

    def genghuan(self):
        self.sleep(0.1)
        if (self.find_one('washa_chuhuo')):
            self.click_relative(0.60, 0.24)
            self.sleep(0.1)
            self.click_relative(0.60, 0.24)
            self.sleep(0.1)
            self.click_relative(0.55, 0.56)
            self.sleep(1.5)
            self.click_relative(0.50, 0.78)
        elif (self.find_one('washa_chudahuo')):
            self.click_relative(0.45, 0.66)
            self.sleep(1.5)
            self.click_relative(0.50, 0.78)
        elif (self.find_one('washa_zhuye')):
            self.click_relative(0.60, 0.24)
            self.sleep(0.1)
            self.click_relative(0.55, 0.56)
            self.sleep(1.5)
            self.click_relative(0.50, 0.78)
        self.sleep(1.5)

    def test_find_one_feature(self):
        return self.find_one('washa_chuhuo')





