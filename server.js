var raspividStream = require('raspivid-stream');
 
var stream = raspividStream();
 
// To stream over websockets:
videoStream.on('data', (data) => {
    ws.send(data, { binary: true }, (error) => { if (error) console.error(error); });
});
