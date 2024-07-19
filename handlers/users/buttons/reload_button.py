from handlers.users.functions.get_menu_devices import get_menu
from FSMs.fsm_class import ClientStatesGroup
from keyboards.ikb_menu import ikb_menu

from aiogram.utils.exceptions import MessageNotModified
from aiogram.dispatcher.storage import FSMContext
from loader import dp
from aiogram import types


@dp.callback_query_handler(state=ClientStatesGroup.menu, text='reload_button')
async def reload(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        token = data['token']
        dict_ = await get_menu(token)
        try:
            await callback.message.edit_text(text=dict_['text'],
                                             reply_markup=ikb_menu(token, dict_['num']))
            await callback.answer()
        except MessageNotModified:
            print('MessageNotModified')
            await callback.answer('Состояние не изменилось!')
            pass
