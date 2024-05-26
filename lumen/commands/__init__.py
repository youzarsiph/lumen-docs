""" Lumen commands """

from lumen.commands.dqa import dqa
from lumen.commands.init import init
from lumen.commands.qa import qa
from lumen.commands.summarize import summarize
from lumen.commands.transcribe import transcribe
from lumen.commands.translate import translate
from lumen.commands.vqa import vqa


commands = [dqa, init, qa, summarize, transcribe, translate, vqa]
