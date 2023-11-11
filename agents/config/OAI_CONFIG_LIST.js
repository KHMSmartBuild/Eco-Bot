const winston = require('winston');
require('dotenv').config()

let configList = [
    // GPT-4-Turbo
    {
        "model": "gpt-4-1106-preview",
        "api_key": process.env.OPENAI_API_KEY,
        "org_id": process.env.OpenAI_ORGANIZATION_ID, // if required
        "logger": winston.createLogger({
            level: 'info',
            format: winston.format.json(),
            transports: [
                new winston.transports.File({ filename: 'gpt-4-1106-preview.log' })
            ]
        })
    },
    // GPT-4
    {
        "model": "gpt-4",
        "api_key": process.env.OPENAI_API_KEY,
        "org_id": process.env.OPENAI_ORGANIZATION_ID, // if required
        "logger": winston.createLogger({
            level: 'info',
            format: winston.format.json(),
            transports: [
                new winston.transports.File({ filename: 'gpt-4.log' })
            ]
        })
    },
    // GPT-3.5
    {
        "model": "gpt-3.5-turbo",
        "api_key": process.env.OPENAI_API_KEY,
        "org_id": process.env.OPENAI_ORGANIZATION_ID, // if required
        "logger": winston.createLogger({
            level: 'info',
            format: winston.format.json(),
            transports: [
                new winston.transports.File({ filename: 'gpt-3.5-turbo.log' })
            ]
        })
    }
    // other configurations...
]