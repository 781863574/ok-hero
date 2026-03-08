import re
from ok import TriggerTask

class guaji(TriggerTask):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "挂机"
        self.description = "挂机"
        self.trigger_count = 0

    def run(self):
        # self.trigger_count += 1
        # self.log_debug(f'MyTriggerTask run {self.trigger_count}')
        if(self.ocr(0.47, 0.07, 0.53, 0.12, match=re.compile('85..'))):
            self.click_relative(0.50, 0.96)
            self.sleep(1.5)
            self.click_relative(0.50, 0.78)
            self.sleep(1.5)
            self.click_relative(0.55, 0.81)
            self.sleep(1.5)
            self.click_relative(0.55, 0.56)
            self.sleep(1.5)




