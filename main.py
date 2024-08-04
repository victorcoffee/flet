import flet as ft
import requests


def main(page: ft.Page):
    page.title = "Погода"
    page.theme_mode = "light"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    label = ft.Text("Місто")
    city_name = ft.TextField(label="Введіть місто", width=300)
    weather_data = ft.Text("")

    def get_info(e):
        if len(city_name.value) < 2:
            return

        API_key = "6b9c4a211a6332966918303ab81f14c2"
        URL = f"https://api.openweathermap.org/data/2.5/weather?q={city_name.value}&appid={API_key}&units=metric"
        res = requests.get(URL).json()
        temp = res["main"]["temp"]
        weather_data.value = f"Температура {temp: .0f}°С"
        page.update()

    def change_theme(e):
        page.theme_mode = "light" if page.theme_mode == "dark" else "dark"
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.SUNNY, on_click=change_theme),
                ft.Text("Погода"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [city_name],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [weather_data],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [ft.ElevatedButton(text="Отримати", on_click=get_info)],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )


ft.app(target=main)

# Щоб створити вебдодаток:
# ft.app(target=main, view=ft.AppView.WEB_BROWSER)
