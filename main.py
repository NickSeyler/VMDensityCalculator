from tkinter import Tk, Frame, BOTH

from Interface.frames import FrameCollection
from Interface.lables import LabelCollection
from Interface.text_lines import TextLineCollection
from Interface.radios import RadioCollection
from Interface.buttons import ButtonCollection


class Window(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.frame_collection = FrameCollection(self)
        self.label_collection = LabelCollection(self.frame_collection.get_frames())
        self.text_line_collection = TextLineCollection(self.frame_collection.get_frames())
        self.radio_collection = RadioCollection(self.frame_collection.get_frames())
        self.button_collection = ButtonCollection(self.frame_collection.get_frames(), self.label_collection,
                                                  self.text_line_collection, self.radio_collection)
        self.set_interface()

    def set_interface(self):
        self.frame_collection.init_frames()
        self.label_collection.init_labels()
        self.text_line_collection.init_text_lines()
        self.radio_collection.init_radios()
        self.button_collection.init_buttons()
        self.pack(fill=BOTH, expand=1)
        self.configure(bg='#202020')


def main():
    root = Tk()
    root.geometry("1280x600+20+20")
    root.title("VM Calculator")

    root.resizable(False, False)

    program = Window(root)

    root.mainloop()


if __name__ == "__main__":
    main()
