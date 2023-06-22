from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message
from aiogram import F
from config.config import host_url
from db.models import TelegramUser
from sqlalchemy.ext.asyncio import AsyncSession
from utils.response import get_tasks_with_auth, is_response_ok

router = Router()


class SetLinkAucsState(StatesGroup):
    unlinked_aucs = State()
    linked_aucs = State()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await message.answer(
        "Hi there! Enter your telegram auth key from "
        f"<a href='{host_url}/accounts/profile/'>your profile</a>."
    )
    await state.set_state(SetLinkAucsState.unlinked_aucs)


@router.message(Command("cancel"))
@router.message(F.text.casefold() == "cancel")
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Your data was cleared.")


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


@router.message(SetLinkAucsState.linked_aucs)
async def linkink_aucs():
    pass
