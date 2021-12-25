# -*- coding: utf-8 -*-

# Módulos importados
from os.path import realpath
from subprocess import run

# Modulos integrados (src)
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaContent

from jsonTools import set_json
from utils import setIcon, setSound
from version import __pagename__


########################################################################################################################


# Função para exibição de notificação.
def notifyMessage(self):
    if self.soma > 1:
        ms = 'Unread messages.'
    else:
        ms = 'Unread message.'
    com = 'notify-send --app-name="' + __pagename__ + '" --expire-time=' + str(set_json('TimeMessage')) + \
          ' --icon="' + realpath(setIcon('notify')) + '" "' + str(self.soma) + ' ' + ms + '"'
    run(com, shell=True)


# Essa função pode variar conforme o webapp.
def verifyNotify(self, res):
    self.soma = 0
    tags = res.findAll(
        "span",
        {"class": "bp9cbjyn ljqsnud1 pq6dq46d datstx6m taijpn5t jb3vyjys jxrgncrl qt6c0cv9 qnrpqo6b k4urcfbm"}
    )

    for tag in tags:
        self.soma += int(tag.getText())  # Contabilizando o número de mensagens
    if self.soma != self.notify and self.soma != 0:
        if self.isHidden() or int(self.windowState()) == 1 or int(self.windowState()) == 3:
            if set_json('NotifySound'):
                self.notify_sound.setMedia(QMediaContent(QUrl.fromLocalFile(setSound(set_json('SoundTheme')))))
                self.notify_sound.play()
            if set_json('NotifyMessage'):
                notifyMessage(self)
        self.notify = self.soma  # Necessário para mapear alterações no número de
