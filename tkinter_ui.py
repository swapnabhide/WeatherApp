from tkinter import *
from tkinter import ttk

from app.get_weather_data import get_weather

class UI:
    def __init__(self):
        self.root = Tk()
        self.panedwindow = ttk.Panedwindow(self.root, orient = VERTICAL)
        self.panedwindow.pack(fill = BOTH, expand = True)

        self.input_frame = ttk.Frame(self.panedwindow, height=150, width=400, relief = RIDGE)
        self.label = ttk.Label(self.input_frame, text = 'City:').grid()
        self.city = ttk.Entry(self.input_frame)
        self.city.grid()
        self.button = ttk.Button(self.input_frame, text = 'Get Weather', command=self.get_weather).grid()

        self.output_frame = ttk.Frame(self.panedwindow, height=250, width=400, relief = RIDGE)

        self.current_temp_label = ttk.Label(self.output_frame, text = 'Current Temperature: ').grid()
        self.current_temp_text_label = ttk.Label(self.output_frame)
        self.current_temp_text_label.grid()

        self.feels_like_label = ttk.Label(self.output_frame, text = 'Feels like: ').grid()
        self.feels_like_text_label = ttk.Label(self.output_frame)
        self.feels_like_text_label.grid()

        self.max_temp_label = ttk.Label(self.output_frame, text = 'Max Temp today: ').grid()
        self.max_temp_text_label = ttk.Label(self.output_frame)
        self.max_temp_text_label.grid()

        self.min_temp_label = ttk.Label(self.output_frame, text = 'Min temp today: ').grid()
        self.min_temp_text_label = ttk.Label(self.output_frame)
        self.min_temp_text_label.grid()


        self.panedwindow.add(self.input_frame, weight=1)
        self.panedwindow.add(self.output_frame, weight=2)
        self.root.mainloop()


    def get_weather(self):
        city_entry = self.city.get()
        data = get_weather(city_entry)
        if data["cod"] != "404":
            self.current_temp_text_label.config(text=data["main"]['temp'])
            self.feels_like_text_label.config(text=data["main"]['feels_like'])
            self.max_temp_text_label.config(text=data["main"]['temp_max'])
            self.min_temp_text_label.config(text=data["main"]['temp_min'])
        else:
            print("wrong city")
    

if __name__ == "__main__":
    ui = UI()