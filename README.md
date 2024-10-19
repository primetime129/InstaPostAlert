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
DISCORD_BOT_TOKEN: Your Discord bot token from the developer portal.<br>
DISCORD_CHANNEL_ID: The ID of the Discord channel where you want the bot to send Instagram updates.<br>
DISCORD_GUILD_ID: The ID of your Discord server (guild).<br>
INSTAGRAM_USERNAME: Instagram username for the bot to log in and fetch posts.<br>
INSTAGRAM_PASSWORD: Password for the Instagram account.

---

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
---

### 7. Troubleshooting

You can clone the InstaPostAlert repository using Git or download it directly.<br>

Login Issues: Make sure your Instagram credentials are correct and that you’ve logged in with them on a browser recently to avoid verification prompts.<br>
Discord Errors: Check that the bot has appropriate permissions in the designated channel.<br>
Interval Adjustments: The bot’s fetch intervals are randomized for safety. You can adjust the time window in the random_range function to suit your needs.

---
