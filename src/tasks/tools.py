from qfluentwidgets import FluentIcon

from src.tasks.MyBaseTask import MyBaseTask


class tools(MyBaseTask):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "杂项"
        self.description = "杂项任务"
        self.icon = FluentIcon.SYNC
        self.default_config.update({
            '自动工具': "自动装备",
        })
        self.config_type["自动工具"] = {'type': "drop_down",
                                      'options': ['自动装备', '自动BOSS', '自动炼金', 'ocr测试']}

    def run(self):
        self.sleep(1)
        if self.config['自动工具'] == '自动装备':
            self.auto_equip()
        elif self.config['自动工具'] == '自动BOSS':
            self.auto_boss()
        elif self.config['自动工具'] == '自动炼金':
            self.auto_lianjin()
        elif self.config['自动工具'] == 'ocr测试':
            self.ocr_test()
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

    def auto_lianjin(self):
        for i in range(100):
            box1 = [0.60, 0.966, 0.63, 0.99]
            click1 = [0.61,0.95]
            self.loop_ocr_click(box1, '刷新', click1)
            self.sleep(0.5)
            self.click_relative(0.56, 0.60)
            self.sleep(0.5)
            self.click_relative(0.61, 0.56)
            self.sleep(0.5)
            self.click_relative(0.50, 0.96)
            self.sleep(0.5)
            self.wait_click_ocr(0.48, 0.89, 0.52, 0.924, match='确认')
            self.sleep(0.8)

    def ocr_test(self):
        box = [0.60, 0.966, 0.63, 0.99]
        ocr = self.ocr(box[0], box[1], box[2], box[3])
        str = ocr[0].name
        print(str)
        self.log_info('ocr识别信息: ' + str, notify=True)

