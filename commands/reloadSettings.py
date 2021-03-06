from CommandTemplate import CommandTemplate
import GlobalStore
from IrcMessage import IrcMessage


class Command(CommandTemplate):
	triggers = ['reloadsettings']
	helptext = "Reloads the settings from disk. Only rarely useful"
	adminOnly = True

	def execute(self, message):
		"""
		:type message: IrcMessage
		"""
		replytext = u""
		#If the keyword 'all' was provided, reload the settings of all bots
		if message.message.lower() == "all":
			serversWithReloadFault = []
			for serverfolder, botfactory in GlobalStore.bothandler.botfactories.iteritems():
				success = botfactory.updateSettings()
				if not success:
					serversWithReloadFault.append(serverfolder)

			replytext = u"Reloaded all settings"
			if len(serversWithReloadFault) > 0:
				replytext += u" (error reloading settings for {})".format("; ".join(serversWithReloadFault))
		#Otherwise, just reload the settings of this bot
		else:
			success = message.bot.factory.updateSettings()
			if success:
				replytext = u"Successfully reloaded settings for this bot"
			else:
				replytext = u"An error occurred while trying to reload the settings for this bot, check the debug output for the cause"
				
		message.bot.say(message.source, replytext)