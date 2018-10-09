import pandas
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.label import Label
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.button import Button
from kivy.properties import BooleanProperty, ListProperty, ObjectProperty
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.core.window import Window
from kivy.lang import Builder

Builder.load_string("""
#:kivy 1.10.0

<SelectableButton>:
    # Draw a background to indicate selection
    canvas.before:
        Color:
            rgba: (0, 0.517, 0.705, 1) if self.selected else (0, 0.517, 0.705, 1)
        Rectangle:
            pos: self.pos
            size: self.size
    background_color: [1, 0, 0, 1]  if self.selected else [1, 1, 1, 1]  # dark red else dark grey
    on_release: app.root.delete_row(self)

<QuestionDb>:
    column_headings: column_headings
    orientation: "vertical"

    Label:
        canvas.before:
            Color:
                rgba: (0, 0, 1, .5)     # 50% translucent blue
            Rectangle:
                pos: self.pos
                size: self.size
        text: 'Click on any row to delete'
        size_hint: 1, 0.1

    GridLayout:
        canvas.before:
            Color:
                rgba: (1, 0.2, 0, .5)     # 50% translucent orange red
            Rectangle:
                pos: self.pos
                size: self.size

        id: column_headings
        size_hint: 1, None
        size_hint_y: None
        height: 25
        cols: 3

    BoxLayout:
        canvas.before:
            Color:
                rgba: (.0, 0.9, .1, .3)
            Rectangle:
                pos: self.pos
                size: self.size

        RecycleView:
            viewclass: 'SelectableButton'
            data: root.rv_data
            SelectableRecycleGridLayout:
                cols: 3
                key_selection: 'selectable'
                default_size: None, dp(26)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                multiselect: True
                touch_multiselect: True""")

class SelectableRecycleGridLayout(FocusBehavior, LayoutSelectionBehavior,
                                  RecycleGridLayout):
    ''' Adds selection and focus behaviour to the view. '''


class SelectableButton(RecycleDataViewBehavior, Button):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableButton, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableButton, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected


class QuestionDb(BoxLayout):
    items_list = ObjectProperty(None)
    column_headings = ObjectProperty(None)
    rv_data = ListProperty([])

    def __init__(self, **kwargs):
        super(QuestionDb, self).__init__(**kwargs)
        self.get_dataframe()

    def get_dataframe(self):
        df = pandas.read_excel("items.xlsx")

        # Extract and create column headings
        for heading in df.columns:
            self.column_headings.add_widget(Label(text=heading))

        # Extract and create rows
        data = []
        for row in df.itertuples():
            for i in range(1, len(row)):
                data.append([row[i], row[0]])
        self.rv_data = [{'text': str(x[0]), 'Index': str(x[1]), 'selectable': True} for x in data]

    def delete_row(self, instance):
        # TODO
        print("delete_row:")
        print("Button: text={0}, index={1}".format(instance.text, instance.index))
        print(self.rv_data[instance.index])
        print("Pandas: Index={}".format(self.rv_data[instance.index]['Index']))


class QuestionApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)    # white background
        return QuestionDb()


if __name__ == "__main__":
    QuestionApp().run()
