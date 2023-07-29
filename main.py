from flet import Page, Column, FilledButton, Text, TextThemeStyle, Row, Dropdown,SnackBar , app
from flet import dropdown as dropdownElement
from random import randint
DEFAULT_FLET_PORT = 8014
data = {
    "Первое" :      ["1", "2", "3"],
    "Второе" :      [],
    "Гарниры" :     [],
    "Закуски" :     [],
    "Салаты" :      [],
    "Еще что-то" :  [],
    "Десерты" :     [],
}
def main(page: Page):
    
    def _bootstrap():
        _elements = []
        for creator in data.keys():
            _elements.append(dropdownElement.Option(creator))
        return _elements

    list_of_last = Column(
        controls=[Text(size=20), Text(size=20), Text(size=20)],
    )
    dropdown_get_type_of_food = Dropdown(
        options=_bootstrap(),
        width=400
    )

    def get(e):
        if dropdown_get_type_of_food.value in ["", None]:
            SnackBar(content=Text("Выберите пункт из выпадающего списка")).open = True
            return
        food = data[dropdown_get_type_of_food.value][randint(0, len(data[dropdown_get_type_of_food.value]) - 1)]

        if len(list_of_last.controls) >= 3:
                list_of_last.controls[2] = list_of_last.controls[1] 
                list_of_last.controls[1] = list_of_last.controls[0]
                list_of_last.controls[0] = Text(food, size=20) 
        else:
            list_of_last.controls.append(Text(food, size=20))
        page.update()
    
    page.title = "Что готовить?"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"  
    text            = Text("Что готовить?", style = TextThemeStyle.DISPLAY_MEDIUM) 
    who_cook_button = FilledButton(text="Предложи", on_click=get, height=60)
    

    page.add(
        Column(
            controls=[
                Row(controls = [text], alignment="center"),
                Row(controls = [dropdown_get_type_of_food], alignment="center"),
                Row(controls=[who_cook_button], alignment= "center" ),
                Row(controls=[list_of_last], alignment="center")                # TODO
            ],
            spacing=50    
        )
    )

app(target=main, port=DEFAULT_FLET_PORT)
