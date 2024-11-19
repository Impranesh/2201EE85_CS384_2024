const express = require('express');
const path = require('path');
const { PythonShell } = require('python-shell');
const app = express();
const PORT = 3000;

// Set view engine to EJS
app.set('view engine', 'ejs');

// Serve static files from the public directory
app.use(express.static(path.join(__dirname, 'public')));

// Home route - display the button
app.get('/', (req, res) => {
    res.render('index', { message: null }); // No message initially
});

// Route to trigger Python script and generate the output file
app.get('/generate', (req, res) => {
    let options = {
        scriptPath: __dirname,
        args: ['Input-1.xlsx', 'Generated_Output.xlsx']
    };
    // console.log("Hello!!");
    PythonShell.run('assignment.py', options, (err) => {
        if (err) {
            console.error("Error running Python script:", err);
            return res.render('index', { message: "An error occurred while generating the output." });
        }
        
    });
    console.log("Output file generated successfully.");
    res.render('index2', { message: "Output generated successfully! " });
    
});

// Route to download the output file
app.get('/download', (req, res) => {
    const filePath = path.join(__dirname, 'Generated_Output.xlsx');
    res.download(filePath, 'Generated_Output.xlsx', (err) => {
        if (err) {
            console.error("Error downloading file:", err);
        }
    });
});

app.listen(PORT, () => {
    console.log(`Server is running at http://localhost:${PORT}`);
});
