# data/intergration/Async_AgentDB_notion.py
import os
import asyncio
import aiopg
from notion_integration import async_notion as AsyncClient
from dotenv import load_dotenv

# Load environment variables from the .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Retrieve the Notion integration token from environment variables
NOTION_TOKEN = os.getenv('Eco-Notion_integration')

# Ensure the token is available
if NOTION_TOKEN is None:
    raise ValueError("Missing 'Eco-Notion_integration' environment variable.")

# Define your PostgreSQL connection details
# Assuming session.get_bind().url.dsn returns a valid DSN string
from data.database.utils.setconn import session
PG_DSN = session().get_bind().url.dsn

# Initialize the Notion API client with the token
notion = AsyncClient(auth=NOTION_TOKEN)

# Define a function to update Notion tables asynchronously
async def update_notion_table(table_id, data):
    # TODO: Implement the logic to update the Notion table based on the data provided
    # Example (update this with actual implementation):
    # response = await notion.pages.update(page_id=table_id, properties=data)
    pass

# Define a function to listen for database changes asynchronously
async def listen_db_changes():
    async with aiopg.create_pool(PG_DSN) as pool:
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                # Set up a listen query for each table you're interested in
                await cur.execute("LISTEN assistants_changes;")
                await cur.execute("LISTEN threads_changes;")
                await cur.execute("LISTEN runs_changes;")
                await cur.execute("LISTEN tools_changes;")

                # Continuously listen for notifications and process them
                while True:
                    msg = await conn.notifies.get()
                    data = parse_notification(msg)
                    await update_notion_table(data['table_id'], data)

# Function to parse database notifications
def parse_notification(notification):
    # TODO: Parse the notification to get the table ID and data
    # Example (update this with actual implementation):
    # return {'table_id': notification.channel, 'data': notification.payload}
    return {'table_id': '...', 'data': {...}}

# Main function to run the asyncio loop
async def main():
    # Run the database change listener
    await listen_db_changes()

# Run the asyncio loop
if __name__ == '__main__':
    asyncio.run(main())
