import random

# Time Frame (24-Hour Period)
morning_time = "08:00"
afternoon_time = "12:00"
evening_time = "20:03"


# Messages, it will choose random
messages = [
    '''Ayoko na! Break muna tayo! It's not you, it's me... char! Break muna sa work I mean 🤣 Time to do something you enjoy mga lods. Let's get inspired! 💙 Don't forget to share your awesome moments in #share-ko-lang with the hashtag #InspirationalFridays.  Ajaa everyone!''',


    ''' Psssttt... uyyy! Sinetch itey na Symphers na hindi lang daw magaling sa work pero sa other 'stuff' din❓🧐 Like parang hindi lang talented...multi-talented pa! Sige nga, inspire me ✨ Don't forget to share moments here at #random with the hashtag #InspirationalFridays From your friendly papi, peace out! ✌'''
]


# Tony Gif Variable
tony_gif = 'Tony.gif'


# Handler for all task in fitness monday
async def inspirational_friday(current_time, current_week_day, client, channel_id):
    '''
    current_week_day, 1=Monday - 7=Sunday
    '''
    text_channel = client.get_channel(channel_id)

    # Means it will run this task on Friday,
    if current_week_day == 5:
        if f'{morning_time}:00' == current_time:
            await text_channel.send(random.choice(messages))
            await text_channel.send(file=discord.File(tony_gif))

        if f'{afternoon_time}:00' == current_time:
            await text_channel.send(random.choice(messages))
            await text_channel.send(file=discord.File(tony_gif))

        if f'{evening_time}:00' == current_time:
            await text_channel.send(random.choice(messages))
            await text_channel.send(file=discord.File(tony_gif))
