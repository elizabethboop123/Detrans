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
        self.progress = 0
        self.detrans_sqlite_nome = settings.MEDIA_ROOT + '/detrans.sqlite'
        self.detrans_sqlite_nome_execucao = settings.MEDIA_ROOT + '/detrans_execucao.sqlite'

    def run(self):

        try:

            self.progress = 1
            if os.path.exists(self.detrans_sqlite_nome_execucao):
                os.remove(self.detrans_sqlite_nome_execucao)

            self.progress = 1
            if os.path.exists(self.detrans_sqlite_nome_execucao + '.gz'):
                os.remove(self.detrans_sqlite_nome_execucao + '.gz')

            self.progress = 2
            conn = sqlite3.connect(self.detrans_sqlite_nome_execucao)
            cursor = conn.cursor()

            self.progress = 3
            cria_db.criar(conn, cursor)

            self.progress = 4
            data_versao_bd = datetime.now()

            self.progress = 5
            if self.stopthread.isSet():
                raise ValueError('Geração detrans.sqlite cancelada, parada ao criar banco sqlite')

            self.progress = 6
            categoria.importa(conn, cursor, self.stopthread)
            self.progress = 8
            cor.importa(conn, cursor, self.stopthread)
            self.progress = 16
            especie.importa(conn, cursor, self.stopthread)
            self.progress = 24
            lei.importa(conn, cursor, self.stopthread)
            self.progress = 32
            tipo_infracao.importa(conn, cursor, self.stopthread)
            self.progress = 40
            tipo_veiculo.importa(conn, cursor, self.stopthread)
            self.progress = 48
            uf_cidade.importa(conn, cursor, self.stopthread)
            self.progress = 56
            modelo.importa(conn, cursor, self.stopthread)
            self.progress = 64
            veiculo.importa(conn, cursor, self.stopthread)
            self.progress = 72
            agente.importa(conn, cursor, self.stopthread)
            self.progress = 80
            config_sinc.importa(conn, cursor, data_versao_bd, self.stopthread)
            self.progress = 90
            comprimir.comprimir_detrans_sqlite(self.detrans_sqlite_nome_execucao)
            self.progress = 99

            self.progress = 100


            if os.path.exists(self.detrans_sqlite_nome):
                os.remove(self.detrans_sqlite_nome)
            
            if os.path.exists(self.detrans_sqlite_nome +".gz"):
                os.remove(self.detrans_sqlite_nome +".gz")
            
            if os.path.exists(self.detrans_sqlite_nome_execucao + ".gz"):
                os.rename(self.detrans_sqlite_nome_execucao + ".gz", self.detrans_sqlite_nome + ".gz")


            if os.path.exists(self.detrans_sqlite_nome_execucao):
                os.rename(self.detrans_sqlite_nome_execucao, self.detrans_sqlite_nome)

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
            return 'Concluido'

        return 'Processando'

    def get_status_mensagem_str(self):
        return self.progress


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

class CriaSqliteCanceladoView(View):
    template = 'detrans_sqlite/cria_sqlite_cancelado.html'

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
        status_mensagem = myProcess.get_status_mensagem_str()

        return render(request, self.template, {'status': status, 'erro': erro, 'status_mensagem': status_mensagem})

    def post(self, request):
        global myProcess

        myProcess.stop()

        return redirect('cria-sqlite-cancelado')