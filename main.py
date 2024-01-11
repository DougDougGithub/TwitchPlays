from src.twitchplays import TwitchPlays

##################### GAME CONSTANTS #####################
# Replace this with your Twitch username. Must be all lowercase.
TWITCH_CHANNEL = 'pdgeorge' 

# If streaming on Youtube, set this to False
STREAMING_ON_TWITCH = True

# If you're streaming on Youtube, replace this with your Youtube's Channel ID
# Find this by clicking your Youtube profile pic -> Settings -> Advanced Settings
YOUTUBE_CHANNEL_ID = "YOUTUBE_CHANNEL_ID_HERE" 

# If you're using an Unlisted stream to test on Youtube, replace "None" below with your stream's URL in quotes.
# Otherwise you can leave this as "None"
YOUTUBE_STREAM_URL = None

# ========== GAME ==========

# Change this to your game. It must match the file name in the "Games" folder. Capitalization is important.
GAME_FILE_NAME = "template"

# ========== MESSAGE QUEUE CONFIG ==========

# MESSAGE_RATE controls how fast we process incoming Twitch Chat messages. It's the number of seconds it will take to handle all messages in the queue.
# This is used because Twitch delivers messages in "batches", rather than one at a time. So we process the messages over MESSAGE_RATE duration, rather than processing the entire batch at once.
# A smaller number means we go through the message queue faster, but we will run out of messages faster and activity might "stagnate" while waiting for a new batch.
# A higher number means we go through the queue slower, and messages are more evenly spread out, but delay from the viewers' perspective is higher.
# You can set this to 0 to disable the queue and handle all messages immediately. However, then the wait before another "batch" of messages is more noticeable.
MESSAGE_RATE = 0.5

# MAX_QUEUE_LENGTH limits the number of commands that will be processed in a given "batch" of messages.
# e.g. if you get a batch of 50 messages, you can choose to only process the first 10 of them and ignore the others.
# This is helpful for Games where too many inputs at once can actually hinder the gameplay.
# Setting to ~50 is good for total chaos, ~5-10 is good for 2D platformers
MAX_QUEUE_LENGTH = 20

# Maximum number of threads you can process at a time. If you don't know, just leave it on 100.
# If you experience performance problems, you could try lowering this number.
# This should not be needed as this script is very lightweight and if you can live stream, you can handle 100 threads.
MAX_WORKERS = 100

# This is the time in seconds until chat messages start counting, giving you some time to tab into the game.
STARTUP_TIME = 0

try:
    TP = TwitchPlays(
        STREAMING_ON_TWITCH,
        TWITCH_CHANNEL,
        YOUTUBE_CHANNEL_ID,
        YOUTUBE_STREAM_URL,
        GAME_FILE_NAME,
        MESSAGE_RATE,
        MAX_QUEUE_LENGTH,
        MAX_WORKERS,
        STARTUP_TIME,
    )
    TP.start()
except KeyboardInterrupt:
    print('Script stopped successfully.')