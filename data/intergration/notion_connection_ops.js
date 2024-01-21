const { Client, APIErrorCode, LogLevel } = require("@notionhq/client")

const notion = new Client({
  auth: process.env.NOTION_TOKEN,
  logLevel: LogLevel.DEBUG,
})

;(async () => {
  try {
    const listUsersResponse = await notion.users.list({})
    console.log(listUsersResponse)
  } catch (error) {
    if (error.code === APIErrorCode.ObjectNotFound) {
      // handle by asking the user to select a different database
    } else {
      // Other error handling code
      console.error(error)
    }
  }
})()