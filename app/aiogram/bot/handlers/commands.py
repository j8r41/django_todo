from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message
from config.config import host_url
from db.models import TelegramUser
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from utils.response import get_tasks_with_auth, is_response_ok

router = Router()


class SetLinkAucsState(StatesGroup):
    unlinked_aucs = State()
    linked_aucs = State()


@router.message(CommandStart())
async def cmd_start(
    message: Message, state: FSMContext, session: AsyncSession
):
    stmt = select(TelegramUser).where(
        TelegramUser.user_id == message.from_user.id
    )
    result = await session.execute(stmt)
    current_user: TelegramUser = result.scalars().first()
    if current_user:
        await state.set_state(SetLinkAucsState.linked_aucs)
        await message.answer(
            "You have already registered!\nTo get task list - /tasks"
        )
    else:
        await message.answer(
            "Hi there! Enter your telegram auth key from "
            f"<a href='{host_url}/accounts/profile/'>your profile</a>."
        )
        await state.set_state(SetLinkAucsState.unlinked_aucs)


@router.message(Command("cancel"))
@router.message(F.text.casefold() == "cancel")
async def cmd_cancel(
    message: Message, state: FSMContext, session: AsyncSession
):
    current_user = delete(TelegramUser).where(
        TelegramUser.user_id == message.from_user.id
    )
    if current_user is not None:
        await session.execute(current_user)
        await session.commit()
        await state.clear()
        await message.answer(
            "Your data was successfully deleted. Start again - /start"
        )
    else:
        await message.answer("You are not registered in our system.")


@router.message(SetLinkAucsState.unlinked_aucs)
async def linkink_aucs(
    message: Message, state: FSMContext, session: AsyncSession
):
    if await is_response_ok(message.text) == 200:
        telegram_auth_key = message.text
        new_user = TelegramUser(
            user_id=message.from_user.id,
            telegram_auth_key=telegram_auth_key,
        )
        session.add(new_user)
        await session.commit()
        await message.answer("Success! Your telegram profile is linked.")
        await state.set_state(SetLinkAucsState.linked_aucs)
    else:
        await message.answer(
            "Error: this key does not exist. Check the key once again!"
        )


@router.message(SetLinkAucsState.linked_aucs, Command("tasks"))
async def send_task_list(
    message: Message, state: FSMContext, session: AsyncSession
):
    stmt = select(TelegramUser).where(
        TelegramUser.user_id == message.from_user.id
    )
    result = await session.execute(stmt)
    current_user: TelegramUser = result.scalars().first()

    data = await get_tasks_with_auth(
        telegram_key=current_user.telegram_auth_key
    )
    for task in data:
        text_message = ""
        title = task.get("title")
        text_message += f"<b>{title}</b>\n"
        description = task.get("description")
        text_message += f"<i>Description:</i> {description}\n"
        end_date = task.get("end_date")
        if end_date is not None:
            text_message += f"<i>Ended at:</i> {end_date}\n"
        status = task.get("status")
        if status != "":
            text_message += f"<i>Status:</i> {status}\n"
        created_at = task.get("created_at")
        if created_at is not None:
            text_message += f"<i>Created at:</i> {created_at}\n"
        await message.answer(text_message)
