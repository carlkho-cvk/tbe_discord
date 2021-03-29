import random
import discord


# Fitness monday variables
morning_alert = "08:00"
date_announce = [1, 3, 5]
image_file_list = [
    'Exercise_Three.png',
    'Exercise_Two_2.png'
]


# Messages to be display for fitness monday
fitness_message = [
    "🏋️ Good morning @everyone!!! Here's your workout session for today! 🏋️",
]


# Handler for all task in fitness monday
async def fitness_monday(current_time, current_week_day, client, channel_id):
    '''
    current_time - required
    current_week_day - Monday=1 ... Sunday=7
    client - discord client
    channel_id - this is where the bot will sel
    discord bot will validate on what to
    send to the text channel
    '''
    text_channel = client.get_channel(channel_id)
    random_message = random.choice(fitness_message)
    random_image = random.choice(image_file_list)

    if current_week_day in date_announce:
        if f'{morning_alert}:00' == current_time:
            await text_channel.send(random_message)
            await text_channel.send(file=discord.File(random_image))
