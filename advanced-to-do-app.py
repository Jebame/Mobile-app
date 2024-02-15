from flet import *
from custom_checkbox import CustomCheckBox

def main(page: Page):
    BG = "#419873"
    FWG = "#317256"
    FG = "#398564"
    BtnsBars = "#52bf90"
    
    def route_change(route):
        page.views.clear()
        page.views.append(
            pages[page.route]
    )
    
    def shrink(e):
        page_2.controls[0].width = 120
        page_2.controls[0].scale = transform.Scale(
            0.8, alignment=alignment.center_right,
        )
        page_2.controls[0].border_radius=border_radius.only(
            top_left=35,
            top_right=0,
            bottom_left=35,
            bottom_right=0
        )
        page_2.update()
        
    def restore(e):
        page_2.controls[0].width = 400
        page_2.controls[0].scale = transform.Scale(
            1, alignment=alignment.center_right,
        )
        page_2.update()

    circle = Stack(
    controls=[
      Container(
        width=100,
        height=100,
        border_radius=50,
        bgcolor='white12'
        ),
      Container(
                  gradient=SweepGradient(
                      center=alignment.center,
                      start_angle=0.0,
                      end_angle=3,
                      stops=[0.5,0.5],
                  colors=['#00000000', BtnsBars],
                  ),
                  width=100,
                  height=100,
                  border_radius=50,
                  content=Row(alignment='center',
                      controls=[
                        Container(padding=padding.all(5),
                          bgcolor=BG,
                          width=90,height=90,
                          border_radius=50,
                          content=Container(bgcolor=FG,
                            height=80,width=80,
                            border_radius=40,
                          content=CircleAvatar(opacity=0.8,
                            foreground_image_url="https://images.unsplash.com/photo-1545912452-8aea7e25a3d3?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
                            )
                          )
                          )
                      ],
                  ),
              ),
      
        ]
    )
    
    create_task_view = Container(
        width=400,
        height=850,
        bgcolor=BG,
        animate = animation.Animation(600, AnimationCurve.EASE_IN_OUT_BACK),
        animate_scale = animation.Animation(400, curve='decelerate'),
        border_radius= 35,
        padding= padding.only(top=50, left=20, right=20, bottom=5),
        content=Column(
            controls=[
                Row(alignment = 'spaceBetween',
                    controls=[
                        Container(
                            content=Container(on_click=lambda _:page.go('/'),
                               height=50, width=50,
                    padding=padding.only(top=10, left=20),
                    border=border.all(color='white', width=1),border_radius=25, content=Text('x'),)
                        )
                    ]
                ),
                
                Container(height=20),
                TextField(
                    height=70, 
                    width=400, 
                    bgcolor=BG,
                    border_radius=10,
                    color='white',
                    border_color= 'white',
                    label= 'Add Task'
                ),
                TextField(
                    height=70, 
                    width=400, 
                    bgcolor=BG,
                    border_radius=10,
                    color='white',
                    border_color= 'white',
                    label= 'Add Category'
                ),
                TextField(
                    height=70, 
                    width=400, 
                    bgcolor=BG,
                    border_radius=10,
                    color='white',
                    border_color= 'white',
                    label= 'Add Shit Here!'
                ),
            ]
        )
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
                      bgcolor=FWG,
                      border_radius=25,
                      padding=padding.only(
                          left=20,top=20,
                      ),
                      content = CustomCheckBox(BtnsBars, label = 'Create interesting content!',size=30,),
                      )
        )

    categories_card = Row(
        scroll='auto'
    )
    categories = ['Business', 'Family', 'Friends']
    for i, category in enumerate(categories):
        categories_card.controls.append(
            Container(
                bgcolor=FWG, height=110, width=170, border_radius=20, padding=15, 
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
                                bgcolor=BtnsBars,
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
                    size=20,
                    weight='bold',
                    value= 'What\'s up, Monisa!'
                ),
                Text(
                    value= 'Categories'
                ),
                Container(
                    padding=padding.only(top=10, bottom=20,),
                    content = categories_card
                ),
                Text("Today's Task"),
                Stack(
                    controls=[
                        tasks,
                        FloatingActionButton(
                            icon= icons.ADD, on_click=lambda _: page.go ('/create_task'),
                            right=20,
                            bottom=5,
                            bgcolor=BG,
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
                Row(alignment='end',
                    controls=[
                        Container(
                    content=Text('<'),
                    height=50, width=50,
                    padding=padding.only(top=13, left=13),
                    border=border.all(color='white', width=1),border_radius=25,
                    on_click=lambda e:restore(e),
                        )
                 ]
                ),
                Container(height=20),
                circle,
                Text('Monisa\nQuino', size=32, weight='bold'),
                Container(height=20),
                Row(controls=[
                    Icon(icons.FAVORITE_BORDER_SHARP, color='white12'),
                    Text('Templates', size=15, weight=FontWeight.W_300, color='white', font_family='poppins')
                ]),
                Container(height=5),
                Row(controls=[
                    Icon(icons.CARD_TRAVEL, color='white12'),
                    Text('Templates', size=15, weight=FontWeight.W_300, color='white', font_family='poppins')
                ]),
                Container(height=5),
                Row(controls=[
                    Icon(icons.CALCULATE_OUTLINED, color='white12'),
                    Text('Templates', size=15, weight=FontWeight.W_300, color='white', font_family='poppins')
                ])
            ]
        )
    )
    page_2 = Row( alignment='end',
        controls= [
            Container(
                width=400,
                height=850,
                bgcolor=FG,
                animate = animation.Animation(600, AnimationCurve.EASE_IN_OUT_BACK),
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

    page.add(container)

    page.on_route_change = route_change
    page.go(page.route)

app(target=main)