import os
import asyncio
import discord
from dotenv import load_dotenv
import instaloader
import random

# Load environment variables from .env file
load_dotenv()

# Get configuration from environment variables
BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
CHANNEL_ID = int(os.getenv('DISCORD_CHANNEL_ID'))
GUILD_ID = int(os.getenv('DISCORD_GUILD_ID'))
INSTAGRAM_USERNAME = os.getenv('INSTAGRAM_USERNAME')
INSTAGRAM_PASSWORD = os.getenv('INSTAGRAM_PASSWORD')

# Define Discord intents
intents = discord.Intents.default()
intents.message_content = True

# Create a Discord client
client = discord.Client(intents=intents)

# Store the shortcodes of the last posts sent for each username
last_post_shortcodes = {}

def random_range(a, b, c, d, e):
    """Return a random integer from specified ranges."""
    choice = random.choice([(a, b), (c, d), (e, e)])
    return random.randint(choice[0], choice[1])

async def fetch_latest_unpinned_post(loader, username):
    """Fetch the latest unpinned post for a given Instagram username."""
    try:
        profile = instaloader.Profile.from_username(loader.context, username)
        posts = profile.get_posts()
        
        # Iterate through the posts to find the latest unpinned post
        for post in posts:
            post_shortcode = post.shortcode

            # If this post was sent already, skip it (pinned post issue workaround)
            if post_shortcode == last_post_shortcodes.get(username):
                continue  # Skip pinned or already sent posts

            # Extract post details
            caption = post.caption if post.caption else "No caption"
            image_url = post.url
            profile_pic_url = profile.profile_pic_url

            return caption, image_url, profile_pic_url, post_shortcode

        return None, None, None, None  # No new post found
    except Exception as e:
        print(f"Error fetching Instagram data for {username}: {str(e)}")
        return None, None, None, None

@client.event
async def on_ready():
    """Event triggered when the bot is ready."""
    print(f"Logged in as {client.user}")
    usernames = ["account1", "account2", "account3"]  # Add Instagram usernames here
    global last_post_shortcodes

    loader = instaloader.Instaloader()

    # Login to Instagram
    try:
        loader.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
        print("Successfully logged in to Instagram.")
    except Exception as e:
        print(f"Error logging in to Instagram: {str(e)}")
        return

    while True:
        for username in usernames:
            try:
                # Fetch the latest unpinned post
                caption, image_url, profile_pic_url, post_shortcode = await fetch_latest_unpinned_post(loader, username)

                # Skip if there's no new post to send
                if not post_shortcode or post_shortcode == last_post_shortcodes.get(username):
                    print(f"No new post to send for {username}.")
                    continue

                guild = client.get_guild(GUILD_ID)
                if not guild:
                    print(f"Error: Could not find the specified guild (ID: {GUILD_ID}).")
                    continue

                channel = client.get_channel(CHANNEL_ID)
                if channel and channel.permissions_for(guild.me).send_messages:
                    if caption or image_url or profile_pic_url:
                        # Create and send an embed for the Instagram post
                        embed = discord.Embed(description=caption)
                        embed.set_thumbnail(url=profile_pic_url)
                        embed.set_image(url=image_url)
                        embed.add_field(name="View Post", value=f"[Click here](https://www.instagram.com/p/{post_shortcode}/)")

                        await channel.send(embed=embed)
                        last_post_shortcodes[username] = post_shortcode  # Update the last sent post shortcode
                    else:
                        await channel.send(f"Failed to fetch the latest Instagram post from @{username}.")
                else:
                    print(f"Error: Channel not found or missing permissions (Channel ID: {CHANNEL_ID}).")

            except Exception as e:
                print(f"An unexpected error occurred while processing {username}: {str(e)}")

        # Randomize the sleep time between checks
        sleep_time = random_range(60, 120, 600, 1200, 1800)  # Options for sleep duration
        print(f"Sleeping for {sleep_time} seconds...")
        await asyncio.sleep(sleep_time)

if __name__ == "__main__":
    # Check for missing environment variables
    if not all([BOT_TOKEN, CHANNEL_ID, GUILD_ID, INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD]):
        print("Error: One or more required environment variables are missing.")
    else:
        client.run(BOT_TOKEN)
