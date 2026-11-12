import reflex as rx

config = rx.Config(
    app_name="app",
    frontend_packages=["ogl@1.0.11"],
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
        rx.plugins.RadixThemesPlugin(),
    ]
)