from qfluentwidgets import FluentIcon

from ok import BaseTask


class tools(BaseTask):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "杂项"
        self.description = "杂项任务"
        self.icon = FluentIcon.SYNC
        self.default_config.update({
            '自动工具': "自动装备",
            '是否选项默认支持': False,
            'int选项': 1,
            '文字框选项': "默认文字",
            '长文字框选项': "默认文字默认文字默认文字默认文字默认文字默认文字默认文字默认文字默认文字默认文字默认文字默认文字默认文字默认文字默认文字默认文字默认文字默认文字默认文字",
            'list选项': ['第一', '第二', '第3'],
        })
        self.config_type["自动工具"] = {'type': "drop_down",
                                      'options': ['自动装备', '自动BOSS']}

    def run(self):
        self.sleep(1)
        if self.config['自动工具'] == '自动装备':
            self.auto_equip()
        elif self.config['自动工具'] == '自动BOSS':
            self.auto_boss()
        self.sleep(1)

    def auto_equip(self):
        for i in range(125):
            self.click_relative(0.62, 0.27)
            self.sleep(0.2)
            while (self.find_one('auto_equip')):
                self.click_relative(0.63, 0.51)
                self.sleep(0.1)
    
    def auto_boss(self):
        for i in range(120):
            self.click_relative(0.63, 0.36)
            self.sleep(0.5)
            self.click_relative(0.58, 0.77)
            self.sleep(5)
            self.wait_feature('home')
            self.sleep(1)



