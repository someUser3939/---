import flet as ft
from api import fetch_weather

def main_ui(page: ft.Page):
    # Настройки главного окна
    page.title = "Погода"
    page.window_width = 350
    page.window_height = 400
    page.window_resizable = False
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Элементы интерфейса
    city_input = ft.TextField(
        label="Введите город", 
        width=250, 
        text_align=ft.TextAlign.CENTER
    )
    
    result_text = ft.Text(
        value="Введите город и нажмите кнопку", 
        size=16, 
        text_align=ft.TextAlign.CENTER
    )

    # Функция, которая срабатывает при нажатии на кнопку
    def search_click(e):
        city = city_input.value.strip()
        if not city:
            result_text.value = "⚠️ Пожалуйста, введите город"
            page.update()
            return

        # Индикатор загрузки на время запроса
        result_text.value = "⌛ Загрузка..."
        page.update()

        weather = fetch_weather(city)

        if weather:
            result_text.value = (
                f"📍 {weather['city']}\n\n"
                f"🌡️ Температура: {weather['temp']}°C\n"
                f"☁️ Погода: {weather['desc']}\n"
                f"💧 Влажность: {weather['humidity']}%"
            )
        else:
            result_text.value = "❌ Город не найден или нет сети"
        
        page.update() # Обновляем экран, чтобы применить изменения

    search_button = ft.ElevatedButton(
        text="Узнать погоду", 
        on_click=search_click, 
        width=250
    )

    # Добавляем элементы на страницу
    page.add(
        ft.Column(
            controls=[
                ft.Text("Прогноз погоды", size=24, weight=ft.FontWeight.BOLD),
                city_input,
                search_button,
                ft.Divider(), # Разделительная линия
                result_text,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )
