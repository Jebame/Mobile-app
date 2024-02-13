from flet import *
from custom_checkbox import CustomCheckBox

def main(page: Page):
    BG = "#041955"
    FWG = "#97b4ff"
    FG = "#3450a1"
    PINK = "#eb06ff"
    
    def shrink(e):
        page_2.controls[0].width = 120
        page_2.controls[0].scale = transform.Scale(
            0.8, alignment=alignment.center_right,
        )
        page_2.controls[0].border_radius=border_radius.only(
            topLeft=35,
            topRight=0,
            bottomLeft=35,
            bottomRight=0
        )
        page_2.update()
        
    def restore(e):
        page_2.controls[0].width = 400
        page_2.controls[0].scale = transform.Scale(
            1, alignment=alignment.center_right,
        )
        page_2.update()

    create_task_view = Container(
        content=Container(on_click=lambda _:page.go('/'),
            height=40, width=40, content=Text('x'),)
    )

    tasks = Column(
        height=400, scroll='auto',
        controls=[
            # Container()
        ]
    )
    for i in range(10):
        tasks.controls.append(
            Container(height=70, 
                      width=400, 
                      bgcolor=BG,
                      border_radius=25,
                      padding=padding.only(
                          left=20,top=20,
                      ),
                      content = CustomCheckBox(PINK, label = 'Create interesting content!',size=30,),
                      )
        )

    categories_card = Row(
        scroll='auto'
    )
    categories = ['Business', 'Family', 'Friends']
    for i, category in enumerate(categories):
        categories_card.controls.append(
            Container(
                bgcolor=BG, height=110, width=170, border_radius=20, padding=15, 
                content=Column(
                    controls=[
                        Text('40 Tasks'),
                        Text(category),
                        Container(
                            width=160,
                            height=5,
                            bgcolor= 'white12',
                            border_radius=20,
                            padding=padding.only(right=i*2),
                            content=Container(
                                bgcolor=PINK,
                            ),
                        )
                    ]
                )
            )
        )

    first_page_contents = Container(
        content=Column(
            controls=[
                Row(alignment = 'spaceBetween',
                    controls=[
                        Container(on_click=lambda e: shrink(e),
                            content=Icon(icons.MENU)),
                        Row(
                            controls=[
                                Icon(icons.SEARCH),
                                Icon(icons.NOTIFICATIONS_OUTLINED),
                            ]
                        )
                    ]
                ),
                
                Container(height=20),
                Text(
                    value= 'What\'s up, Jeb!'
                ),
                Text(
                    value= 'Categories'
                ),
                Container(
                    padding=padding.only(top=10, bottom=20,),
                    content = categories_card
                ),
                Text("TODAY'S TASKS"),
                Stack(
                    controls=[
                        tasks,
                        FloatingActionButton(
                            icon= icons.ADD, on_click=lambda _: page.go ('/create_task'),
                            right=20,
                            bottom=5
                        )
                    ]
                )
            ]
        )
    )

    page_1 = Container(
        width=400,
        height=850,
        bgcolor=BG,
        border_radius=35,
        padding=padding.only(left=50, top=60, right=200),   
        
        content=Column(
            controls=[
                Container(
                    content=Text('<'),
                    height=50, width=50,
                    padding=padding.only(top=13, left=13),
                    border=border.all(color='white', width=1),border_radius=25,
                    on_click=lambda e:restore(e),
                )
            ]
        )
    )
    page_2 = Row( alignment='end',
        controls= [
            Container(
                width=400,
                height=850,
                bgcolor=FG,
                animate = animation.Animation(600, AnimationCurve.BOUNCE_IN_OUT),
                animate_scale = animation.Animation(400, curve='decelerate'),
                border_radius= 35,
                padding= padding.only(
                    top=50, left=20, right=20, bottom=5
                ),
                content=Column(
                    controls=[
                        first_page_contents
                    ]
                )
            )
        ]
    )

    container = Container(
        width=500, height=850, bgcolor=BG , border_radius=35, content= Stack(
            controls= [
                page_1,
                page_2
            ]
        )
    )

    pages = {
        '/':View(
            "/",
            [
                container
            ]
        ),
        '/create_task': View(
            "/create_task",
            [
                create_task_view
            ]
        )
    }

    def route_change(route):
        page.views.clear()
        page.views.append(
            pages[page.route]
        )

    page.add(container)

    page.on_route_change = route_change
    page.go(page.route)

app(target=main)