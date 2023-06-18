from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message
from django.contrib.auth import get_user_model

from todo.models import Task

router = Router()

User = get_user_model()


class SetAuthKeyState(StatesGroup):
    waiting_for_key = State()
    key_is_verified = State()


@router.message(CommandStart())
async def process_start_cmd(message: Message, state: FSMContext):
    await message.answer("Enter your auth key from your profile:")
    await state.set_state(SetAuthKeyState.setting_len_pass)


@router.message(SetAuthKeyState.setting_len_pass)
async def process_key(message: Message, state: FSMContext):
    auth_telegram_key = message.text
    user = User.objects.filter(telegram_key=auth_telegram_key).first()
    if user:
        await message.answer("Welcome! To get tasks - /tasks")
        user.is_telegram_verified = True
        await state.update_data(auth_telegram_key=auth_telegram_key)
        await state.set_state(SetAuthKeyState.key_is_verified)
    else:
        await message.answer("Invalid key. Please try again.")


@router.message(SetAuthKeyState.setting_len_pass, Command("tasks"))
async def getting_tasks(message: Message, state: FSMContext):
    data = await state.get_data()
    auth_telegram_key = data.get("auth_telegram_key")
    user = User.objects.filter(telegram_key=auth_telegram_key).first()
    if user:
        tasks_message = ""
        k = 1
        tasks = Task.objects.filter(user=user)
        for task in tasks:
            tasks_message += f"{k}) <b>{task.title}</b>\n{task.description}"
        await message.answer("All tasks to do:\n" + tasks_message)


@router.message(Command("cancel"))
async def cancel_cmd(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text="Canceled.",
    )


@router.message()
async def send_answer(message: Message):
    await message.answer(text="Unknown command.")
