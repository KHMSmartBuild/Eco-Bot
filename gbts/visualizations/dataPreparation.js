// prepare the data from the conversation between the user and the bot
// ensure that the data is in the correct format for the visualization
// add the data to the seed data script formatted for the visualization

// This is a placeholder for your raw conversation data
let rawConversationData = [
    { sender: 'user', content: 'Hello, bot!' },
    { sender: 'bot', content: 'Hello, user!' },
    // ...
];

// This is a placeholder for your seed data
let seedData = [];

function prepareData(rawData) {
    // Parse the raw data
    let parsedData = rawData.map(message => {
        return {
            sender: message.sender,
            content: message.content,
            // Add any other fields you need for your visualization
        };
    });

    // Add the parsed data to the seed data
    seedData = seedData.concat(parsedData);
}

// Call the function to prepare the data
prepareData(rawConversationData);

console.log(seedData);

