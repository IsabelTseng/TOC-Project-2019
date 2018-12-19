from transitions.extensions import GraphMachine

from utils import send_text_message
from utils import send_image_url
from utils import send_button_message
from getDcard import getTop10Title
from getNews import getNews1


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    def is_going_to_state1(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go to state1'
        return False

    def is_going_to_help(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'help'
        return False

    def is_going_to_newRecord(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '開始記帳'
        return False

    def is_going_to_getPhoto(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '照片'
        return False

    def is_going_to_photo1(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '照片1'
        if event.get("postback"):
            text = event['postback']['payload']
            return text.lower() == '照片1'
        return False

    def is_going_to_photo2(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '照片2'
        if event.get("postback"):
            text = event['postback']['payload']
            return text.lower() == '照片2'
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
        responese = send_text_message(sender_id, "I'm entering state1")
        self.go_back()

    def on_exit_state1(self):
        print('Leaving state1')

    def on_enter_help(self, event):
        print("I'm entering help")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "輸入 \"news\" 查看新聞\n輸入 \"FSM\" 查看FSM圖")
        self.go_back()

    def on_exit_help(self):
        print('Leaving help')

    def on_enter_newRecord(self, event):
        print("I'm entering newRecord")

        sender_id = event['sender']['id']
        responese = send_image_url(sender_id, "https://upload.wikimedia.org/wikipedia/commons/f/f8/Dcard_Favicon_x520.png")
        # https://9.share.photo.xuite.net/wh_lydia/1960663/11444643/536779712_m.jpg
        self.go_back()

    def on_exit_newRecord(self):
        print('Leaving newRecord')

    def on_enter_getPhoto(self, event):
        print("I'm entering getPhoto")

        sender_id = event['sender']['id']
        buttons = [
                    {
                        "type":"postback",
                        "title":"照片1",
                        "payload":"照片1"
                    },
                    {
                        "type":"postback",
                        "title":"照片2",
                        "payload":"照片2"
                    }
                ]
        responese = send_button_message(sender_id, "選擇照片", buttons)
        self.go_back()

    def on_exit_getPhoto(self):
        print('Leaving getPhoto')

    def on_enter_photo1(self, event):
        print("I'm entering photo1")

        sender_id = event['sender']['id']
        responese = send_image_url(sender_id, "https://pic3.zhimg.com/80/v2-919c284f057ab0f7c6e9a3bb1f131c12_hd.jpg")
        self.go_back()

    def on_exit_photo1(self):
        print('Leaving photo1')

    def on_enter_photo2(self, event):
        print("I'm entering photo2")

        sender_id = event['sender']['id']
        responese = send_image_url(sender_id, "https://wx3.sinaimg.cn/large/006VNNAsly1fqsluxiz9mj30ku0bpqhj.jpg")
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