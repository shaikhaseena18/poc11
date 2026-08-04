const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.send('Voting Results');
});

app.listen(80);
