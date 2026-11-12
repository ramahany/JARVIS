import reflex as rx

jsx_path = rx.asset(
    "./crystalized_ball.jsx",
    shared=True
)

css_path = rx.asset(
    "./crystalized_ball.css",
    shared=True
)


class CrystalBall(rx.Component):

    library = f"$/public{jsx_path}"
    tag = "CrystalizedBall"

    def add_imports(self):
        return {
            "": f"$/public/{css_path}"
        }


crystalized_ball = CrystalBall.create