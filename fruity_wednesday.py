# Fitness monday variables
fruity_wed_1 = "08:00"
fruity_wed_2 = "10:00"
fruity_wed_3 = "12:30"
date_announce = [3]


# Messages to be display for fitness monday
fruity_wed_1_msg = "Fruity Wednesdays @everyone"
fruity_wed_2_msg = "Fruity Wednesdays @everyone"
fruity_wed_3_msg = "Fruity Wednesdays @everyone"


# Handler for all task in fitness monday
async def fruity_wednesday(current_time, current_week_day, client, channel_id):
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
        if f'{fruity_wed_1}:00' == current_time:
            await text_channel.send(fruity_wed_1_msg)

        if f'{fruity_wed_2}:00' == current_time:
            await text_channel.send(fruity_wed_2_msg)

        if f'{fruity_wed_3}:00' == current_time:
            await text_channel.send(fruity_wed_3_msg)
