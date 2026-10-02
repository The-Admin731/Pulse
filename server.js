const express = require('express');
const app = express();
const PORT = 3000;

app.use(express.json());

app.post('/api/metrics', (req, res) => {
    const { node_id, cpu, ram } = req.body;
    const timestamp = new Date().toLocaleTimeString();

    console.log(`[${timestamp}] Metrics received from ${node_id} -> CPU: ${cpu}% | RAM: ${ram}%`);

    res.status(200).json({ status: "success", message: "Metrics received" });
});

app.listen(PORT, () => {
    console.log(`Pulse Central Server running at http://localhost:${PORT}`);
});