from aiogram.dispatcher import FSMContext

from FSMs.fsm_class import ClientStatesGroup
from handlers.users.commands.menu import menu
from handlers.users.functions.calibration import calibration
from loader import dp, bot
from aiogram import types
from keyboards.ikb_ask_for_calibration import ikb_ask_for_calibration
from aiogram.dispatcher.filters import Text


async def ask_for_calibration(message, msg_id):
    await bot.edit_message_text(chat_id=message.from_user.id,
                                message_id=msg_id,
                                text='<b>Провести первоначальную калибровку?</b>\n'
                                     '\n'
                                     '<i>Советуется проводить калибровку, если:</i>\n'
                                     '<i>1. Что-то не работает</i>\n'
                                     '<i>2. Токен используется впервые.</i>',
                                reply_markup=ikb_ask_for_calibration)


@dp.callback_query_handler(Text(endswith='button'), state=ClientStatesGroup.token)
async def yes_or_no(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        token = data['token']
        message = data['message']
    if callback.data.startswith('yes'):
        await calibration(message=message, token=token, state=state)
    else:
        await menu(message=message, token=token, state=state)
