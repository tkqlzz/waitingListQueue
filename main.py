from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.properties import NumericProperty

from customer import Customer
from queue import Queue

queue = Queue()


class InputPopup(Popup):
    def on_press_OK(self, *args): #예약접수 완료
        c = Customer(args[0], args[1])
        queue.enqueue(c)
        self.dismiss()

    def on_press_Cancel(self, *args): #취소
        self.dismiss()


class MyWidget(Widget):
    number = NumericProperty(queue.length)
    
    def show_input(self): #예약접수 팝업
        popup = InputPopup();
        popup.bind(on_dismiss=self.my_callback)
        popup.open()

    def delete_reservation(self): #자리 배치
        queue.dequeue()
        self.number = queue.length

    def my_callback(self, popup): #예약인원 refresh
        self.number = queue.length


class MyApp(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    MyApp().run()
