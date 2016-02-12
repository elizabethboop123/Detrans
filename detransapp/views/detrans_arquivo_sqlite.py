# coding: utf-8
import threading
import sqlite3
from datetime import datetime
import os

from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.conf import settings

from detrans_sqlite.importa import *
from detrans_sqlite import cria_db


class ThreadDetransSqlite(threading.Thread):
    # tempo com os ifs 10:35 as 11:12 = 37
    # tempo sem os ifs 11:55 as 12:33 = 37
    def __init__(self, threadName):

        threading.Thread.__init__(self)
        self.stopthread = threading.Event()
        self.threadName = threadName
        self.is_finalisado = False
        self.is_cancelado = False
        self.is_erro_processo = False
        self.detrans_sqlite_nome = settings.MEDIA_ROOT + '/detrans.sqlite'

    def run(self):

        try:

            if os.path.exists(self.detrans_sqlite_nome):
                os.remove(self.detrans_sqlite_nome)

            if os.path.exists(self.detrans_sqlite_nome + '.gz'):
                os.remove(self.detrans_sqlite_nome + '.gz')

            conn = sqlite3.connect(self.detrans_sqlite_nome)
            cursor = conn.cursor()

            cria_db.criar(conn, cursor)

            data_versao_bd = datetime.now()

            if self.stopthread.isSet():
                raise ValueError('Geração detrans.sqlite cancelada, parada ao criar banco sqlite')

            categoria.importa(conn, cursor, self.stopthread)
            cor.importa(conn, cursor, self.stopthread)
            especie.importa(conn, cursor, self.stopthread)
            lei.importa(conn, cursor, self.stopthread)
            tipo_infracao.importa(conn, cursor, self.stopthread)
            tipo_veiculo.importa(conn, cursor, self.stopthread)
            uf_cidade.importa(conn, cursor, self.stopthread)
            modelo.importa(conn, cursor, self.stopthread)
            veiculo.importa(conn, cursor, self.stopthread)
            agente.importa(conn, cursor, self.stopthread)
            config_sinc.importa(conn, cursor, data_versao_bd, self.stopthread)
            comprimir.comprimir_detrans_sqlite(self.detrans_sqlite_nome)

            self.is_finalisado = True
            self.is_erro_processo = False
            self.is_cancelado = False

        except Exception as ex:
            print ex
            self.is_finalisado = True
            self.is_erro_processo = True
        finally:
            self.is_finalisado = True

    def stop(self):
        self.is_finalisado = False
        self.is_cancelado = True
        self.stopthread.set()

    def get_status_str(self):

        if self.is_cancelado:
            return 'Cancelado'

        if self.is_finalisado:
            return 'Concluído'

        return 'Processando'


myProcess = None


class CriaSqliteView(View):
    template = 'detrans_sqlite/cria_sqlite.html'

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        global myProcess

        myProcess = ThreadDetransSqlite('importa')
        myProcess.start()

        return redirect('status-sqlite')


class StatusView(View):
    template = 'detrans_sqlite/status_sqlite.html'

    def get(self, request):
        global myProcess

        status = myProcess.get_status_str()
        erro = myProcess.is_erro_processo

        return render(request, self.template, {'status': status, 'erro': erro})

    def post(self, request):
        global myProcess

        myProcess.stop()

        return redirect('cria-sqlite')
