<script type="text/javascript" src="https://rawgit.com/131/h264-live-player/master/vendor/dist/http-live-player.js"></script>
<script>
    var canvas = document.createElement("canvas");
    document.body.appendChild(canvas);
 
    var wsavc = new WSAvcPlayer(canvas, "webgl");
 
    wsavc.connect(YOUR_WEBSOCKET_URL);
</script> 