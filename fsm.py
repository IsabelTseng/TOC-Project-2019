from transitions.extensions import GraphMachine

from utils import send_text_message
from utils import send_image_url
from utils import send_button_message
from getDcard import getTop10Title
from getNews import getNews1
import random


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    def is_going_to_state1(self, event):
        # if event.get("message"):
        #     text = event['message']['text']
        #     return text.lower() == 'go to state1'
        # return False
        return True

    def is_going_to_help(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'help'
        return False

    def is_going_to_fsm(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'fsm'
        return False

    # def is_going_to_newRecord(self, event):
    #     if event.get("message"):
    #         text = event['message']['text']
    #         return text.lower() == '開始記帳'
    #     return False

    def is_going_to_getPhoto(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '照片'
        return False

    def is_going_to_photo1(self, event):
        # if event.get("message"):
        #     text = event['message']['text']
        #     return text.lower() == '羽生結弦'
        if event.get("postback"):
            text = event['postback']['payload']
            return text.lower() == '羽生結弦'
        return False

    def is_going_to_photo2(self, event):
        # if event.get("message"):
        #     text = event['message']['text']
        #     return text.lower() == '新垣结衣'
        if event.get("postback"):
            text = event['postback']['payload']
            return text.lower() == '新垣结衣'
        return False

    def is_going_to_getNews(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'news'
        if event.get("postback"):
            text = event['postback']['payload']
            return text.lower() == '返回'
        return False

    def is_going_to_dcardPhoto(self, event):
        if event.get("postback"):
            text = event['postback']['payload']
            return text.lower() == 'dcard'
        return False

    def is_going_to_dcardTitle(self, event):
        if event.get("postback"):
            text = event['postback']['payload']
            return text.lower() == '確認'
        return False

    def is_going_to_news1Photo(self, event):
        if event.get("postback"):
            text = event['postback']['payload']
            return text.lower() == '民報'
        return False

    def is_going_to_news1Title(self, event):
        if event.get("postback"):
            text = event['postback']['payload']
            return text.lower() == '確認'
        return False

    def on_enter_state1(self, event):
        print("I'm entering state1")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "Hello")
        self.go_back()

    def on_exit_state1(self):
        print('Leaving state1')

    def on_enter_help(self, event):
        print("I'm entering help")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "輸入 \"news\" 查看新聞\n輸入 \"FSM\" 查看FSM圖\n輸入 \"照片\" 查看隨機照片")
        # self.go_back()

    def on_exit_help(self, event):
        print('Leaving help')

    def on_enter_fsm(self, event):
        print("I'm entering fsm")

        sender_id = event['sender']['id']
        responese = send_image_url(sender_id, "https://raw.githubusercontent.com/IsabelTseng/TOC-Project-2019/master/fsm.png")
        self.go_back()

    def on_exit_fsm(self):
        print('Leaving fsm')

    # def on_enter_newRecord(self, event):
    #     print("I'm entering newRecord")

    #     sender_id = event['sender']['id']
    #     responese = send_image_url(sender_id, "https://upload.wikimedia.org/wikipedia/commons/f/f8/Dcard_Favicon_x520.png")
    #     # https://9.share.photo.xuite.net/wh_lydia/1960663/11444643/536779712_m.jpg
    #     self.go_back()

    # def on_exit_newRecord(self):
    #     print('Leaving newRecord')

    def on_enter_getPhoto(self, event):
        print("I'm entering getPhoto")

        sender_id = event['sender']['id']
        buttons = [
                    {
                        "type":"postback",
                        "title":"羽生結弦",
                        "payload":"羽生結弦"
                    },
                    {
                        "type":"postback",
                        "title":"新垣结衣",
                        "payload":"新垣结衣"
                    }
                ]
        responese = send_button_message(sender_id, "選擇照片", buttons)

    def on_exit_getPhoto(self, event):
        print('Leaving getPhoto')

    def on_enter_photo1(self, event):
        print("I'm entering photo1")

        photos = [
            "https://i1.kknews.cc/SIG=3bj0v8q/66n8000510n6r19ps0so.jpg",
            "http://cms.exmoo.com/uploads/HNh4MndPk1x1p8Jrb7HF.jpg",
            "https://i1.read01.com/SIG=26tgnje/30384573386a3033.jpg"
        ]
        sender_id = event['sender']['id']
        responese = send_image_url(sender_id, photos[random.randint(0,len(photos)-1)])
        self.go_back()

    def on_exit_photo1(self):
        print('Leaving photo1')

    def on_enter_photo2(self, event):
        print("I'm entering photo2")

        photos = [
            "https://pic2.zhimg.com/80/v2-7c1f928a45d6aef403e8b9f9361eca0e_qhd.jpg",
            "https://wx2.sinaimg.cn/wap720/70396e5agy1fguxpp35rhj20zl0ku779.jpg",
            "http://n.sinaimg.cn/transform/20150319/N4Ne-chmifpy0845535.jpg"
        ]
        sender_id = event['sender']['id']
        responese = send_image_url(sender_id, photos[random.randint(0,len(photos)-1)])
        self.go_back()

    def on_exit_photo2(self):
        print('Leaving photo2')

    def on_enter_getNews(self, event):
        print("I'm entering getNews")

        sender_id = event['sender']['id']
        buttons = [
                    {
                        "type":"postback",
                        "title":"Dcard",
                        "payload":"Dcard"
                    },
                    {
                        "type":"postback",
                        "title":"民報",
                        "payload":"民報"
                    }
                ]
        responese = send_button_message(sender_id, "選擇網站", buttons)
        # self.go_back()

    def on_exit_getNews(self, event):
        print('Leaving getNews')

    def on_enter_dcardPhoto(self, event):
        print("I'm entering dcardPhoto")

        sender_id = event['sender']['id']
        responese = send_image_url(sender_id, "https://upload.wikimedia.org/wikipedia/commons/f/f8/Dcard_Favicon_x520.png")
        buttons = [
                    {
                        "type":"postback",
                        "title":"確認",
                        "payload":"確認"
                    },
                    {
                        "type":"postback",
                        "title":"返回",
                        "payload":"返回"
                    }
                ]
        responese = send_button_message(sender_id, "查看Dcard熱門？", buttons)

    def on_exit_dcardPhoto(self, event):
        print('Leaving dcardPhoto')

    def on_enter_dcardTitle(self, event):
        print("I'm entering dcardTitle")

        sender_id = event['sender']['id']
        dcard10Title = getTop10Title(10)
        text = '\n'.join(dcard10Title)
        send_text_message(sender_id, text)
        self.go_back()

    def on_exit_dcardTitle(self):
        print('Leaving dcardTitle')

    def on_enter_news1Photo(self, event):
        print("I'm entering news1Photo")

        sender_id = event['sender']['id']
        responese = send_image_url(sender_id, "http://www.peoplenews.tw/images/logo_full.png")
        buttons = [
                    {
                        "type":"postback",
                        "title":"確認",
                        "payload":"確認"
                    },
                    {
                        "type":"postback",
                        "title":"返回",
                        "payload":"返回"
                    }
                ]
        responese = send_button_message(sender_id, "查看民報即時新聞？", buttons)

    def on_exit_news1Photo(self, event):
        print('Leaving news1Photo')

    def on_enter_news1Title(self, event):
        print("I'm entering news1Title")

        sender_id = event['sender']['id']
        news = getNews1()
        text = '\n'.join(news)
        send_text_message(sender_id, text)
        self.go_back()

    def on_exit_news1Title(self):
        print('Leaving news1Title')