const serverless = require('serverless-http');
const wsgi = require('wsgi-request');
const { spawn } = require('child_process');

// Start Django server
const server = spawn('python', ['manage.py', 'runserver', '8000']);

server.stdout.on('data', (data) => {
  console.log(`stdout: ${data}`);
});

server.stderr.on('data', (data) => {
  console.error(`stderr: ${data}`);
});

// Handler
module.exports.handler = serverless(wsgi(server));