from datetime import datetime, date
import discord
import time

from fitness_monday import fitness_monday
from fruity_wednesday import fruity_wednesday
from health_reminder import health_reminder
from inspirational_friday import inspirational_friday
from meal_reminder import meal_reminder


# Discord auth variables
client = discord.Client()
fitness_monday_channel = 797520995011002378
discord_bot_id = 'NzgyMjIxNDcwNTg3NTUxNzY0.X8JCgw.RZmdItcMTHvoR126Ud2iM4_ffJs'


def check_date_time(current_time):
    '''
    For debugging only
    Check what is our current time, date and second
    '''
    print("Current Time =", current_time)


# Function will triggered when discord client starts
@client.event
async def on_ready():
    while True:
        status_time = datetime.now()
        current_week_day = date.today().isoweekday()
        current_time = status_time.strftime("%H:%M:%S")

        # Run all functions here
        check_date_time(current_time)
        await fitness_monday(current_time=current_time, current_week_day=current_week_day,
                             client=client, channel_id=fitness_monday_channel)
        await fruity_wednesday(current_time=current_time, current_week_day=current_week_day,
                               client=client, channel_id=fitness_monday_channel)
        await health_reminder(current_time=current_time, current_week_day=current_week_day,
                              client=client, channel_id=fitness_monday_channel)
        await inspirational_friday(current_time=current_time, current_week_day=current_week_day,
                                   client=client, channel_id=fitness_monday_channel)
        await meal_reminder(current_time=current_time, current_week_day=current_week_day,
                            client=client, channel_id=fitness_monday_channel)

        time.sleep(1)


client.run(discord_bot_id)
