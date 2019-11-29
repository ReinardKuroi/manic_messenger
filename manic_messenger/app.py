from datetime import datetime
import discord
import json
import asyncio
from .log import logger


client = discord.Client(command_prefix='!')


def get_value_asserted(source, key):
    try:
        return source[key]
    except KeyError:
        logger.error('%s needs a value in settings.json!' % key)
        exit(1)

@client.event
async def on_ready():
    logger.info('We are logged in as %s, ID=%s' % (client.user.name, client.user.id))


async def daily_message(message, user_id, send_time):
    await client.wait_until_ready()
    user = client.get_user(user_id)
    logger.debug('Got user %s' % user)
    while not client.is_closed():
        now = datetime.strftime(datetime.now(), '%H:%M')
        if now == send_time:
            logger.debug('Sending message %s to %s' % (message, user.name))
            await user.send(message)
            await asyncio.sleep(90)
        else:
            await asyncio.sleep(1)


def main():
    try:
        with open('auth.json') as auth_file:
            auth_data = json.load(auth_file)
    except IOError as exc:
        logger.error('Credentials not found, check for auth.json!')
        exit(1)
    try:
        with open('settings.json') as settings_file:
            settings = json.load(settings_file)
    except IOError as exc:
        logger.error('Settings file not found, check for settings.json!')
        exit(1)
    try:
        message = get_value_asserted(settings, 'message')
        user_id = int(get_value_asserted(settings, 'user_id'))
        send_time = get_value_asserted(settings, 'send_time')
    except:
        logger.warning('One of the settings is empty! Did you forget to edit settings.json?')
        exit(1)
    client.loop.create_task(daily_message(message, user_id, send_time))
    try:
        client.run(auth_data['token'])
    except:
        logger.error('Invalid application token')
        exit(1)
