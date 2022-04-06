import sys

import cx_Oracle
from PyQt5 import Qt, QtCore
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QFileDialog, QLabel, QApplication
from PyQt5.QtWidgets import QMainWindow


class App(QMainWindow, QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Tema de casa - BD'
        self.left = 150
        self.top = 150
        self.width = 1020
        self.height = 775

        self.nume_client = 'NONE'
        self.prenume_client = 'NONE'

        self.denumire_parfum = 'NONE'
        self.tip_parfum = 'NONE'
        self.pret_parfum = 'NONE'
        self.id_marca = 'NONE'
        self.id_cantitate = 'NONE'
        self.id_miros = 'NONE'

        self.id_client = 'NONE'
        self.data_comanda = 'NONE'

        self.id_client_cont = 'NONE'
        self.cnp = 'NONE'
        self.sold = 'NONE'

        self.id_comanda = 'NONE'
        self.id_client_istoric = 'NONE'
        self.nr_produse = 'NONE'
        self.id_parfum = 'NONE'

        self.identificator = 'NONE'
        self.atribut = 'NONE'
        self.valoare = 'NONE'
        self.tabel = 'NONE'
        self.valoare_identificator = 'NONE'

        self.delete_identificator = 'NONE'
        self.delete_val_identificator = 'NONE'
        self.delete_tabel = 'NONE'

        self.initUI()

    def run(self):
        try:
            cx_Oracle.init_oracle_client(lib_dir=r"D:\Facultate\ANUL 3\SEM 1\BD\SQL Plus\instantclient_21_3")

            self.connection = cx_Oracle.connect(
                user="system",
                password="marco",
                dsn="localhost/xepdb1")

            print("Successfully connected to Oracle Database")
        except cx_Oracle.Error as e:
            print("Problema...pornire program/" + str(e))
            self.label_select.setText("Problema...pornire program/" + str(e))
        except:
            print("Problema la pornirea program")
            self.label_select.setText("Problema la pornirea program")

    def print_clienti(self):
        try:
            self.cursor = self.connection.cursor()
            self.show_text_clienti = ""

            for row in self.cursor.execute('select * from clienti'):
                self.show_text_clienti = self.show_text_clienti + str(row[0]) + ' - ' + str(row[1]) + ' - ' + str(
                    row[2]) + '\n'
            self.label_select.setText('ID CLIENT / NUME CLIENT / PRENUME CLIENT' + '\n' + self.show_text_clienti)
        except cx_Oracle.Error as e:
            print('Problema..afisare clienti/' + str(e))
            self.label_select.setText('Problema..afisare clienti/' + str(e))
        except:
            print("Problema..afisare clienti")
            self.label_select.setText("Problema..afisare clienti")

    def print_parfum(self):
        try:
            self.cursor = self.connection.cursor()
            self.show_text_clienti = ""

            for row in self.cursor.execute('select * from parfum'):
                self.show_text_clienti = self.show_text_clienti + str(row[0]) + ' - ' + str(row[1]) + ' - ' + str(
                    row[2]) + ' - ' + str(row[3]) + ' - ' + str(row[4]) + ' - ' + str(row[5]) + ' - ' + str(
                    row[6]) + '\n'

            self.label_select.setText(
                'ID PARFUM / DENUMIRE PARFUM / TIP PARFUM / PRET PARFUM / ID MARCA / ID CANTITATE / ID MIROS' + '\n' + self.show_text_clienti)
        except cx_Oracle.Error as e:
            print('Problema..afisare parfum/' + str(e))
            self.label_select.setText('Problema..afisare parfum/' + str(e))
        except:
            print('Problema...afisare parfum')
            self.label_select.setText('Problema..afisare parfum')

    def print_comanda(self):
        try:
            self.cursor = self.connection.cursor()
            self.show_text_clienti = ""

            for row in self.cursor.execute('select * from comanda'):
                self.show_text_clienti = self.show_text_clienti + str(row[0]) + ' - ' + str(row[1]) + ' - ' + str(
                    row[2]) + '\n'

            self.label_select.setText('ID COMANDA / ID CLIENT / DATA COMANDA' + '\n' + self.show_text_clienti)
        except cx_Oracle.Error as e:
            print('Problema..afisare comanda/' + str(e))
            self.label_select.setText('Problema..afisare comanda/' + str(e))
        except:
            print('Problema...afisare comanda')
            self.label_select.setText('Problema..afisare comanda')

    def print_cont_client(self):
        try:
            self.cursor = self.connection.cursor()
            self.show_text_clienti = ""

            for row in self.cursor.execute('select * from cont_client'):
                self.show_text_clienti = self.show_text_clienti + str(row[0]) + ' - ' + str(row[1]) + ' - ' + str(
                    row[2]) + ' - ' + str(row[3]) + '\n'

            self.label_select.setText('ID CLIENT / CNP / SOLD / ORAS CLIENT' + '\n' + self.show_text_clienti)
        except cx_Oracle.Error as e:
            print('Problema..afisare cont client/' + str(e))
            self.label_select.setText('Problema..afisare cont client/' + str(e))
        except:
            print('Problema...afisare cont client')
            self.label_select.setText('Problema...afisare cont client')

    def print_istoric_comenzi(self):
        try:
            self.cursor = self.connection.cursor()
            self.show_text_clienti = ""

            for row in self.cursor.execute('select * from istoric_comenzi'):
                self.show_text_clienti = self.show_text_clienti + str(row[0]) + ' - ' + str(row[1]) + ' - ' + str(
                    row[2]) + ' - ' + str(row[3]) + '\n'

            self.label_select.setText('ID COMANDA / ID CLIENT / ID PARFUM / NR PRODUSE' + '\n' + self.show_text_clienti)
        except cx_Oracle.Error as e:
            print('Problema..afisare istoric comenzi/' + str(e))
            self.label_select.setText('Problema..afisare istoric comenzi/' + str(e))
        except:
            print("Problema...afisare istoric comenzi")
            self.label_select.setText("Problema...afisare istoric comenzi")

    def print_miros(self):
        try:
            self.cursor = self.connection.cursor()
            self.show_text_clienti = ""

            for row in self.cursor.execute('select * from miros'):
                self.show_text_clienti = self.show_text_clienti + str(row[0]) + ' - ' + str(row[1]) + '\n'

            self.label_select.setText(' ID MIROS / DENUMIRE MIROS' + '\n' + self.show_text_clienti)
        except cx_Oracle.Error as e:
            print('Problema..afisare miros/' + str(e))
            self.label_select.setText('Problema..afisare miros/' + str(e))
        except:
            print("Problema...afisare miros")
            self.label_select.setText("Problema...afisare miros")

    def print_cantitate(self):
        try:
            self.cursor = self.connection.cursor()
            self.show_text_clienti = ""

            for row in self.cursor.execute('select * from cantitate'):
                self.show_text_clienti = self.show_text_clienti + str(row[0]) + ' - ' + str(row[1]) + '\n'

            self.label_select.setText(' ID CANTITATE / CANTITATE ML' + '\n' + self.show_text_clienti)
        except cx_Oracle.Error as e:
            print('Problema..afisare cantitate/' + str(e))
            self.label_select.setText('Problema..afisare cantitate/' + str(e))
        except:
            print("Problema...afisare cantitate")
            self.label_select.setText('Problema..afisare cantitate')

    def print_marca(self):
        try:
            self.cursor = self.connection.cursor()
            self.show_text_clienti = ""

            for row in self.cursor.execute('select * from marca'):
                self.show_text_clienti = self.show_text_clienti + str(row[0]) + ' - ' + str(row[1]) + '\n'

            self.label_select.setText(' ID MARCA / NUME MARCA ' + '\n' + self.show_text_clienti)
        except cx_Oracle.Error as e:
            print('Problema..afisare marca/' + str(e))
            self.label_select.setText('Problema..afisare marca/' + str(e))
        except:
            print("Problema...afisare marca")
            self.label_select.setText("Problema...afisare marca")

    def insert_client(self):
        try:
            self.nume_client = self.textbox_nume_client.text()
            self.prenume_client = self.textbox_prenume_client.text()

            self.cursor = self.connection.cursor()
            if self.nume_client != 'NONE' and self.prenume_client != 'NONE':
                self.cursor.execute(
                    'insert into clienti (nume_client,prenume_client) values (\'' + str(
                        self.nume_client) + '\',\'' + str(
                        self.prenume_client) + '\')')
            else:
                print('Problema insert_client - Valori de NONE')
                self.label_select.setText('Problema insert_client - Valori de NONE')

            self.connection.commit()
        except cx_Oracle.Error as e:
            print('Problema..inserare clienti/' + str(e))
            self.label_select.setText('Problema..inserare clienti/' + str(e))
        except:
            print("Problema...inserare clienti")
            self.label_select.setText("Problema...inserare clienti")

    def insert_parfum(self):

        try:
            self.denumire_parfum = self.textbox_denumire_parfum.text()
            self.tip_parfum = self.textbox_tip_parfum.text()
            self.pret_parfum = self.textbox_pret_parfum.text()
            self.id_marca = self.textbox_id_marca.text()
            self.id_cantitate = self.textbox_id_cantitate.text()
            self.id_miros = self.textbox_id_miros.text()

            self.cursor = self.connection.cursor()
            if self.denumire_parfum != 'NONE' and \
                    self.tip_parfum != 'NONE' and \
                    self.pret_parfum != 'NONE' and \
                    self.id_marca != 'NONE' and \
                    self.id_cantitate != 'NONE' and \
                    self.id_miros != 'NONE':
                self.cursor.execute(
                    'insert into parfum (denumire_parfum,tip_parfum,pret_parfum,marca_id_marca,cantitate_id_cantitate,miros_id_miros) values (\'' + str(
                        self.denumire_parfum) + '\',\'' + str(self.tip_parfum) + '\',\'' + str(
                        self.pret_parfum) + '\',\'' + str(self.id_marca) + '\',\'' + str(
                        self.id_cantitate) + '\',\'' + str(
                        self.id_miros) + '\')')
            else:
                print('Problema insert_parfum valori NONE')
                self.label_select.setText('Problema insert_parfum valori NONE')
            self.connection.commit()
        except cx_Oracle.Error as e:
            print('Problema..inserare parfum/' + str(e))
            self.label_select.setText('Problema..inserare parfum/' + str(e))
        except:
            print("Problema...inserare parfum")
            self.label_select.setText("Problema...inserare parfum")

    def insert_comanda(self):
        try:
            self.id_client = self.textbox_id_client.text()
            self.data_comanda = self.textbox_data_comanda.text()
            id_client_int = int(self.id_client)
            self.cursor = self.connection.cursor()
            comma = "'"
            if self.id_client != 'NONE' and self.data_comanda != 'NONE':
                print(self.id_client + ' - ' + self.data_comanda + 'spatiu' + comma)
                sql = """ INSERT INTO comanda (clienti_id_client,data_comanda) VALUES ('{}',to_date('{}','dd.mm.yyyy'))""".format(
                    self.id_client, self.data_comanda)
                self.cursor.execute(sql)
            else:
                print('Problema insert_comanda - VALORI NONE')
                self.label_select.setText('Problema insert_comanda - VALORI NONE')

            self.connection.commit()
        except cx_Oracle.Error as e:
            print('Problema..inserare comanda/' + str(e))
            self.label_select.setText('Problema..inserare comanda/' + str(e))

        except:
            print("Problema...inserare comanda")
            self.label_select.setText("Problema...inserare comanda")

    def insert_cont(self):
        try:
            self.id_client_cont = self.textbox_id_client_cont.text()
            self.cnp = self.textbox_cnp.text()
            self.sold = self.textbox_sold.text()

            self.cursor = self.connection.cursor()
            if self.id_client_cont != 'NONE' and \
                    self.cnp != 'NONE' and \
                    self.sold != 'NONE':
                self.cursor.execute(
                    'insert into cont_client (clienti_id_client,cnp,sold) values (\'' + str(
                        self.id_client_cont) + '\',\'' + str(self.cnp) + '\',\'' + str(
                        self.sold) + '\')')
            else:
                print('Problema insert_cont - VALORI NONE')
                self.label_select.setText('Problema insert_cont - VALORI NONE')

            self.connection.commit()

        except cx_Oracle.Error as e:
            print('Problema..inserare cont client/' + str(e))
            self.label_select.setText('Problema..inserare cont client/' + str(e))

        except:
            print("Problema...inserare cont client ")
            self.label_select.setText("Problema...inserare cont client ")

    def insert_istoric(self):
        try:
            self.id_comanda = self.textbox_id_comanda.text()
            self.id_client_istoric = self.textbox_id_client_istoric.text()
            self.id_parfum = self.textbox_id_parfum.text()
            self.nr_produse = self.textbox_nr_produse.text()

            self.cursor = self.connection.cursor()
            if self.id_comanda != 'NONE' and \
                    self.id_client_istoric != 'NONE' and \
                    self.id_parfum != 'NONE' and \
                    self.nr_produse != 'NONE':
                self.cursor.execute(
                    'insert into istoric_comenzi  (comanda_id_comanda,comanda_id_client,parfum_id_parfum,nr_produse) values (\'' + str(
                        self.id_comanda) + '\',\'' + str(self.id_client_istoric) + '\',\'' + str(
                        self.id_parfum) + '\',\'' + str(self.nr_produse) + '\')')
            else:
                print('Problema insert_istoric - VALORI NONE')
                self.label_select.setText('Problema insert_istoric - VALORI NONE')

            self.connection.commit()

        except cx_Oracle.Error as e:
            print('Problema..inserare istoric comenzi/' + str(e))
            self.label_select.setText('Problema..inserare istoric comenzi/' + str(e))

        except:
            print("Problema...inserare istoric comenzi ")
            self.label_select.setText("Problema...inserare istoric comenzi ")

    def insert_miros(self):
        try:
            self.denumire_miros = self.textbox_denumire_miros.text()

            self.cursor = self.connection.cursor()
            if self.denumire_miros != 'NONE':
                self.cursor.execute('insert into miros (denumire_miros) values (\'' + str(self.denumire_miros) + '\')')
            else:
                print('Problema insert_miros - VALORI NONE')
                self.label_select.setText('Problema insert_miros - VALORI NONE')

            self.connection.commit()

        except cx_Oracle.Error as e:
            print('Problema..inserare miros/' + str(e))
            self.label_select.setText('Problema..inserare miros/' + str(e))

        except:
            print("Problema...inserare miros ")
            self.label_select.setText("Problema...inserare miros ")

    def insert_marca(self):
        try:
            self.nume_marca = self.textbox_nume_marca.text()

            self.cursor = self.connection.cursor()
            if self.nume_marca != 'NONE':
                self.cursor.execute('insert into marca (nume_marca) values (\'' + str(self.nume_marca) + '\')')
            else:
                print('Problema insert_marca - VALORI NONE')
                self.label_select.setText('Problema insert_marca - VALORI NONE')

            self.connection.commit()
        except cx_Oracle.Error as e:
            print('Problema..inserare marca/' + str(e))
            self.label_select.setText('Problema..inserare marca/' + str(e))

        except:
            print("Problema...inserare marca ")
            self.label_select.setText("Problema...inserare marca ")

    def edit(self):
        try:
            self.tabel = self.textbox_edit_tabel.text()
            self.atribut = self.textbox_edit_atribut.text()
            self.valoare = self.textbox_edit_valoare.text()
            self.identificator = self.textbox_edit_identificator.text()
            self.valoare_identificator = self.textbox_edit_val_identificator.text()

            self.cursor = self.connection.cursor()

            sql = """UPDATE {} SET {} = '{}' WHERE {} = {}""".format(self.tabel, self.atribut, self.valoare,
                                                                     self.identificator, self.valoare_identificator)

            if self.tabel != 'NONE' and self.atribut != 'NONE' and self.valoare != 'NONE' and self.identificator != 'NONE':
                self.cursor.execute(sql)
                self.connection.commit()

            else:
                print("problema edit... - VALORI NONE")
                self.label_select.setText("problema edit... - VALORI NONE")

        except cx_Oracle.Error as e:
            print('Problema..editare/' + str(e))
            self.label_select.setText('Problema..editare/' + str(e))

        except:
            print("Problema...editare ")
            self.label_select.setText("Problema...editare ")

    def stergere(self):
        try:
            self.delete_tabel = self.textbox_delete_tabel.text()
            self.delete_identificator = self.textbox_delete_identificator.text()
            self.delete_val_identificator = self.textbox_delete_val_identificator.text()

            self.cursor = self.connection.cursor()

            sql = """DELETE FROM {} WHERE {} = '{}'""".format(self.delete_tabel, self.delete_identificator,
                                                              self.delete_val_identificator)
            if self.delete_tabel != 'NONE' and self.delete_identificator != 'NONE' and self.delete_val_identificator != 'NONE':
                self.cursor.execute(sql)
                self.connection.commit()

            else:
                print("problema delete... - VALORI NONE")
                self.label_select.setText("problema delete... - VALORI NONE")

        except cx_Oracle.Error as e:
            print('Problema..stergere/' + str(e))
            self.label_select.setText('Problema..stergere/' + str(e))

        except:
            print("Problema...stergere")
            self.label_select.setText("Problema...stergere")

    def detalii_parfum(self):
        try:
            self.cursor = self.connection.cursor()
            self.show_text_clienti = ""

            for row in self.cursor.execute(
                    'select p.id_parfum,p.denumire_parfum,p.tip_parfum,p.pret_parfum,m.nume_marca,c.cantitate_ml,s.denumire_miros from parfum p,marca m, cantitate c,miros s where p.marca_id_marca = m.id_marca and p.cantitate_id_cantitate = c.id_cantitate and p.miros_id_miros = s.id_miros'):
                self.show_text_clienti = self.show_text_clienti + str(row[0]) + ' - ' + str(row[1]) + ' - ' + str(
                    row[2]) + ' - ' + str(row[3]) + ' - ' + str(row[4]) + ' - ' + str(row[5]) + ' - ' + str(
                    row[6]) + '\n'

            self.label_select.setText(self.show_text_clienti)
        except cx_Oracle.Error as e:
            print('Problema..detalii parfum/' + str(e))
            self.label_select.setText('Problema..detalii parfum/' + str(e))
        except:
            print('Problema...detalii parfum')
            self.label_select.setText('Problema..detalii parfum')

    def detalii_comanda(self):
        try:
            self.cursor = self.connection.cursor()
            self.show_text_clienti = ""

            for row in self.cursor.execute(
                    'select c.id_comanda,cl.nume_client , cl.prenume_client, c.data_comanda from comanda c,clienti cl where c.clienti_id_client = cl.id_client'):
                self.show_text_clienti = self.show_text_clienti + str(row[0]) + ' - ' + str(row[1]) + ' - ' + str(
                    row[2]) + ' - ' + str(row[3]) + '\n'

            self.label_select.setText(self.show_text_clienti)
        except cx_Oracle.Error as e:
            print('Problema..detalii comenzi/' + str(e))
            self.label_select.setText('Problema..detalii comenzi/' + str(e))
        except:
            print('Problema...detalii comenzi')
            self.label_select.setText('Problema..detalii comenzi')

    def detalii_cheltuieli(self):
        try:
            self.cursor = self.connection.cursor()
            self.show_text_clienti = ""

            for row in self.cursor.execute(
                    'select comanda_id_comanda ,comanda_id_client,clienti.nume_client, sum(parfum.pret_parfum*nr_produse) "Total cheltuit"  from istoric_comenzi ,parfum,clienti where parfum.id_parfum = parfum_id_parfum and comanda_id_client = clienti.id_client group by comanda_id_comanda,comanda_id_client,clienti.nume_client'):
                self.show_text_clienti = self.show_text_clienti + str(row[0]) + ' - ' + str(row[1]) + ' - ' + str(
                    row[2]) + ' - ' + str(row[3]) + '\n'
            self.label_select.setText(
                'ID COMANDA / ID CLIENT / NUME CLIENT / SUMA CHELTUITA \n' + self.show_text_clienti)
        except cx_Oracle.Error as e:
            print('Problema..detalii cheltuieli/' + str(e))
            self.label_select.setText('Problema..detalii cheltuieli/' + str(e))
        except:
            print("Problema...detalii cheltuieli")
            self.label_select.setText("Problema...detalii cheltuieli")

    def detalii_numar_produse(self):
        try:
            self.cursor = self.connection.cursor()
            self.show_text_clienti = ""

            for row in self.cursor.execute(
                    'select clienti.nume_client , parfum.denumire_parfum,count(*)  "Numar parfumuri comandate" from clienti,parfum,istoric_comenzi where clienti.id_client = comanda_id_client and parfum.id_parfum = parfum_id_parfum group by clienti.nume_client , parfum.denumire_parfum'):
                self.show_text_clienti = self.show_text_clienti + str(row[0]) + ' - ' + str(row[1]) + ' - ' + str(
                    row[2]) + '\n'
            self.label_select.setText(self.show_text_clienti)
        except cx_Oracle.Error as e:
            print('Problema..detalii numar produse/' + str(e))
            self.label_select.setText('Problema..detalii numar produse/' + str(e))
        except:
            print("Problema...detalii numar produse")
            self.label_select.setText("Problema...detalii numar produse")

    def detalii_clienti(self):
        try:
            self.cursor = self.connection.cursor()
            self.show_text_clienti = ""

            for row in self.cursor.execute(
                    'select clienti.nume_client,clienti.prenume_client , cont_client.cnp,cont_client.sold from clienti,cont_client where clienti.id_client = cont_client.clienti_id_client'):
                self.show_text_clienti = self.show_text_clienti + str(row[0]) + ' - ' + str(row[1]) + ' - ' + str(
                    row[2]) + ' - ' + str(row[3]) + '\n'
            self.label_select.setText(self.show_text_clienti)
        except cx_Oracle.Error as e:
            print('Problema..detalii clienti/' + str(e))
            self.label_select.setText('Problema..detalii clienti/' + str(e))
        except:
            print("Problema...detalii clienti")
            self.label_select.setText("Problema...detalii clienti")

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.show_text_clienti = ''

        # Textboxs

        self.textbox_nume_client = QLineEdit(self)
        self.textbox_nume_client.move(20, 550)
        self.textbox_nume_client.resize(50, 25)
        self.textbox_nume_client.setText("NONE")

        self.textbox_prenume_client = QLineEdit(self)
        self.textbox_prenume_client.move(80, 550)
        self.textbox_prenume_client.resize(50, 25)
        self.textbox_prenume_client.setText("NONE")

        self.textbox_denumire_parfum = QLineEdit(self)
        self.textbox_denumire_parfum.move(20, 580)
        self.textbox_denumire_parfum.resize(50, 25)
        self.textbox_denumire_parfum.setText("NONE")

        self.textbox_tip_parfum = QLineEdit(self)
        self.textbox_tip_parfum.move(80, 580)
        self.textbox_tip_parfum.resize(50, 25)
        self.textbox_tip_parfum.setText("NONE")

        self.textbox_pret_parfum = QLineEdit(self)
        self.textbox_pret_parfum.move(140, 580)
        self.textbox_pret_parfum.resize(50, 25)
        self.textbox_pret_parfum.setText("NONE")

        self.textbox_id_marca = QLineEdit(self)
        self.textbox_id_marca.move(200, 580)
        self.textbox_id_marca.resize(50, 25)
        self.textbox_id_marca.setText("NONE")

        self.textbox_id_cantitate = QLineEdit(self)
        self.textbox_id_cantitate.move(260, 580)
        self.textbox_id_cantitate.resize(50, 25)
        self.textbox_id_cantitate.setText("NONE")

        self.textbox_id_miros = QLineEdit(self)
        self.textbox_id_miros.move(320, 580)
        self.textbox_id_miros.resize(50, 25)
        self.textbox_id_miros.setText("NONE")

        self.textbox_id_client = QLineEdit(self)
        self.textbox_id_client.move(20, 610)
        self.textbox_id_client.resize(50, 25)
        self.textbox_id_client.setText("NONE")

        self.textbox_data_comanda = QLineEdit(self)
        self.textbox_data_comanda.move(80, 610)
        self.textbox_data_comanda.resize(50, 25)
        self.textbox_data_comanda.setText("NONE")

        self.textbox_id_client_cont = QLineEdit(self)
        self.textbox_id_client_cont.move(20, 640)
        self.textbox_id_client_cont.resize(50, 25)
        self.textbox_id_client_cont.setText("NONE")

        self.textbox_cnp = QLineEdit(self)
        self.textbox_cnp.move(80, 640)
        self.textbox_cnp.resize(50, 25)
        self.textbox_cnp.setText("NONE")

        self.textbox_sold = QLineEdit(self)
        self.textbox_sold.move(140, 640)
        self.textbox_sold.resize(50, 25)
        self.textbox_sold.setText("NONE")

        self.textbox_id_comanda = QLineEdit(self)
        self.textbox_id_comanda.move(20, 670)
        self.textbox_id_comanda.resize(50, 25)
        self.textbox_id_comanda.setText("NONE")

        self.textbox_id_client_istoric = QLineEdit(self)
        self.textbox_id_client_istoric.move(80, 670)
        self.textbox_id_client_istoric.resize(50, 25)
        self.textbox_id_client_istoric.setText("NONE")

        self.textbox_id_parfum = QLineEdit(self)
        self.textbox_id_parfum.move(140, 670)
        self.textbox_id_parfum.resize(50, 25)
        self.textbox_id_parfum.setText("NONE")

        self.textbox_nr_produse = QLineEdit(self)
        self.textbox_nr_produse.move(200, 670)
        self.textbox_nr_produse.resize(50, 25)
        self.textbox_nr_produse.setText("NONE")

        self.textbox_denumire_miros = QLineEdit(self)
        self.textbox_denumire_miros.move(20, 700)
        self.textbox_denumire_miros.resize(50, 25)
        self.textbox_denumire_miros.setText("NONE")

        self.textbox_nume_marca = QLineEdit(self)
        self.textbox_nume_marca.move(20, 730)
        self.textbox_nume_marca.resize(50, 25)
        self.textbox_nume_marca.setText("NONE")

        self.textbox_edit_identificator = QLineEdit(self)
        self.textbox_edit_identificator.move(550, 550)
        self.textbox_edit_identificator.resize(50, 25)
        self.textbox_edit_identificator.setText("NONE")

        self.textbox_edit_val_identificator = QLineEdit(self)
        self.textbox_edit_val_identificator.move(620, 550)
        self.textbox_edit_val_identificator.resize(50, 25)
        self.textbox_edit_val_identificator.setText("NONE")

        self.textbox_edit_atribut = QLineEdit(self)
        self.textbox_edit_atribut.move(690, 550)
        self.textbox_edit_atribut.resize(50, 25)
        self.textbox_edit_atribut.setText("NONE")

        self.textbox_edit_valoare = QLineEdit(self)
        self.textbox_edit_valoare.move(760, 550)
        self.textbox_edit_valoare.resize(50, 25)
        self.textbox_edit_valoare.setText("NONE")

        self.textbox_edit_tabel = QLineEdit(self)
        self.textbox_edit_tabel.move(830, 550)
        self.textbox_edit_tabel.resize(50, 25)
        self.textbox_edit_tabel.setText("NONE")

        self.textbox_delete_identificator = QLineEdit(self)
        self.textbox_delete_identificator.move(550, 610)
        self.textbox_delete_identificator.resize(50, 25)
        self.textbox_delete_identificator.setText("NONE")

        self.textbox_delete_val_identificator = QLineEdit(self)
        self.textbox_delete_val_identificator.move(620, 610)
        self.textbox_delete_val_identificator.resize(50, 25)
        self.textbox_delete_val_identificator.setText("NONE")

        self.textbox_delete_tabel = QLineEdit(self)
        self.textbox_delete_tabel.move(690, 610)
        self.textbox_delete_tabel.resize(50, 25)
        self.textbox_delete_tabel.setText("NONE")

        # COMANDA_ID_COMANDA COMANDA_ID_CLIENT PARFUM_ID_PARFUM NR_PRODUSE
        # self.textbox_addr_sender.text()

        # Buttons

        button_print_clienti = QPushButton('Print Clienti', self)
        button_print_clienti.setToolTip('Print clienti')
        button_print_clienti.move(700, 40)
        button_print_clienti.clicked.connect(self.print_clienti)

        button_print_parfum = QPushButton('Print Parfum', self)
        button_print_parfum.setToolTip('Print parfum')
        button_print_parfum.move(700, 65)
        button_print_parfum.clicked.connect(self.print_parfum)

        button_print_comanda = QPushButton('Print Comanda', self)
        button_print_comanda.setToolTip('Print comanda')
        button_print_comanda.move(700, 90)
        button_print_comanda.clicked.connect(self.print_comanda)

        button_print_cont = QPushButton('Print Cont Client', self)
        button_print_cont.setToolTip('Print Cont Client')
        button_print_cont.move(700, 115)
        button_print_cont.clicked.connect(self.print_cont_client)

        button_print_istoric = QPushButton('Print Istoric', self)
        button_print_istoric.setToolTip('Print Istoric')
        button_print_istoric.move(700, 140)
        button_print_istoric.clicked.connect(self.print_istoric_comenzi)

        button_print_miros = QPushButton('Print Miros', self)
        button_print_miros.setToolTip('Print Miros')
        button_print_miros.move(700, 165)
        button_print_miros.clicked.connect(self.print_miros)

        button_print_cantitate = QPushButton('Print Cantitate', self)
        button_print_cantitate.setToolTip('Print Cantitate')
        button_print_cantitate.move(700, 190)
        button_print_cantitate.clicked.connect(self.print_cantitate)

        button_print_marca = QPushButton('Print Marca', self)
        button_print_marca.setToolTip('Print Marca')
        button_print_marca.move(700, 215)
        button_print_marca.clicked.connect(self.print_marca)

        button_insert_client = QPushButton('Insert Client', self)
        button_insert_client.setToolTip('Insert Client')
        button_insert_client.move(380, 550)
        button_insert_client.clicked.connect(self.insert_client)

        button_insert_parfum = QPushButton('Insert Parfum', self)
        button_insert_parfum.setToolTip('Insert Parfum')
        button_insert_parfum.move(380, 580)
        button_insert_parfum.clicked.connect(self.insert_parfum)

        button_insert_comanda = QPushButton('Insert Comanda', self)
        button_insert_comanda.setToolTip('Insert Comanda')
        button_insert_comanda.move(380, 610)
        button_insert_comanda.clicked.connect(self.insert_comanda)

        button_insert_comanda = QPushButton('Insert Cont ', self)
        button_insert_comanda.setToolTip('Insert Cont ')
        button_insert_comanda.move(380, 640)
        button_insert_comanda.clicked.connect(self.insert_cont)

        button_insert_istoric = QPushButton('Insert Istoric', self)
        button_insert_istoric.setToolTip('Insert Istoric')
        button_insert_istoric.move(380, 670)
        button_insert_istoric.clicked.connect(self.insert_istoric)

        button_insert_miros = QPushButton('Insert Miros', self)
        button_insert_miros.setToolTip('Insert Miros')
        button_insert_miros.move(80, 700)
        button_insert_miros.clicked.connect(self.insert_miros)

        button_insert_marca = QPushButton('Insert Marca', self)
        button_insert_marca.setToolTip('Insert Marca')
        button_insert_marca.move(80, 730)
        button_insert_marca.clicked.connect(self.insert_marca)

        button_edit = QPushButton('Confirm Edit', self)
        button_edit.setToolTip('Confirm Edit')
        button_edit.move(900, 550)
        button_edit.clicked.connect(self.edit)

        button_delete = QPushButton('Confirm Delete', self)
        button_delete.setToolTip('Confirm Delete')
        button_delete.move(760, 610)
        button_delete.clicked.connect(self.stergere)

        button_run = QPushButton('Run', self)
        button_run.setToolTip('RUN BUTTON')
        button_run.move(700, 240)
        button_run.clicked.connect(self.run)

        button_detalii_parfum = QPushButton('Detalii Parfum', self)
        button_detalii_parfum.setToolTip('Detalii Parfum')
        button_detalii_parfum.move(830, 40)
        button_detalii_parfum.clicked.connect(self.detalii_parfum)

        button_detalii_comanda = QPushButton('Detalii Comenzi', self)
        button_detalii_comanda.setToolTip('Detalii Comenzi')
        button_detalii_comanda.move(830, 65)
        button_detalii_comanda.clicked.connect(self.detalii_comanda)

        button_detalii_cheltuieli = QPushButton('Detalii Cheltuieli', self)
        button_detalii_cheltuieli.setToolTip('Detalii Cheltuieli')
        button_detalii_cheltuieli.move(830, 90)
        button_detalii_cheltuieli.clicked.connect(self.detalii_cheltuieli)

        button_detalii_numar_produse = QPushButton('Numar Produse', self)
        button_detalii_numar_produse.setToolTip('Numar Produse')
        button_detalii_numar_produse.move(830, 115)
        button_detalii_numar_produse.clicked.connect(self.detalii_numar_produse)

        button_detalii_numar_produse = QPushButton('Detalii Clienti', self)
        button_detalii_numar_produse.setToolTip('Detalii Clienti')
        button_detalii_numar_produse.move(830, 140)
        button_detalii_numar_produse.clicked.connect(self.detalii_clienti)


        self.label_select = QLabel(self)
        self.label_select.move(10, 20)
        self.label_select.resize(650, 500)
        self.label_select.setText("Welcome :)")
        self.label_select.setAlignment(QtCore.Qt.AlignCenter)

        self.label_edit = QLabel(self)
        self.label_edit.move(550, 530)
        self.label_edit.resize(450, 25)
        self.label_edit.setText("identificator / valoare identificator / atribut / valoare noua / tabel")

        self.label_delete = QLabel(self)
        self.label_delete.move(550, 590)
        self.label_delete.resize(250, 25)
        self.label_delete.setText("identificator / valoare identificator / tabel")

        self.show()


if __name__ == '__main__':
    app = QApplication([])
    ex = App()
    sys.exit(app.exec_())
