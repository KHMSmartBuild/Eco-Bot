@echo off

:: Directories
mkdir ProjectRoot\APIGateway
mkdir ProjectRoot\Backend\dataLayer
mkdir ProjectRoot\Backend\processingLayer
mkdir ProjectRoot\SecurityLayer
mkdir ProjectRoot\Frontend
mkdir ProjectRoot\RealTimeData
mkdir ProjectRoot\AssistantBotLayer

:: Files
type nul > ProjectRoot\APIGateway\queryHandler.js

type nul > ProjectRoot\Backend\dataLayer\dataRetriever.js
type nul > ProjectRoot\Backend\dataLayer\blockchainVerifier.js

type nul > ProjectRoot\Backend\processingLayer\responseFormatter.js

type nul > ProjectRoot\SecurityLayer\authenticator.js

type nul > ProjectRoot\Frontend\dashboardRenderer.js

type nul > ProjectRoot\RealTimeData\realTimeProcessor.js

type nul > ProjectRoot\AssistantBotLayer\librarianBot.js

echo Script executed successfully.