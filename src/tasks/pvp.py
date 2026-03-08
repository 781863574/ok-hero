import re

from qfluentwidgets import FluentIcon

from src.tasks.MyBaseTask import MyBaseTask


class pvp(MyBaseTask):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "pvp"
        self.description = "pvp"
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
        while not (self.ocr(0.50,0.60,0.53,0.63,match='0/5')):
            self.pvp_un()

    def find_some_text_on_bottom_right(self):
        return self.ocr(box="bottom_right",match="商城", log=True) #指定box以提高ocr速度

    def find_some_text_with_relative_box(self):
        return self.ocr(0.5, 0.5, 1, 1, match=re.compile("招"), log=True) #指定box以提高ocr速度

    def test_find_one_feature(self):
        return self.find_one('box_battle_1')

    def test_find_feature_list(self):
        return self.find_feature('box_battle_1')

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

    def pvp(self):
        first = int(self.ocr(0.40, 0.70, 0.43, 71)[0].name.replace(',','').replace('.',''))
        second = int(self.ocr(0.49, 0.70, 0.52, 71)[0].name.replace(',','').replace('.',''))
        third = int(self.ocr(0.58, 0.70, 0.61, 71)[0].name.replace(',','').replace('.',''))
        pvp_list = [first, second, third]
        min_value = min(pvp_list)
        min_index = pvp_list.index(min_value)
        print(pvp_list)
        print(min_value)
        print(min_index)
        if min_index == 0:
            self.click_relative(0.41,0.86)
        elif min_index == 1:
            self.click_relative(0.50,0.86)
        elif min_index == 2:
            self.click_relative(0.59,0.86)
        self.wait_click_ocr(0.48,0.86,0.51,0.88,match=re.compile('确认'))

    def pvp_un(self):
        self.click_relative(0.50, 0.86)
        self.sleep(1)

