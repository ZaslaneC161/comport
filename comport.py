import sys
import serial.tools.list_ports
import serial
import threading
from find_crc16 import crc16
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import pyqtSlot
from choice import Ui_ChoiceWindow
from start import Ui_StartWindow
from status import Ui_StatusWindow
from arrowstat import Ui_ArrowStat
from setting import Ui_Setting


ser = None  # Объявляем переменную ser в глобальной области видимости
arr = [0] * 10050
############################################ поиск портов #######################################
def find_port():
    #com_ports = serial.tools.list_ports.comports()

    # Создаем список для хранения COM-портов в формате (comport.device, comport.description)
    #return[(f"{comport.device}, {comport.description}") for comport in com_ports]
    ports = list(serial.tools.list_ports.comports())
    port_list = []
    # Выводим информацию о каждом порте
    for port in ports:
        port_list.append(port.device)
    return port_list
################################################################################################
# Определение функции для записи данных в порт
def write_to_port(ser,data):

    temp = ser.write(data)
    if temp:
        print(f'Успешно записано {temp} байтов в COM-порт.')
    else:
        print('Ошибка записи в COM-порт.')
########################## функция определения отрицательного числа #############################

def min(a, b):
    y = a * 256 + b
    if a & 0x80:
        z = (~(y & 0x7fff) + 1) / 10
    else:
        z = y / 10
    return z
###################################################################################################

###################################### функция сканирования связи с контроллером #####################################

def scan_connect():
    global scan_count
    if scan_count > 10:
        connect_window.show()
        start_window.hide()

    else:
        start_window.show()
        connect_window.hide()


###################################################################################################################

