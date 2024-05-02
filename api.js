const express = require('express');
const { exec } = require('child_process');
const fs = require('fs');
const app = express();
const PORT = 3000;

app.use(express.json()); // Para parsear application/json

// Endpoint para encriptar datos
app.post('/encrypt', (req, res) => {
    const { data } = req.body;
    // Escribir los datos en un archivo temporal
    fs.writeFileSync('temp.txt', data);
    // Ejecutar el script de Python
    exec(`python3 Encriptacion.py encrypt temp.txt`, (error, stdout, stderr) => {
        if (error) {
            console.error(`exec error: ${error}`);
            return res.status(500).send(stderr);
        }
        // Eliminar el archivo temporal después de usarlo
        fs.unlinkSync('temp.txt');
        res.send({ encrypted: stdout });
    });
});

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
