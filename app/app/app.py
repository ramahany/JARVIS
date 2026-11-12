"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from app.components import crystalized_ball



ball = rx.center(
        crystalized_ball(
            preset="plasma",
            color="#F25BD0",
            width="100%",
            height="600px",
        ),
        width="100%",
        height="80vh",
    )

page = rx.grid(
    rx.box(bg=rx.color("accent", 3)),
    rx.box(ball),
    rx.box(bg=rx.color("accent", 3)),
    columns="20% 60% 20%",
    width="100%",
    height="100vh",
    gap="0px",
)
def index():
    return page

app = rx.App()
app.add_page(index)
