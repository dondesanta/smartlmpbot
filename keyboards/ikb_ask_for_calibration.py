from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


ikb_ask_for_calibration = InlineKeyboardMarkup(row_width=2,
                                               inline_keyboard=[
                                                   [
                                                       InlineKeyboardButton(text='Да', callback_data='yes_button'),
                                                       InlineKeyboardButton(text='Нет', callback_data='no_button')
                                                   ]
                                               ])
