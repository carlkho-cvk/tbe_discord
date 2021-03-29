# Fitness monday variables
bf_Time = "08:00"
l_Time = "12:00"
d_Time = "19:00"
date_announce = [1, 2, 3, 4, 5]

# Messages to be display for fitness monday
bf_Msg = "@everyone, time for breakfast! 😋🥚"
l_Msg = "@everyone, what's that? It's lunch time! 🍲"
d_Msg = "@everyone, I wonder what's for dinner? 🥘"


# Handler for all task in fitness monday
async def meal_reminder(current_time, current_week_day, client, channel_id):
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
        if f'{bf_Time}:20' == current_time:
            print('Alert Now')
            await text_channel.send(bf_Msg)
        if f'{l_Time}:00' == current_time:
            await text_channel.send(l_Msg)
        if f'{d_Time}:00' == current_time:
            await text_channel.send(d_Msg)
