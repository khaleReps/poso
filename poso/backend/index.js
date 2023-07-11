const express = require('express');
const app = express();
const cred = 'mongodb+srv://demo_user:fakepassword3000@cluster0.1xup6ed.mongodb.net/?retryWrites=true&w=majority';

// MongoDB configuration
const mongoose = require('mongoose');
mongoose.connect(cred, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
  dbName: '<your-database-name>',
})
  .then(() => {
    console.log('Connected to MongoDB');
  })
  .catch((error) => {
    console.error('Error connecting to MongoDB:', error);
  });

// API routes

const port = 3000;
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
