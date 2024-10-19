# InstaPostAlert: Automated Instagram Post Notifications for Discord

InstaPostAlert is a Discord bot that automatically monitors Instagram accounts and sends new posts directly to your Discord server. Perfect for content creators, brands, news organizations, and community managers, this bot ensures that your server stays updated with the latest Instagram content—complete with captions, images, and profile links.

## Key Features:
- Automatically fetches the latest Instagram posts from specified accounts.
- Sends posts, images, and captions directly to a designated Discord channel.
- Randomized intervals for fetching posts to avoid detection.
- Supports multiple Instagram accounts.
- Easy configuration using environment variables.

Stay updated and keep your community engaged with InstaPostAlert.

---

## Setup Guide for InstaPostAlert

Follow these step-by-step instructions to install, configure, and run the InstaPostAlert bot on your own server:

### 1. Prerequisites

Before you begin, make sure you have the following installed:
- [Python 3.9+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads) (optional, for cloning the repository)
- A Discord bot token (you can create one via the [Discord Developer Portal](https://discord.com/developers/applications))
- Instagram login credentials (for the bot to fetch posts)

---

### 2. Clone the Repository

You can clone the InstaPostAlert repository using Git or download it directly.

```bash
git clone https://github.com/your-username/InstaPostAlert.git
cd InstaPostAlertz
```

---

### 3. Install Required Libraries

Navigate to the bot directory and install the required Python libraries by running:

```bash
pip install -r requirements.txt
```
This will install discord.py, instaloader, and python-dotenv—all necessary for running the bot.

---

### 4. Create a .env File

In the root directory, create a .env file to securely store your bot credentials and settings:

```makefile
DISCORD_BOT_TOKEN=your-discord-bot-token
DISCORD_CHANNEL_ID=your-discord-channel-id
DISCORD_GUILD_ID=your-discord-server-id
INSTAGRAM_USERNAME=your-instagram-username
INSTAGRAM_PASSWORD=your-instagram-password
```
- DISCORD_BOT_TOKEN: Your Discord bot token from the developer portal.<br>
- DISCORD_CHANNEL_ID: The ID of the Discord channel where you want the bot to send Instagram updates.<br>
- DISCORD_GUILD_ID: The ID of your Discord server (guild).<br>
- INSTAGRAM_USERNAME: Instagram username for the bot to log in and fetch posts.<br>
- INSTAGRAM_PASSWORD: Password for the Instagram account.

---

### 5. Run the Bot

Start the bot by running the Python script:

```bash
python instapostalert.py
```
Once the bot is running, it will log into Instagram and Discord, fetching new posts from the Instagram accounts you specify in the code.

---

### 6. Customization

You can modify the list of Instagram accounts the bot monitors in the on_ready event

```python
usernames = ["account1", "account2", "account3"]  # Add Instagram usernames here
```
---

### 7. Troubleshooting

You can clone the InstaPostAlert repository using Git or download it directly.<br>

- Login Issues: Make sure your Instagram credentials are correct and that you’ve logged in with them on a browser recently to avoid verification prompts.<br>
- Discord Errors: Check that the bot has appropriate permissions in the designated channel.<br>
- Interval Adjustments: The bot’s fetch intervals are randomized for safety. You can adjust the time window in the random_range function to suit your needs.

---

With InstaPostAlert, your Discord server will stay connected with Instagram, bringing fresh content directly to your community in real-time. Enjoy keeping your audience engaged and informed!

---

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


