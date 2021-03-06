from CommandTemplate import CommandTemplate
import GlobalStore
from IrcMessage import IrcMessage


class Command(CommandTemplate):
	triggers = ['debug']
	helptext = "Used in debugging. Only really useful to my owner"
	showInCommandList = False
	adminOnly = True

	def execute(self, message):
		"""
		:type message: IrcMessage
		"""
		for serverfolder, botfactory in GlobalStore.bothandler.botfactories.iteritems():
			print "Channel and user list for {}:".format(botfactory.serverfolder)
			print botfactory.bot.channelsUserList