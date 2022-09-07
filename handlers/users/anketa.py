from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Commands, Command

from loader import dp
from states.state import PersonalData


@dp.message_handler(Command("anketa"), state=None)
async def get_anketa(message: types.Message):
    await message.answer("To'liq ismingizni kiriting")
    await PersonalData.fullname.set()


@dp.message_handler(state=PersonalData.fullname)
async def get_full_name(message: types.Message, state: FSMContext):
    full_name = message.text
    await state.update_data({"name": full_name})

    await message.answer("Email manzilingizni kiriting")
    await PersonalData.next()


@dp.message_handler(state=PersonalData.email)
async def get_email(message: types.Message, state: FSMContext):
    email = message.text
    await state.update_data({
        "mail": email
    })
    await message.answer("Telefon raqamingizni kiriting")
    await PersonalData.next()


@dp.message_handler(state=PersonalData.PhoneNum)
async def get_phonenum(message: types.Message, state: FSMContext):
    phonenum = message.text
    await state.update_data({
        "phonenum": phonenum
    })

    data = await state.get_data()
    name = data.get("name")
    email = data.get("email")
    phone = data.get("phonenum")

    msg = "Quyidagi ma'lumotlar qabul qilindi: \n"
    msg += f"Ismingiz - {name}\n"
    msg += f"Email manzillingiz " \
           f"  {email}\n"
    msg += f"Telefon raqamingiz {phone}"

    await message.answer(msg)
    await state.finish()
    # await state.reset_state(with_data=False)
