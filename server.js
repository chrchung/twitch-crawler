/**
 * Created by christina on 2017-11-06.
 */

var tmi = require('tmi.js');
var fs = require('fs');

var options = {
    options: {
        debug: true
    },
    connection: {
        cluster: 'aws',
        reconnect: true
    },
    identity: {
        username: 'randomasshole',
        password: 'oauth:tc97i9ef0ez6rkdgjmlygvajbzkk1s'
    },
    channels: ['grinninggoat']
};


var client = new tmi.client(options);
client.connect();

client.on('chat', function(channel, user, message, self) {

    var parsedMessage = JSON.stringify({
        user: user,
        channel: channel,
        message: message
    }) + ",";

    console.log(parsedMessage);


    fs.appendFile('chatlog.txt', parsedMessage, function (err, data) {
        if (err) {
            return console.log(err);
        }
    });

});
