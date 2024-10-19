# Creating a Discord Bot

Follow these steps to create your own Discord bot and connect it to your server.

## Step 1: Create a Discord Account

If you don't have a Discord account, sign up at [discord.com](https://discord.com/).

## Step 2: Access the Discord Developer Portal

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Log in with your Discord account.

## Step 3: Create a New Application

1. Click on the **"New Application"** button at the top right.
2. Enter a name for your application (this will be your bot's name) and click **"Create"**.

## Step 4: Create a Bot User

1. In your application settings, navigate to the **"Bot"** tab on the left sidebar.
2. Click on the **"Add Bot"** button, and then confirm by clicking **"Yes, do it!"**.
3. Once the bot is created, you can customize its username and profile picture if you wish.

## Step 5: Copy Your Bot Token

1. Under the **"Bot"** tab, you will see a section labeled **"TOKEN"**.
2. Click the **"Copy"** button to copy your bot token. **Keep this token secret!** This token is used to authenticate your bot and should not be shared with anyone.

## Step 6: Invite the Bot to Your Server

1. Go to the **"OAuth2"** tab in your application settings.
2. In the **"Scopes"** section, check the **"bot"** checkbox.
3. In the **"Bot Permissions"** section, select the permissions your bot will need (for example, **Send Messages**, **Read Message History**, etc.).
4. Copy the generated URL from the **"Scopes"** section.
5. Open the URL in your web browser, select the server you want to invite the bot to, and click **"Authorize"**.

## Step 7: Set Up Permissions

Make sure your bot has the necessary permissions in the Discord server. You can adjust permissions in the server settings or by editing the bot’s role.

## Step 8: Enable Developer Mode (Optional)

To get the Channel and Guild IDs easily:

1. Go to Discord and click on **User Settings** (the gear icon).
2. Scroll down to **Advanced** and enable **Developer Mode**.

With Developer Mode enabled, you can right-click on channels and servers to copy their IDs.

## Conclusion

You have successfully created a Discord bot and invited it to your server! Now you can proceed to configure your bot and run it using the provided Python script in your project.

For further assistance with your bot, refer to the Python setup instructions in the README.

