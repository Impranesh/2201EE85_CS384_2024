const express = require('express');
const path = require('path');
const multer = require("multer");
const { PythonShell } = require('python-shell');
const app = express();
const PORT = 3000;

// Set view engine to EJS
app.set('view engine', 'ejs');

// Serve static files from the public directory
app.use(express.static(path.join(__dirname, 'public')));



// Set up multer for file upload
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, 'uploads/');  // Store uploaded files in the 'uploads' directory
  },
  filename: (req, file, cb) => {
    cb(null, file.originalname);  // Keep the original filename
  },
});
const upload = multer({ storage: storage });


// Home route - display the button
app.get('/', (req, res) => {
    res.render('index', { message: null }); // No message initially
});

// Route to trigger Python script and generate the output file
app.post('/generate', (req, res) => {

    if (!req.file) {
      return res.render("index", { message: "Please upload a file." });
    }

    let options = {
      scriptPath: __dirname,
      args: [req.file.path, "demo1.xlsx"], // Use the uploaded file path as input to Python
    };
    // console.log("Hello!!");
    PythonShell.run('tut11.py', options, (err) => {
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
    const filePath = path.join(__dirname, 'demo1.xlsx');
    res.download(filePath, 'demo1.xlsx', (err) => {
        if (err) {
            console.error("Error downloading file:", err);
        }
    });
});

app.listen(PORT, () => {
    console.log("Server is running at http://localhost:${PORT}");
});