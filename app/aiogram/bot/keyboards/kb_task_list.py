from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import types

kb_task_list = ReplyKeyboardBuilder()
kb_task_list.add(types.KeyboardButton(text="Get task list 📋"))
kb_task_list.add(types.KeyboardButton(text="Cancel ❌"))
