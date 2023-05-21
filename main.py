
import openai

from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token='5608342899:AAGRgUMqM6ssrd1LpVpM1cCsZYp3Pqi5NEE')

dp = Dispatcher(bot)

openai.api_key = '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'

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет, меня зовут Спортик! Я часть большого проекта MetaFit. Я могу быть твоим личным"
                        "тренером, но учти, что в телеграмме мой функционал ограничен."
                        "Если ты хочешь получить больше функций, то скачай наше приложение из Google Play: \n "
                        "https://the-imran.dev/ \n"
                        "Ты можешь задать мне любой вопрос, связанный с спортом")


@dp.message_handler()
async def send_welcome(message: types.Message):
    text = message.text
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Ты умный и профессиональный тренер для спортсменов по имени Спортик. "
                                          "Ты отвечаешь только на вопросы связанные с спортом. "
                                          "На другие вопросы ты отказываешься отвечать. "
                                          "Ты очень квалифицирован, имеешь несколько высших спортивных образований, "
                                          "ты мастер спорта На все вопросы, которые не связаны с спортом,"
                                          " ты отказываешься отвечать. Ты являешься частью приложения MetaFit. "
                                          "Если вопрос не связан с спортом, ты не отвечаешь на него."
                                          "Ты не можешь задавать пользователю дополнительные вопросы"},

            {"role": "user", "content": text}
        ]
    )
    await message.reply(response.choices[0].message.content)


if __name__ == '__main__':
    print('runned')
    executor.start_polling(dp)
