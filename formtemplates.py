from flet import *

class FormContainer(UserControl):
    def __init__(self):
        # self.func = func
        super().__init__()
    
    def build(self):
        return Container(
                TextField(
                    height=70, 
                    width=400, 
                    bgcolor="#419873",
                    border_radius=10,
                    color='white',
                    border_color= 'white',
                    label= 'Add Task',
                ),
        )

class Createtask(UserControl):
    def __init__(self):
        super().__init__()
        
    def build(self):
        return Container(
            height=50,
            width=400,
            bgcolor='#317256',
            border_radius=25,
            padding=10,
            content= Row(
                alignment=CrossAxisAlignment.SPACE_BETWEEN,
                controls=[
                    Column(
                        spacing=1,
                        alignment = MainAxisAlignment.CENTER,
                        controls = [
                            Text(value=self.task)
                        ]
                    ),
                ]
            )
        )