from twisted.words.protocols import irc
from twisted.internet import protocol

import logging

class TwitchBot(irc.IRCClient):
    def signedOn(self):
        self.join(self.factory.channel)
        logging.info("Signed on as {}".format(self.nickname))

    def joined(self, channel):
        logging.info("Joined {}".cormat(channel))

    def privmsg(self, user, channel, message):
        print(message)


class TwitchBotFactory(protocol.ClientFactory):
    protocol = TwitchBot

    def __init__(self, channel, nickname='test'):
        self.channel = channel
        self.nickname = nickname
        self.password = 'xxx'

    def clientConnectionLost(self, connector, reason):
        logging.warn("Lost connection ({}), reconnecting...".format(reason))
        connector.connect()

    def clientConnectionFailed(self, connector, reason):
        logging.error("Failed to connect! {}".format(reason))



import sys
from twisted.internet import reactor

# server = 'irc.twitch.tv'
server = 'irc.choopa.net'
port = 6667

reactor.connectTCP(server, port, TwitchBotFactory(''))
reactor.run()

