const axios = require('axios');

async function analyzePost(postText) {
    try {
        const url = 'http://127.0.0.1:8000/analyze/'; // FastAPI endpoint

        // Send a POST request to the FastAPI server
        const response = await axios.post(url, {
            text: postText
        });

        console.log("Post approved:", response.data.approved); // True or False
    } catch (error) {
        console.error("Error analyzing post:", error.message);
    }
}

// Example Usage
analyzePost("I absolutely love this product! It's amazing.");
// analyzePost("This is the worst experience I have ever had.");