######################################## функция чтения порта ##################################
def read_com_port(ser):
    while True:
        global arr
        date = ser.read(100)
        data = [date[0 + i] for i in range(len(date))]
        print(data)
        if len(data)>0:
            if data[0] == 1:
                print(data[1])
                if data[1] == 16:
                    print('второй байт: 16')
                    if crc16(data[0:data[6] + 7]) == data[(data[6] + 9) - 2] * 256 + data[(data[6] + 9) - 1]:
                        print('crc прошёл проверку!!!!!')
                        arr[(data[2]*256+data[3])*2:(data[2]*256+data[3])*2 + data[6]] = [data[7 + x] for x in range(data[6])]
                        arr1 = [data[0+x] for x in range(6)]
                        print(arr1)
                        arr1.extend([(crc16(arr1) // 256), (crc16(arr1) % 256)])
                        print(arr1)
                        write_to_port(ser, bytes(arr1))
                        print(arr)
                        if arr[10001] == 1:
                            start_window.update_label()
                        if arr[10001] == 2:
                            status_window.update_label()
                        if arr[10001] > 2 & arr[10001] < 7:
                            arrow_stat.update_label()
                if data[1] == 3:
                    print('второй байт: 3')
                    if crc16(data[0:6]) == data[6] * 256 + data[7]:
                        print('crc прошёл проверку!!!!!')
                        arr2 = [data[0+x] for x in range(8)]
                        print(arr2)
                        buff = [data[0], data[1], (data[4]*256 + data[5])*2, ]
                        buff1 = [arr[((data[2] * 256 + data[3])*2) + i] for i in range((data[4] * 256 + data[5]) * 2)]
                        buff.extend([buff1[0 + y] for y in range(len(buff1))])
                        print(buff)
                        buff.extend([(crc16(buff) // 256), (crc16(buff) % 256)])
                        write_to_port(ser, bytes(buff))
                        print(buff)



####################################################################################################################

#########################################  Окно Выбора COM порта ####################################################
class ChoiceWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ChoiceWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.connect_button_clicked)
        self.ui.comboBox.addItems(find_port())

    def connect_button_clicked(self):
        global reading_thread
        global arr
        global ser  # Используем глобальную переменную ser
        com_port = self.ui.comboBox.currentText()
        ser = serial.Serial(com_port, baudrate=9600, timeout=0.2, stopbits=1)
        # Открываем COM порт и запускаем чтение в отдельном потоке
        reading_thread = threading.Thread(target=read_com_port, args=(ser,), daemon=True)
        reading_thread.start()
        arr[10001] = 1
        print(f"screen №: {arr[10001]}")
        self.close()
        start_window.show()

###################################################################################################################

############################################### Окно Start ##########################################################
class StartWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_StartWindow()
        self.ui.setupUi(self)
        self.ui.statusButton.clicked.connect(self.open_status_window)
        self.ui.settingButton.clicked.connect(self.open_setting_window)

        self.ui.name_arrow1.mousePressEvent = self.open_arrstat_window1
        self.ui.stat_arrow1.mousePressEvent = self.open_arrstat_window1
        self.ui.t_arrow1.mousePressEvent = self.open_arrstat_window1
        self.ui.name_arrow2.mousePressEvent = self.open_arrstat_window2
        self.ui.stat_arrow2.mousePressEvent = self.open_arrstat_window2
        self.ui.t_arrow2.mousePressEvent = self.open_arrstat_window2
        self.ui.name_arrow3.mousePressEvent = self.open_arrstat_window3
        self.ui.stat_arrow3.mousePressEvent = self.open_arrstat_window3
        self.ui.t_arrow3.mousePressEvent = self.open_arrstat_window3
        self.ui.name_arrow4.mousePressEvent = self.open_arrstat_window4
        self.ui.stat_arrow4.mousePressEvent = self.open_arrstat_window4
        self.ui.t_arrow4.mousePressEvent = self.open_arrstat_window4



    def update_label(self):
        global arr
        if arr[10001] == 1:
########################################## Статус стрелки №1 ##################################################
            if arr[23] == 0: self.ui.stat_arrow1.setText(f"Нет стрелки")
            if arr[23] == 1: self.ui.stat_arrow1.setText(f"Выведена из обслуживания")
            if arr[23] == 2: self.ui.stat_arrow1.setText(f"ОТКЛ     ПРУ")
            if arr[23] == 3: self.ui.stat_arrow1.setText(f"ВКЛ     ПРУ")
            if arr[23] == 4: self.ui.stat_arrow1.setText(f"ПРУ  АВТО")
            if arr[23] == 5: self.ui.stat_arrow1.setText(f"ДС АВТО")
            if arr[23] == 6: self.ui.stat_arrow1.setText(f"ДС ОТКЛ")
            if arr[23] == 7: self.ui.stat_arrow1.setText(f"ОТКЛ     ПУО")
            if arr[23] == 8: self.ui.stat_arrow1.setText(f"ВКЛ     ПУО")
            if arr[23] == 9: self.ui.stat_arrow1.setText(f"ПУО АВТО")
            if arr[23] == 10: self.ui.stat_arrow1.setText(f"Ручной инстр.")
########################################## Статус стрелки №2 ##################################################
            if arr[22] == 0: self.ui.stat_arrow2.setText(f"Нет стрелки")
            if arr[22] == 1: self.ui.stat_arrow2.setText(f"Выведена из обслуживания")
            if arr[22] == 2: self.ui.stat_arrow2.setText(f"ОТКЛ     ПРУ")
            if arr[22] == 3: self.ui.stat_arrow2.setText(f"ВКЛ      ПРУ")
            if arr[22] == 4: self.ui.stat_arrow2.setText(f"ПРУ  АВТО")
            if arr[22] == 5: self.ui.stat_arrow2.setText(f"ДС АВТО")
            if arr[22] == 6: self.ui.stat_arrow2.setText(f"ДС ОТКЛ")
            if arr[22] == 7: self.ui.stat_arrow2.setText(f"ОТКЛ     ПУО")
            if arr[22] == 8: self.ui.stat_arrow2.setText(f"ВКЛ      ПУО")
            if arr[22] == 9: self.ui.stat_arrow2.setText(f"ПУО АВТО")
            if arr[22] == 10: self.ui.stat_arrow2.setText(f"Ручной инстр.")
########################################## Статус стрелки №3 ##################################################
            if arr[25] == 0: self.ui.stat_arrow3.setText(f"Нет стрелки")
            if arr[25] == 1: self.ui.stat_arrow3.setText(f"Выведена из обслуживания")
            if arr[25] == 2: self.ui.stat_arrow3.setText(f"ОТКЛ    ПРУ")
            if arr[25] == 3: self.ui.stat_arrow3.setText(f"ВКЛ    ПРУ")
            if arr[25] == 4: self.ui.stat_arrow3.setText(f"ПРУ  АВТО")
            if arr[25] == 5: self.ui.stat_arrow3.setText(f"ДС АВТО")
            if arr[25] == 6: self.ui.stat_arrow3.setText(f"ДС ОТКЛ")
            if arr[25] == 7: self.ui.stat_arrow3.setText(f"ОТКЛ    ПУО")
            if arr[25] == 8: self.ui.stat_arrow3.setText(f"ВКЛ     ПУО")
            if arr[25] == 9: self.ui.stat_arrow3.setText(f"ПУО АВТО")
            if arr[25] == 10: self.ui.stat_arrow3.setText(f"Ручной инстр.")
########################################## Статус стрелки №4 ##################################################
            if arr[24] == 0: self.ui.stat_arrow4.setText(f"Нет стрелки")
            if arr[24] == 1: self.ui.stat_arrow4.setText(f"Выведена из обслуживания")
            if arr[24] == 2: self.ui.stat_arrow4.setText(f"ОТКЛ     ПРУ")
            if arr[24] == 3: self.ui.stat_arrow4.setText(f"ВКЛ     ПРУ")
            if arr[24] == 4: self.ui.stat_arrow4.setText(f"ПРУ  АВТО")
            if arr[24] == 5: self.ui.stat_arrow4.setText(f"ДС АВТО")
            if arr[24] == 6: self.ui.stat_arrow4.setText(f"ДС ОТКЛ")
            if arr[24] == 7: self.ui.stat_arrow4.setText(f"ОТКЛ     ПУО")
            if arr[24] == 8: self.ui.stat_arrow4.setText(f"ВКЛ     ПУО")
            if arr[24] == 9: self.ui.stat_arrow4.setText(f"ПУО АВТО")
            if arr[24] == 10: self.ui.stat_arrow4.setText(f"Ручной инстр.")
############################## Статус освещения ###############################################################
            if arr[26] * 256 + arr[27] == 11: self.ui.stat_lighting.setText(f"ОТКЛ  ПРУ")
            if arr[26] * 256 + arr[27] == 12: self.ui.stat_lighting.setText(f"ВКЛ   ПРУ")
            if arr[26] * 256 + arr[27] == 13: self.ui.stat_lighting.setText(f"ПРУ   АВТО")
            if arr[26] * 256 + arr[27] == 14: self.ui.stat_lighting.setText(f"ОТКЛ   ПУО")
            if arr[26] * 256 + arr[27] == 15: self.ui.stat_lighting.setText(f"ВКЛ      ПУО")
            if arr[26] * 256 + arr[27] == 16: self.ui.stat_lighting.setText(f"АВТО    ПУО")
########################################## Статус связи с пультом  ##################################################
            if arr[2000]==1: self.ui.stat_puo.setText(f"ПУО")
            else: self.ui.stat_puo.setText(f"Нет   Связи")

########################################### Состояние стрелки №1 ######################################################

                                         ######## Общая Авария  ########
            if arr[101]&0x01:
                self.ui.name_arrow1.setText("Авария")
                self.ui.name_arrow1.setStyleSheet("background-color: red;")
            else:
                self.ui.name_arrow1.setText("№1")
                self.ui.name_arrow1.setStyleSheet("background-color: black; color: white; ")
                                             ######## Авария ДТР  ########
            if arr[101]&0x02:
                self.ui.t_arrow1.setText("Авария")
                self.ui.t_arrow1.setStyleSheet("background-color: red;")
            else:
                self.ui.t_arrow1.setText(f"{min(arr[102],arr[103])}")
                self.ui.t_arrow1.setStyleSheet("background-color: #c8c5c1; color: black;")

########################################### Состояние стрелки №2 ######################################################

                                            ######## Общая Авария  ########
            if arr[121]&0x01:
                self.ui.name_arrow2.setText("Авария")
                self.ui.name_arrow2.setStyleSheet("background-color : red")
            else:
                self.ui.name_arrow2.setText("№2")
                self.ui.name_arrow2.setStyleSheet("background-color : black; color : white ")
                                             ######## Авария ДТР  ########
            if arr[121]&0x02:
                self.ui.t_arrow2.setText("Авария")
                self.ui.t_arrow2.setStyleSheet("background-color : red")
            else:
                self.ui.t_arrow2.setText(f"{min(arr[122],arr[123])}")
                self.ui.t_arrow2.setStyleSheet("background-color : #c8c5c1; color : black ")

########################################### Состояние стрелки №3 ######################################################

                                            ######## Общая Авария  ########
            if arr[141]&0x01:
                self.ui.name_arrow3.setText("Авария")
                self.ui.name_arrow3.setStyleSheet("background-color : red")
            else:
                self.ui.name_arrow3.setText("№3")
                self.ui.name_arrow3.setStyleSheet("background-color : black; color : white ")
                                             ######## Авария ДТР  ########
            if arr[141]&0x02:
                self.ui.t_arrow3.setText("Авария")
                self.ui.t_arrow3.setStyleSheet("background-color : red")
            else:
                self.ui.t_arrow3.setText(f"{min(arr[142],arr[143])}")
                self.ui.t_arrow3.setStyleSheet("background-color : #c8c5c1; color : black ")



########################################### Состояние стрелки №4 ######################################################

                                         ######## Общая Авария  ########
            if arr[161]&0x01:
                self.ui.name_arrow4.setText("Авария")
                self.ui.name_arrow4.setStyleSheet("background-color : red")
            else:
                self.ui.name_arrow4.setText("№4")
                self.ui.name_arrow4.setStyleSheet("background-color : black; color : white ")
                                             ######## Авария ДТР  ########
            if arr[161]&0x02:
                self. ui.t_arrow4.setText("Авария")
                self.ui.t_arrow4.setStyleSheet("background-color : red")
            else:
                self.ui.t_arrow4.setText(f"{min(arr[162],arr[163])}")
                self.ui.t_arrow4.setStyleSheet("background-color : #c8c5c1; color : black ")

######################################################################################################################

    @pyqtSlot()
    def open_arrstat_window1(self,event):
        global arr
        arr[10001] = 3
        print(f"screen №: {arr[10001]}")
        self.close()
        arrow_stat.show()

    @pyqtSlot()
    def open_arrstat_window2(self, event):
        global arr
        arr[10001] = 4
        print(f"screen №: {arr[10001]}")
        self.close()
        arrow_stat.show()

    @pyqtSlot()
    def open_arrstat_window3(self, event):
        global arr
        arr[10001] = 5
        print(f"screen №: {arr[10001]}")
        self.close()
        arrow_stat.show()

    @pyqtSlot()
    def open_arrstat_window4(self, event):
        global arr
        arr[10001] = 6
        print(f"screen №: {arr[10001]}")
        self.close()
        arrow_stat.show()



    def open_status_window(self):
        global arr
        arr[10001] = 2
        print(f"screen №: {arr[10001]}")
        self.close()
        status_window.show()

    def open_setting_window(self):
        #global count
        #count = 1
        #arr[10001] = count
        #print(f"screen №: {count}")
        self.close()
        setting_window.show()
##########################################################################################################

##################################################### Окно Status ####################################################
######################################################################################################################
class StatusWindow(QMainWindow):
    global arr
    def __init__(self):
        super().__init__()
        self.ui = Ui_StatusWindow()
        self.ui.setupUi(self)
        self.ui.backButton.clicked.connect(self.back_to_start_window)

    def update_label(self):
        if arr[10001] == 2:
            self.ui.serial_number.setText(f"{arr[2] * 256 + arr[3]}")
            self.ui.date.setText(f"{(arr[8]*256+arr[9])/100}")
            self.ui.t_street.setText(f"{min(arr[18],arr[19])}")
            self.ui.t_box.setText(f"{min(arr[20],arr[21])}")
            self.ui.upt.setText(f"{arr[12]*256+arr[13]}")
            self.ui.tupt.setText(f"{arr[4]*256+arr[5]}")
            self.ui.modbus.setText(f"{arr[2001]}")

        # Например, self.ui.label.setText(data)
    def back_to_start_window(self):
        global arr
        arr[10001] = 1
        print(f"screen №: {arr[10001]}")
        self.close()
        start_window.show()


###############################################################################################################

################################################# Окно Статус стрелок ##################################################
########################################################################################################################
class ArrowStat(QMainWindow):
    global arr
    def __init__(self):
        super().__init__()
        self.ui = Ui_ArrowStat()
        self.ui.setupUi(self)
        self.ui.back.clicked.connect(self.back_to_start_window)

    def back_to_start_window(self):
        global arr
        arr[10001] = 1
        print(f"screen №: {arr[10001]}")
        self.close()
        start_window.show()

    def update_label(self):
        global arr
        index = (arr[10001]-3)*20
############################################ тип аварии стр№ 1 ################################################
        if arr[10001] > 2:
                                      ######## Авария ДТР  ########
            if arr[101+index]&0x02:
                self.ui.t_arrow.setText("Авария")
                self.ui.t_arrow.setStyleSheet("background-color: red;")
            else:
                self.ui.t_arrow.setText(f"{min(arr[102], arr[103])}")
                self.ui.t_arrow.setStyleSheet("background-color: #00aa00; color: white")
                                 ######## Авария изоляции канал 1  ########
            if arr[101+index] & 0x04 == 0:
                self.ui.ch1_stat.setText("АВАРИЯ")
                self.ui.ch1_stat.setStyleSheet("background-color: red; color: white;")
            else:
                self.ui.ch1_stat.setText("НОРМА")
                self.ui.ch1_stat.setStyleSheet("background-color: #00aa00; color: black;")
                              ######## Авария изоляции канал 2  ########
            if arr[101+index] & 0x08 == 0:
                self.ui.ch2_stat.setText("АВАРИЯ")
                self.ui.ch2_stat.setStyleSheet("background-color: red; color: white;")
            else:
                self.ui.ch2_stat.setText("НОРМА")
                self.ui.ch2_stat.setStyleSheet("background-color: #00aa00; color: black;")
        else:
            self.ui.t_arrow.setText(f"{min(arr[102], arr[103])}")
            self.ui.t_arrow.setStyleSheet("background-color: #00aa00; color: white;")
            self.ui.ch1_stat.setText("НОРМА")
            self.ui.ch1_stat.setStyleSheet("background-color: #00aa00; color: black;")
            self.ui.ch2_stat.setText("НОРМА")
            self.ui.ch2_stat.setStyleSheet("background-color: #00aa00; color: black;")

############################################################################################################################
#############################################################################################################################


############################################# Окно связи с контроллером ##################################################
##########################################################################################################################

######################################################################################################################
######################################################################################################################


######################################### Окно настройки ##############################################################
#######################################################################################################################
class Setting(QMainWindow):
    #global count
    #arr[10001] = count
    def __init__(self):
        super().__init__()
        self.ui = Ui_Setting()
        self.ui.setupUi(self)
        self.ui.backButton.clicked.connect(self.back_to_start_window)

    def back_to_start_window(self):
        global arr
        arr[10001] = 1
        print(f"screen №: {arr[10001]}")
        self.close()
        start_window.show()
#######################################################################################################################
#######################################################################################################################

if __name__ == "__main__":
    app = QApplication(sys.argv)

    choice_window = ChoiceWindow()
    status_window = StatusWindow()
    start_window = StartWindow()
    arrow_stat = ArrowStat()
    setting_window = Setting()
    choice_window.show()

    sys.exit(app.exec_())