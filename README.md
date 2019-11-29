####Before you can use the bot, you have to do some prep work. Don't worry, it should be easy.

#####First of all, you need a bot:
1. Go to https://discordapp.com/developers/applications
2. Click 'New Application' to add a new application
3. Give it a name
4. After the application is created, go to 'Bot' settings
5. Add a bot
6. Give it a name
7. Don't close the page, you will need it later

#####Now, time to edit some settings:
1. In this exact folder, you have a file auth.json
2. Open the file
3. You will see something like this: "token": ""
4. Don't close the file
5. Go to your bot page
6. Find 'TOKEN' and click 'Copy'
7. Paste said token into the auth.json file, like so: "token": "%your_token_here%"
8. Save the file


####Now, for our next trick, you'll set up the messaging itself.

#####Let's find our friend that we want to message to:
1. Open Discord
2. In your settings, go to Appearance
3. Scroll down to ADVANCED
4. Enable Developer Mode
5. Find your friend
6. Right click on him
7. Click 'Copy ID'

#####Time to edit settings.json:
1. Open settings.json
2. There will be some sample lines there
3. Find this one: "user_id": ""
4. Paste your friend's id into user_id: "user_id": "%id_goes_here%"
5. Now fill in the message: "message": "%message_goes_here%"
6. And the time, in 24hr format: "send_time": "HH:MM"