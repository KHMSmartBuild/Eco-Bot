// Importing the necessary module for YAML parsing
const yaml = require('js-yaml');
const fs = require('fs');

// Sample function to convert YAML to JSON
const convertYAMLtoJSON = (yamlFilePath) => {
    try {
        // Read the YAML file
        const fileContents = fs.readFileSync(yamlFilePath, 'utf8');
        
        // Convert YAML to JSON
        const jsonData = yaml.load(fileContents);

        // Structure the data for D3.js (if needed)
        // For example, you might want to create an array of nodes and an array of links
        // ...

        return jsonData;
    } catch (e) {
        console.error("Error in converting YAML to JSON:", e);
        return null;
    }
};

module.exports = convertYAMLtoJSON;
