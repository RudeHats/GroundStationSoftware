const { app, BrowserWindow } = require('electron');
const path = require('path');

let mainWindow;

function createWindow() {
    mainWindow = new BrowserWindow({
        width: 1200,
        height: 800,
        webPreferences: {
            nodeIntegration: true,
            contextIsolation: false,
        }
    });

    // Load the login page by default
    mainWindow.loadFile('login.html');

    // Open DevTools (optional)
    mainWindow.webContents.openDevTools();
}

app.on('ready', createWindow);

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit();
    }
});

app.on('activate', () => {
    if (mainWindow === null) {
        createWindow();
    }
});



"git add frontend/assets frontend/images frontend/login.html frontend/login.css frontend/tel.css frontend/Telemetry.html frontend/server.py frontend/Maps.html frontend/map.css frontend/main.js frontend/Graphs.html frontend/graph.css README.md"