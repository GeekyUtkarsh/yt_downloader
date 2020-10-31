from kivy.uix.behaviors import button
from self2 import MyGrid
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.label import Label


class MyGrid(GridLayout):
    def __init__(self, **kwargs):               
        super().__init__(**kwargs)
        super(MyGrid, self).__init__(**kwargs)

        self.cols = 1 #columns

        self.inside = GridLayout() #layout nesting

        self.inside.cols = 3

        self.add_widget(Label(text = "YT Video Downloader!", font_size = 20))
        self.video_link = TextInput(font_size = 16, hint_text = "Paste your yt link here")
        self.add_widget(self.video_link)

        self.inside.add_widget(Label(text = ""))

        self.butt = (Button(text = "Download", font_size = 14))
        self.inside.add_widget(self.butt)
        self.butt.bind(on_press = self.download)
        self.inside.add_widget(Label(text = ""))

        self.add_widget(self.inside)

    def download(self, instance):
        import pafy
        import urllib.request
        video = self.video_link.text
        video_down = None
        def connect(host = 'https://www.google.com'):
            try:
                urllib.request.urlopen(host) #to check the internet
                return True
            except:
                return False 
        if connect() == True: #if net is available downloading starts
            try:
                video_down = pafy.new(video) #getting the link
            except:
                box = BoxLayout()
                box.add_widget(Label(text = "No Video Found!", font_size = 10))
                pop = Popup(
                    content = box, title="Error",auto_dismiss = False, size_hint=[None, None], size=[200, 200])
                pop.open()
                box.on_touch_down = pop.dismiss
            best = video_down.getbest(preftype = "mp4") #to get best quality video
            best.download()

            box = BoxLayout()
            box.add_widget(Label(text = "Video Downloaded Successfuly!", font_size = 10))
            pop = Popup(
                content = box, title="Done",auto_dismiss = False, size_hint=[None, None], size=[200, 200])
            pop.open()
            box.on_touch_down = pop.dismiss

        else:
            box = BoxLayout()
            box.add_widget(Label(text = "No Internet Connectivity Found!", font_size = 10))
            pop = Popup(
                content = box, title="Error",auto_dismiss = False, size_hint=[None, None], size=[200, 200])
            pop.open()
            box.on_touch_down = pop.dismiss



class MyApp(App):
    def build(self):
        self.title = "YT Video Downloader"
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()