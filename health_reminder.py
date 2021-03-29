# Fitness monday variables
morning_1 = "10:00"
morning_2 = "8:00"

afternoon_1 = "13:00"
afternoon_2 = "14:30"
afternoon_3 = "15:30"
afternoon_4 = "17:55"

evening_1 = "20:30"
evening_2 = "21:10"

date_announce = [1, 2, 3, 4, 5]
image_file_list = [
    'Exercise_Three.png',
    'Exercise_Two_2.png'
]


# Messages to be display for fitness monday
# messageContentVariables
morning_1_msg = "Do some stretches! @everyone."
morning_2_msg = "Drink water! @everyone."

afternoon_1_msg = "Breath fresh air outside before starting your afternoon shift. @everyone."
afternoon_2_msg = "Drink a glass of water. Stay hydrated, @everyone!"
afternoon_3_msg = "Get up and stretch! @everyone."
afternoon_4_msg = "Go out and breathe before the evening sync. @everyone."

evening_1_msg = "Do some stretches! @everyone."
evening_2_msg = "Drink water. Good night, @everyone."


# Handler for all task in fitness monday
async def health_reminder(current_time, current_week_day, client, channel_id):
    '''
    current_time - required
    current_week_day - Monday=1 ... Sunday=7
    client - discord client
    channel_id - this is where the bot will sel
    discord bot will validate on what to
    send to the text channel
    '''
    text_channel = client.get_channel(channel_id)

    if current_week_day in date_announce:
        if f'{morning_1}:00' == current_time:
            await text_channel.send(morning_1_msg)

        if f'{morning_2}:00' == current_time:
            await text_channel.send(morning_2_msg)

        if f'{afternoon_1}:00' == current_time:
            await text_channel.send(afternoon_1_msg)

        if f'{afternoon_2}:00' == current_time:
            await text_channel.send(afternoon_2_msg)

        if f'{afternoon_3}:00' == current_time:
            await text_channel.send(afternoon_3_msg)

        if f'{afternoon_4}:00' == current_time:
            await text_channel.send(afternoon_4_msg)

        if f'{evening_1}:00' == current_time:
            await text_channel.send(evening_1_msg)

        if f'{evening_2}:00' == current_time:
            await text_channel.send(evening_2_msg)
