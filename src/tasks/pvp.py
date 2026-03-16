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
        while not (self.find_one('pvp_wanbi')):
            self.pvp_complete()
        self.log_info('pvp完成', log=True)

    def pvp(self):
        first = int(self.ocr(0.40, 0.69, 0.43, 70)[0].name.replace(',','').replace('.',''))
        second = int(self.ocr(0.49, 0.69, 0.52, 70)[0].name.replace(',','').replace('.',''))
        third = int(self.ocr(0.58, 0.69, 0.61, 70)[0].name.replace(',','').replace('.',''))
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
        self.sleep(2)
        self.wait_click_ocr(0.48,0.86,0.51,0.88,match=re.compile('确认'))

    def pvp_un(self):
        self.click_relative(0.50, 0.86)
        self.sleep(1)

    def check_lv(self):
        lv = self.ocr(0.46,0.39,0.50,0.41)[0].name.replace(',','').replace('Lv.','').replace('？','0')
        return lv
 
    def pvp_complete(self):
        click1 = [0.41, 0.73]
        click2 = [0.50, 0.73]
        click3 = [0.59, 0.73]
        click = [click1, click2, click3]
        lv = []
        for i in click:
            self.click_relative(i[0], i[1])
            self.sleep(0.5)
            lv.append(self.check_lv())
            self.sleep(0.5)
            self.back()
            self.sleep(0.5)
        min_value = min(lv)
        min_index = lv.index(min_value)
        if min_index == 0:
            self.click_relative(0.41,0.86)
        elif min_index == 1:
            self.click_relative(0.50,0.86)
        elif min_index == 2:
            self.click_relative(0.59,0.86)
        # 同时等待胜利或失败特征，使用循环检查
        import time
        start_time = time.time()
        timeout = 30  # 30秒超时
        
        while time.time() - start_time < timeout:
            if self.find_one('pvp_shengli') or self.find_one('pvp_baibei'):
                break
            self.sleep(0.1)  # 每0.1秒检查一次
        
        if time.time() - start_time >= timeout:
            self.log_warning('等待胜利或失败特征超时', log=True)
        self.click_relative(0.50,0.86)
        self.sleep(0.5)

        

