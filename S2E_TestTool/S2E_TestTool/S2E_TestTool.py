# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import serial
import serial.tools.list_ports
import os
import time
import threading
import filecmp
import wx.lib.newevent


lock = threading.Lock()

wxUnit1Recv, EVT_UNIT1_RECV = wx.lib.newevent.NewEvent()
wxUnit2Recv, EVT_UNIT2_RECV = wx.lib.newevent.NewEvent()
wxUnit1Send, EVT_UNIT1_SEND = wx.lib.newevent.NewEvent()
wxUnit2Send, EVT_UNIT2_SEND = wx.lib.newevent.NewEvent()


class Unit1SendThread(threading.Thread):
    def __init__(self, parent):
        threading.Thread.__init__(self)
        self._parent = parent
        self.start()

    def run(self):
        evt = wxUnit1Send()
        self._parent.GetEventHandler().ProcessEvent(evt)

class Unit2SendThread(threading.Thread):
    def __init__(self, parent):
        threading.Thread.__init__(self)
        self._parent = parent
        self.start()

    def run(self):
        evt = wxUnit2Send()
        self._parent.GetEventHandler().ProcessEvent(evt)


class Unit1RecvThread(threading.Thread):
    def __init__(self, parent):
        threading.Thread.__init__(self)
        self._parent = parent
        self._stop = threading.Event()
        self.start()
    
    def run(self):
        evt = wxUnit1Recv()
        self._parent.GetEventHandler().ProcessEvent(evt)
        
    def stop(self):
        self._stop.set()
    
    def IsStopped(self):
        return self._stop.isSet()
        


class Unit2RecvThread(threading.Thread):
    def __init__(self, parent):
        threading.Thread.__init__(self)
        self._parent = parent
        self._stop = threading.Event()
        self.start()

    def run(self):
        evt = wxUnit2Recv()
        self._parent.GetEventHandler().ProcessEvent(evt)

    def stop(self):
        self._stop.set()
    
    def IsStopped(self):
        return self._stop.isSet()

###########################################################################
## Class S2E_TestTool
###########################################################################

class S2E_TestTool ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"S2E Test Tool", pos = wx.DefaultPosition, size = wx.Size( 521,708 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
        
        bSizer9 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
        
        
        bSizer9.Add( bSizer10, 0, wx.EXPAND, 5 )
        
        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )
        
        sbSizer_TestUnit1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Test Unit 1" ), wx.VERTICAL )
        
        bSizer_serial_port1 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText_Serial_Port1 = wx.StaticText( sbSizer_TestUnit1.GetStaticBox(), wx.ID_ANY, u"Serial Port", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_Serial_Port1.Wrap( -1 )
        bSizer_serial_port1.Add( self.m_staticText_Serial_Port1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        m_comboBox_serialPort1Choices = []
        self.m_comboBox_serialPort1 = wx.ComboBox( sbSizer_TestUnit1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBox_serialPort1Choices, 0 )
        bSizer_serial_port1.Add( self.m_comboBox_serialPort1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        sbSizer_TestUnit1.Add( bSizer_serial_port1, 0, wx.EXPAND, 5 )
        
        bSizer_baudrate1 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText_baudrate1 = wx.StaticText( sbSizer_TestUnit1.GetStaticBox(), wx.ID_ANY, u"Baudrate", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_baudrate1.Wrap( -1 )
        bSizer_baudrate1.Add( self.m_staticText_baudrate1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        m_comboBox_baudrate1Choices = [ u"2400", u"9600", u"14400", u"19200", u"38400", u"57600", u"76800", u"115200", u"230400", u"460800" ]
        self.m_comboBox_baudrate1 = wx.ComboBox( sbSizer_TestUnit1.GetStaticBox(), wx.ID_ANY, u"115200", wx.DefaultPosition, wx.DefaultSize, m_comboBox_baudrate1Choices, 0 )
        bSizer_baudrate1.Add( self.m_comboBox_baudrate1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        sbSizer_TestUnit1.Add( bSizer_baudrate1, 1, wx.EXPAND, 5 )
        
        bSizer_serialconnect1 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_button_SerialConnect1 = wx.Button( sbSizer_TestUnit1.GetStaticBox(), wx.ID_ANY, u"Connect", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer_serialconnect1.Add( self.m_button_SerialConnect1, 1, wx.ALL, 5 )
        
        self.m_button_SerialClose1 = wx.Button( sbSizer_TestUnit1.GetStaticBox(), wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button_SerialClose1.Enable( False )
        
        bSizer_serialconnect1.Add( self.m_button_SerialClose1, 1, wx.ALL, 5 )
        
        
        sbSizer_TestUnit1.Add( bSizer_serialconnect1, 1, wx.EXPAND, 5 )
        
        
        bSizer12.Add( sbSizer_TestUnit1, 1, wx.EXPAND|wx.ALL, 5 )
        
        sbSizer_TestUnit2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Test Unit2" ), wx.VERTICAL )
        
        bSizer_serialport2 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText_serialPort2 = wx.StaticText( sbSizer_TestUnit2.GetStaticBox(), wx.ID_ANY, u"Serial Port", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_serialPort2.Wrap( -1 )
        bSizer_serialport2.Add( self.m_staticText_serialPort2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        m_comboBox_serialPort2Choices = []
        self.m_comboBox_serialPort2 = wx.ComboBox( sbSizer_TestUnit2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBox_serialPort2Choices, 0 )
        bSizer_serialport2.Add( self.m_comboBox_serialPort2, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        sbSizer_TestUnit2.Add( bSizer_serialport2, 1, wx.EXPAND, 5 )
        
        bSizer_baudrate2 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText_baudrate2 = wx.StaticText( sbSizer_TestUnit2.GetStaticBox(), wx.ID_ANY, u"Baudrate", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_baudrate2.Wrap( -1 )
        bSizer_baudrate2.Add( self.m_staticText_baudrate2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        m_comboBox_baudrate2Choices = [ u"2400", u"9600", u"14400", u"19200", u"38400", u"57600", u"76800", u"115200", u"230400", u"460800" ]
        self.m_comboBox_baudrate2 = wx.ComboBox( sbSizer_TestUnit2.GetStaticBox(), wx.ID_ANY, u"115200", wx.DefaultPosition, wx.DefaultSize, m_comboBox_baudrate2Choices, 0 )
        bSizer_baudrate2.Add( self.m_comboBox_baudrate2, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        sbSizer_TestUnit2.Add( bSizer_baudrate2, 1, wx.EXPAND, 5 )
        
        bSizer_serialconnect2 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_button_SerialConnect2 = wx.Button( sbSizer_TestUnit2.GetStaticBox(), wx.ID_ANY, u"Connect", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer_serialconnect2.Add( self.m_button_SerialConnect2, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_button_SerialClose2 = wx.Button( sbSizer_TestUnit2.GetStaticBox(), wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button_SerialClose2.Enable( False )
        
        bSizer_serialconnect2.Add( self.m_button_SerialClose2, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        sbSizer_TestUnit2.Add( bSizer_serialconnect2, 1, wx.EXPAND, 5 )
        
        
        bSizer12.Add( sbSizer_TestUnit2, 1, wx.EXPAND|wx.ALL, 5 )
        
        
        bSizer9.Add( bSizer12, 0, wx.EXPAND, 5 )
        
        sbSizer_SendOption = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Send Option" ), wx.VERTICAL )
        
        bSizer16 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_checkBox_usingFile = wx.CheckBox( sbSizer_SendOption.GetStaticBox(), wx.ID_ANY, u"Using File", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_checkBox_usingFile.SetValue(True) 
        bSizer16.Add( self.m_checkBox_usingFile, 0, wx.ALL, 5 )
        
        self.m_checkBox_NotUsingFile = wx.CheckBox( sbSizer_SendOption.GetStaticBox(), wx.ID_ANY, u"Not Using File", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer16.Add( self.m_checkBox_NotUsingFile, 0, wx.ALL, 5 )
        
        
        sbSizer_SendOption.Add( bSizer16, 1, wx.EXPAND, 5 )
        
        sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( sbSizer_SendOption.GetStaticBox(), wx.ID_ANY, u"Using File" ), wx.HORIZONTAL )
        
        self.m_staticText_ChunkSize = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"Chunk Size", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_ChunkSize.Wrap( -1 )
        sbSizer6.Add( self.m_staticText_ChunkSize, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_textCtrl_ChunkSize = wx.TextCtrl( sbSizer6.GetStaticBox(), wx.ID_ANY, u"1024", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl_ChunkSize.SetMaxLength( 1024000 ) 
        sbSizer6.Add( self.m_textCtrl_ChunkSize, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText_SendDelay = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"Send Delay(ms)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_SendDelay.Wrap( -1 )
        sbSizer6.Add( self.m_staticText_SendDelay, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_textCtrl_SendDelay = wx.TextCtrl( sbSizer6.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer6.Add( self.m_textCtrl_SendDelay, 1, wx.ALL, 5 )
        
        
        sbSizer_SendOption.Add( sbSizer6, 0, wx.EXPAND, 5 )
        
        sbSizer8 = wx.StaticBoxSizer( wx.StaticBox( sbSizer_SendOption.GetStaticBox(), wx.ID_ANY, u"Not Using File" ), wx.VERTICAL )
        
        bSizer18 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText_Unit1_SendSize = wx.StaticText( sbSizer8.GetStaticBox(), wx.ID_ANY, u"Unit1 Send Size(Byte)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_Unit1_SendSize.Wrap( -1 )
        bSizer18.Add( self.m_staticText_Unit1_SendSize, 1, wx.ALL, 5 )
        
        self.m_textCtrl_Unit1_SendSize = wx.TextCtrl( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl_Unit1_SendSize.Enable( False )
        
        bSizer18.Add( self.m_textCtrl_Unit1_SendSize, 1, wx.ALL, 5 )
        
        self.m_staticText_Unit2_SendSize = wx.StaticText( sbSizer8.GetStaticBox(), wx.ID_ANY, u"Unit2 Send Size(Byte)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_Unit2_SendSize.Wrap( -1 )
        bSizer18.Add( self.m_staticText_Unit2_SendSize, 1, wx.ALL, 5 )
        
        self.m_textCtrl_Unit2_SendSize = wx.TextCtrl( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl_Unit2_SendSize.Enable( False )
        
        bSizer18.Add( self.m_textCtrl_Unit2_SendSize, 1, wx.ALL, 5 )
        
        
        sbSizer8.Add( bSizer18, 1, wx.EXPAND, 5 )
        
        bSizer19 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText11 = wx.StaticText( sbSizer8.GetStaticBox(), wx.ID_ANY, u"Send Delay(byte per us)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )
        bSizer19.Add( self.m_staticText11, 0, wx.ALL, 5 )
        
        self.m_textCtrl_SendDelay_Byteus = wx.TextCtrl( sbSizer8.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl_SendDelay_Byteus.Enable( False )
        
        bSizer19.Add( self.m_textCtrl_SendDelay_Byteus, 0, wx.ALL, 5 )
        
        
        sbSizer8.Add( bSizer19, 1, wx.EXPAND, 5 )
        
        
        sbSizer_SendOption.Add( sbSizer8, 0, wx.EXPAND, 5 )
        
        bSizer17 = wx.BoxSizer( wx.HORIZONTAL )
        
        
        sbSizer_SendOption.Add( bSizer17, 1, wx.EXPAND, 5 )
        
        
        bSizer9.Add( sbSizer_SendOption, 0, wx.ALL|wx.EXPAND, 5 )
        
        sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Send Test File" ), wx.VERTICAL )
        
        bSizer26 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText_TestUnit1File = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Test Unit1 File", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_TestUnit1File.Wrap( -1 )
        bSizer26.Add( self.m_staticText_TestUnit1File, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_textCtrl_TestFile1 = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer26.Add( self.m_textCtrl_TestFile1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_button_browse1 = wx.Button( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Browse", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer26.Add( self.m_button_browse1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        sbSizer3.Add( bSizer26, 0, wx.EXPAND, 5 )
        
        bSizer27 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText_TestUnit2File = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Test Unit2 File", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_TestUnit2File.Wrap( -1 )
        bSizer27.Add( self.m_staticText_TestUnit2File, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_textCtrl_TestFile2 = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer27.Add( self.m_textCtrl_TestFile2, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_button_browse2 = wx.Button( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Browse", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer27.Add( self.m_button_browse2, 0, wx.ALL, 5 )
        
        
        sbSizer3.Add( bSizer27, 0, wx.EXPAND, 5 )
        
        bSizer28 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_button_StartTest = wx.Button( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Start Test", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button_StartTest.Enable( False )
        
        bSizer28.Add( self.m_button_StartTest, 1, wx.ALL, 5 )
        
        
        sbSizer3.Add( bSizer28, 1, wx.EXPAND, 5 )
        
        bSizer34 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_checkBox_Fullduplex = wx.CheckBox( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Full-Duplex", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_checkBox_Fullduplex.SetValue(True) 
        bSizer34.Add( self.m_checkBox_Fullduplex, 0, wx.ALL, 5 )
        
        self.m_checkBox_Unit1toUnit2 = wx.CheckBox( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Unit1 --> Unit2", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer34.Add( self.m_checkBox_Unit1toUnit2, 0, wx.ALL, 5 )
        
        self.m_checkBox_Unit2toUnit1 = wx.CheckBox( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Unit2 --> Unit1", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer34.Add( self.m_checkBox_Unit2toUnit1, 0, wx.ALL, 5 )
        
        
        sbSizer3.Add( bSizer34, 1, wx.EXPAND, 5 )
        
        
        bSizer9.Add( sbSizer3, 0, wx.EXPAND|wx.ALL, 5 )
        
        sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Test Result" ), wx.HORIZONTAL )
        
        bSizer30 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_textCtrl_ResultUnit1 = wx.TextCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
        bSizer30.Add( self.m_textCtrl_ResultUnit1, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        sbSizer4.Add( bSizer30, 1, wx.EXPAND, 5 )
        
        bSizer31 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_textCtrl_ResultUnit2 = wx.TextCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
        bSizer31.Add( self.m_textCtrl_ResultUnit2, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        sbSizer4.Add( bSizer31, 1, wx.EXPAND, 5 )
        
        
        bSizer9.Add( sbSizer4, 1, wx.EXPAND|wx.ALL, 5 )
        
        
        self.SetSizer( bSizer9 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_comboBox_serialPort1.Bind( wx.EVT_LEFT_DOWN, self.onSerialPort1 )
        self.m_button_SerialConnect1.Bind( wx.EVT_BUTTON, self.onSerialConnect1 )
        self.m_button_SerialClose1.Bind( wx.EVT_BUTTON, self.onSerialClose1 )
        self.m_comboBox_serialPort2.Bind( wx.EVT_LEFT_DOWN, self.onSerialPort2 )
        self.m_button_SerialConnect2.Bind( wx.EVT_BUTTON, self.onSerialConnect2 )
        self.m_button_SerialClose2.Bind( wx.EVT_BUTTON, self.onSerialClose2 )
        self.m_checkBox_usingFile.Bind( wx.EVT_CHECKBOX, self.onUsingFile )
        self.m_checkBox_NotUsingFile.Bind( wx.EVT_CHECKBOX, self.onNotUsingFile )
        self.m_button_browse1.Bind( wx.EVT_BUTTON, self.onBrowse1 )
        self.m_button_browse2.Bind( wx.EVT_BUTTON, self.onBrowse2 )
        self.m_button_StartTest.Bind( wx.EVT_BUTTON, self.onStartTest )
        self.m_checkBox_Fullduplex.Bind( wx.EVT_CHECKBOX, self.onFullduplex )
        self.m_checkBox_Unit1toUnit2.Bind( wx.EVT_CHECKBOX, self.onUnit1toUnit2 )
        self.m_checkBox_Unit2toUnit1.Bind( wx.EVT_CHECKBOX, self.onUnit2toUnit1 )

        
        
        #User Code
        self.Bind(EVT_UNIT1_SEND, self.Send_DataUnit1toUnit2)
        self.Bind(EVT_UNIT2_SEND, self.Send_DataUnit2toUnit1)
        
        self.Bind(EVT_UNIT1_RECV, self.Recv_DataUnit1)
        self.Bind(EVT_UNIT2_RECV, self.Recv_DataUnit2)
        
        self.GetComPortList(1)
        self.GetComPortList(2)

        self.m_Unit1_ser_IsOpen = False
        self.m_Unit2_ser_IsOpen = False
        self.m_Unit1_recv_filename = "Unit1_Rx_File.txt"
        self.m_Unit2_recv_filename = "Unit2_Rx_File.txt"
        
        self.m_Unit1_Send_Size = 0
        self.m_Unit2_Send_Size = 0
        self.m_unit1_recv_size = 0
        self.m_unit2_recv_size = 0
        
        
    def __del__( self ):
        if self.m_Unit1_ser_IsOpen == True:
            self.m_Unit1_ser.close();
        if self.m_Unit2_ser_IsOpen == True:
            self.m_Unit2_ser.close();


    def GetComPortList(self,unit_num):
        comboBox_serial_portChoices = []
        
        self.available_ports = list(serial.tools.list_ports.comports())
        for self.port in self.available_ports:
            if(self.port[2] != 'n/a'):
                comboBox_serial_portChoices.append(self.port[0])
                 
        if(unit_num == 1):
            self.m_comboBox_serialPort1.SetItems(comboBox_serial_portChoices)
        else:
            self.m_comboBox_serialPort2.SetItems(comboBox_serial_portChoices)
    
    
    # Virtual event handlers, overide them in your derived class
    def onSerialPort1( self, event ):
        self.GetComPortList(1)    

    def onSerialConnect1( self, event ):
        com = self.m_comboBox_serialPort1.GetValue()
        baud = int(self.m_comboBox_baudrate1.GetValue())
        if com == '':
            wx.MessageBox("Please Select Serial Port", 'Warning',wx.OK | wx.ICON_ERROR)
            return
        
        self.m_Unit1_ser = serial.Serial(com, baud, timeout = 0)
        if(self.m_Unit1_ser == -1):
            self.m_Unit1_ser.close()
            wx.MessageBox("Serial Open Error.\r\n", 'Warning',wx.OK | wx.ICON_ERROR)
            return
        
        self.m_button_SerialConnect1.Disable()
        self.m_button_SerialClose1.Enable()
        self.m_Unit1_ser_IsOpen = True;
        
    def onSerialClose1( self, event ):
        if(self.m_Unit1_ser_IsOpen == True):
            self.m_Unit1_ser.close()
            self.m_button_SerialConnect1.Enable()
            self.m_button_SerialClose1.Disable()
            self.m_Unit1_ser_IsOpen = False
            self.m_textCtrl_TestFile1.SetValue("")
            self.m_textCtrl_TestFile2.SetValue("")

    def onSerialPort2( self, event ):
        self.GetComPortList(2)    
    
    def onSerialConnect2( self, event ):
        com = self.m_comboBox_serialPort2.GetValue()
        baud = int(self.m_comboBox_baudrate2.GetValue())
        if com == '':
            wx.MessageBox("Please Select Serial Port", 'Warning',wx.OK | wx.ICON_ERROR)
            return
        
        self.m_Unit2_ser = serial.Serial(com, baud, timeout = 0)
        if(self.m_Unit2_ser == -1):
            self.m_Unit2_ser.close()
            wx.MessageBox("Serial Open Error.\r\n", 'Warning',wx.OK | wx.ICON_ERROR)
            return
        
        self.m_button_SerialConnect2.Disable()
        self.m_button_SerialClose2.Enable()
        self.m_Unit2_ser_IsOpen = True;
        
    def onSerialClose2( self, event ):
        if(self.m_Unit2_ser_IsOpen == True):
            self.m_Unit2_ser.close()
            self.m_button_SerialConnect2.Enable()
            self.m_button_SerialClose2.Disable()
            self.m_Unit2_ser_IsOpen = False
            self.m_textCtrl_TestFile1.SetValue("")
            self.m_textCtrl_TestFile2.SetValue("")

    def onUsingFile( self, event ):
        self.m_checkBox_NotUsingFile.SetValue(False)
        self.m_button_browse1.Enable()
        self.m_button_browse2.Enable()
        self.m_textCtrl_TestFile1.Enable()
        self.m_textCtrl_TestFile2.Enable()
        self.m_textCtrl_Unit1_SendSize.Disable()
        self.m_textCtrl_Unit2_SendSize.Disable()
        self.m_textCtrl_SendDelay_Byteus.Disable()
        self.m_button_StartTest.Disable()
        self.m_textCtrl_ChunkSize.Enable()
        self.m_textCtrl_SendDelay.Enable()
        
        
    def onNotUsingFile( self, event ):
        self.m_checkBox_usingFile.SetValue(False)
        self.m_button_browse1.Disable()
        self.m_button_browse2.Disable()
        self.m_textCtrl_TestFile1.Disable()
        self.m_textCtrl_TestFile2.Disable()
        self.m_textCtrl_Unit1_SendSize.Enable()
        self.m_textCtrl_Unit2_SendSize.Enable()
        self.m_textCtrl_SendDelay_Byteus.Enable()
        self.m_button_StartTest.Enable()
        self.m_textCtrl_ChunkSize.Disable()
        self.m_textCtrl_SendDelay.Disable()
        
            
    def onBrowse1( self, event ):
        if self.m_Unit1_ser_IsOpen == False and self.m_Unit2_ser_IsOpen == False:
            wx.MessageBox("Please Open Serial Port.\r\n", 'Warning',wx.OK | wx.ICON_ERROR)
            return

        filename = ''
        dlg = wx.FileDialog(self, message='Choose a file')
        
        if dlg.ShowModal() == wx.ID_OK:
            #get the new filename from the dialog
            filename = dlg.GetPath()
        dlg.Destroy()
        
        if filename:
            self.m_textCtrl_TestFile1.SetValue(filename)
    
        if self.m_checkBox_Unit1toUnit2.GetValue() == True:
            self.m_button_StartTest.Enable()
        elif (self.m_checkBox_Fullduplex.GetValue() == True) and (self.m_textCtrl_TestFile2.GetValue() != ''):
            self.m_button_StartTest.Enable()
        else:
            self.m_button_StartTest.Disable()
            
    
    def onBrowse2( self, event ):
        if self.m_Unit1_ser_IsOpen == False and self.m_Unit2_ser_IsOpen == False:
            wx.MessageBox("Please Open Serial Port.\r\n", 'Warning',wx.OK | wx.ICON_ERROR)
            return

        filename = ''
        dlg = wx.FileDialog(self, message='Choose a file')
        
        if dlg.ShowModal() == wx.ID_OK:
            filename = dlg.GetPath()
        dlg.Destroy()
        
        if filename:
            self.m_textCtrl_TestFile2.SetValue(filename)
        
        if self.m_checkBox_Unit2toUnit1.GetValue() == True:
            self.m_button_StartTest.Enable()
        elif (self.m_checkBox_Fullduplex.GetValue() == True) and (self.m_textCtrl_TestFile1.GetValue() != ''):
            self.m_button_StartTest.Enable()
        else:
            self.m_button_StartTest.Disable()

    def onStartTest( self, event ):
        self.m_recv1_finish = False
        self.m_recv2_finish = False
        
        self.m_unit1_recv_size = 0;
        self.m_unit2_recv_size = 0;
        self.m_textCtrl_ResultUnit1.Clear()
        self.m_textCtrl_ResultUnit2.Clear()
        
        if self.m_checkBox_Unit1toUnit2.GetValue() == True:
            Unit2RecvThread(self)            
            Unit1SendThread(self)
        elif self.m_checkBox_Unit2toUnit1.GetValue() == True:
            Unit1RecvThread(self)            
            Unit2SendThread(self)
        elif self.m_checkBox_Fullduplex.GetValue() == True:
            Unit1RecvThread(self)            
            Unit1SendThread(self)
            Unit2RecvThread(self)            
            Unit2SendThread(self)
            
        self.m_button_StartTest.Disable()
        
    def onFullduplex( self, event ):
        self.m_checkBox_Fullduplex.SetValue(True)
        self.m_checkBox_Unit1toUnit2.SetValue(False)
        self.m_checkBox_Unit2toUnit1.SetValue(False)
    
    def onUnit1toUnit2( self, event ):
        self.m_checkBox_Unit1toUnit2.SetValue(True)
        self.m_checkBox_Fullduplex.SetValue(False)
        self.m_checkBox_Unit2toUnit1.SetValue(False)
    
    def onUnit2toUnit1( self, event ):
        self.m_checkBox_Unit2toUnit1.SetValue(True)
        self.m_checkBox_Unit1toUnit2.SetValue(False)
        self.m_checkBox_Fullduplex.SetValue(False)
        
    def Recv_DataUnit1(self, event):
        end_cnt = 0
        
        self.m_unit1_recv_size = 0
        recv_file_data = ""
        self.m_textCtrl_ResultUnit1.Clear()


        if self.m_checkBox_NotUsingFile.GetValue() == True:
            while True:
                recv_data = self.m_Unit1_ser.read(1024)
                if len(recv_data) > 0:
                    end_cnt = 0
                    self.m_unit1_recv_size += len(recv_data)
                     
                    temp_str = "Recv size : %d/%d\r\n" % (self.m_unit1_recv_size,self.m_Unit2_Send_Size)
                    self.m_textCtrl_ResultUnit1.AppendText(temp_str)
                else:
                    time.sleep(0.0001)
                    end_cnt += 1

                    if end_cnt == 100000 :
                        self.m_textCtrl_ResultUnit1.AppendText("Wait for remained serial data\r\n")
                    elif end_cnt >= 200000:
                        self.m_recv1_finish = True
                        break
        
            message = "Test Result : %d/%d\r\n" % (self.m_unit1_recv_size,self.m_Unit2_Send_Size)
            self.m_textCtrl_ResultUnit1.AppendText(message)
        
        elif self.m_checkBox_usingFile.GetValue() == True:
            while True:
                recv_data = self.m_Unit1_ser.read(1024)
                if len(recv_data) > 0:
                    end_cnt = 0
                    lock.acquire()
                    self.m_unit1_recv_size += len(recv_data)
                    recv_file_data += recv_data
                    lock.release()

                    temp_str = "Recv size : %d/%d\r\n" % (self.m_unit1_recv_size,self.filename2_size)
                    self.m_textCtrl_ResultUnit1.AppendText(temp_str)
                else:
                    time.sleep(0.0001)
                    end_cnt += 1

                    if end_cnt == 100000 :
                        self.m_textCtrl_ResultUnit1.AppendText("Wait for remained serial data\r\n")
                    elif end_cnt >= 200000:
                        self.m_recv1_finish = True
                        break
            
            recv_file = open(self.m_Unit1_recv_filename,"wb")
            recv_file.write(recv_file_data)
            recv_file.close()

            result = filecmp.cmp(self.m_textCtrl_TestFile2.GetValue(),self.m_Unit1_recv_filename)
            message = "Test Result(File Compare) : %s\r\n" % str(result)
            self.m_textCtrl_ResultUnit1.AppendText(message)
            

        if self.m_checkBox_Fullduplex.GetValue() == True:
            if self.m_recv1_finish == True and self.m_recv2_finish == True:
                self.m_button_StartTest.Enable()
        else:
            self.m_button_StartTest.Enable()
        
    def Recv_DataUnit2(self, event):
        end_cnt = 0
        self.m_unit2_recv_size = 0
        recv_file_data = ""
        self.m_textCtrl_ResultUnit2.Clear()

        if self.m_checkBox_NotUsingFile.GetValue() == True:
            while True:
                recv_data = self.m_Unit2_ser.read(1024)
                if len(recv_data) > 0:
                    end_cnt = 0
                    lock.acquire()
                    self.m_unit2_recv_size += len(recv_data)
                    
                    temp_str = "Recv size : %d/%d\r\n" % (self.m_unit2_recv_size,self.m_Unit1_Send_Size)
                    self.m_textCtrl_ResultUnit2.AppendText(temp_str)
                    lock.release()
                else:
                    time.sleep(0.0001)
                    end_cnt += 1

                    if end_cnt == 100000 :
                        self.m_textCtrl_ResultUnit2.AppendText("Wait for remained serial data\r\n")
                    elif end_cnt >= 200000:
                        self.m_recv2_finish = True
                        break

            message = "Test Result : %d/%d\r\n" % (self.m_unit2_recv_size,self.m_Unit1_Send_Size)
            self.m_textCtrl_ResultUnit2.AppendText(message)

        elif self.m_checkBox_usingFile.GetValue() == True:
            while True:
                recv_data = self.m_Unit2_ser.read(1024)
                if len(recv_data) > 0:
                    end_cnt = 0
                    lock.acquire()
                    self.m_unit2_recv_size += len(recv_data)
                    recv_file_data += recv_data
                    lock.release()

                    temp_str = "Recv size : %d/%d\r\n" % (self.m_unit2_recv_size,self.filename1_size)
                    self.m_textCtrl_ResultUnit2.AppendText(temp_str)
                else:
                    time.sleep(0.0001)
                    end_cnt += 1

                    if end_cnt == 100000 :
                        self.m_textCtrl_ResultUnit2.AppendText("Wait for remained serial data\r\n")
                    elif end_cnt >= 200000:
                        self.m_recv2_finish = True
                        break

            recv_file = open(self.m_Unit2_recv_filename,"wb")
            recv_file.write(recv_file_data)
            recv_file.close()

            result = filecmp.cmp(self.m_textCtrl_TestFile1.GetValue(),self.m_Unit2_recv_filename)
            message = "Test Result(File Compare) : %s\r\n" % str(result)
            self.m_textCtrl_ResultUnit2.AppendText(message)
            

        if self.m_checkBox_Fullduplex.GetValue() == True:
            if self.m_recv1_finish == True and self.m_recv2_finish == True:
                self.m_button_StartTest.Enable()
        else:
            self.m_button_StartTest.Enable()

    def Send_DataUnit1toUnit2(self, event):
        if self.m_checkBox_usingFile.GetValue() == True:
            self.Send_File_Unit1toUnit2()
        elif self.m_checkBox_NotUsingFile.GetValue() == True:
            self.Send_Ascii_Unit1toUnit2()  
    
    def Send_DataUnit2toUnit1(self, event):
        if self.m_checkBox_usingFile.GetValue() == True:
            self.Send_File_Unit2toUnit1()
        elif self.m_checkBox_NotUsingFile.GetValue() == True:
            self.Send_Ascii_Unit2toUnit1()
    
    def Send_Ascii_Unit1toUnit2(self):
        send_data = 'A'
        self.m_Unit1_Send_Size = int(self.m_textCtrl_Unit1_SendSize.GetValue())
        delay = float(int(self.m_textCtrl_SendDelay_Byteus.GetValue())) / float(1000000)

        try:
            for i in range(self.m_Unit1_Send_Size):
                self.m_Unit1_ser.write(send_data)
                time.sleep(delay)
                
                if send_data == 'z':
                    send_data = '\r'
                elif send_data == '\r':
                    send_data = '\n'
                elif send_data == '\n':
                    send_data = 'A'
                elif i == (self.m_Unit1_Send_Size - 3):
                    send_data = '\r'
                else:
                    send_data = chr(ord(send_data) + 1)
            
        except Exception as e:
            s = str(e)
            wx.MessageBox(s, 'Warning',wx.OK | wx.ICON_ERROR)

    def Send_Ascii_Unit2toUnit1(self):
        send_data = 'A'
        self.m_Unit2_Send_Size = int(self.m_textCtrl_Unit2_SendSize.GetValue())
        delay = float(int(self.m_textCtrl_SendDelay_Byteus.GetValue())) / float(1000000)


        try:
            for i in range(self.m_Unit2_Send_Size):
                self.m_Unit2_ser.write(send_data)
                time.sleep(delay)
                
                if send_data == 'z':
                    send_data = '\r'
                elif send_data == '\r':
                    send_data = '\n'
                elif send_data == '\n':
                    send_data = 'A'
                elif i == (self.m_Unit2_Send_Size - 3):
                    send_data = '\r'
                else:
                    send_data = chr(ord(send_data) + 1)
            
        except Exception as e:
            s = str(e)
            wx.MessageBox(s, 'Warning',wx.OK | wx.ICON_ERROR)

    
    def Send_File_Unit1toUnit2(self):
        self.filename1 = self.m_textCtrl_TestFile1.GetValue()
        if self.filename1 == '':
            return
        
        self.filename1_size = os.stat(self.filename1).st_size

        file_data = ""
        send_file = open(self.filename1,'rb')
        for i in xrange(0,self.filename1_size,1024):
            data = send_file.read(1024)
            file_data += data
        send_file.close()
        
        try:
            chunk_size = int(self.m_textCtrl_ChunkSize.GetValue())
            send_delay = float(int(self.m_textCtrl_SendDelay.GetValue())) / float(1000)
            
            for i in xrange(0,self.filename1_size,chunk_size):
                data = file_data[i:i+chunk_size]
                self.m_Unit1_ser.write(data)
                time.sleep(send_delay)
                
        except Exception as e:
            s = str(e)
            wx.MessageBox(s, 'Warning',wx.OK | wx.ICON_ERROR)
            

    def Send_File_Unit2toUnit1(self):
        self.filename2 = self.m_textCtrl_TestFile2.GetValue()
        if self.filename2 == '':
            return
        
        self.filename2_size = os.stat(self.filename2).st_size
        file_data = ""
        send_file = open(self.filename2,'rb')
        for i in xrange(0,self.filename2_size,1024):
            data = send_file.read(1024)
            file_data += data
        send_file.close()
        
        try:
            chunk_size = int(self.m_textCtrl_ChunkSize.GetValue())
            send_delay = float(int(self.m_textCtrl_SendDelay.GetValue())) / float(1000)
            
            for i in xrange(0,self.filename2_size,chunk_size):
                data = file_data[i:i+chunk_size]
                self.m_Unit2_ser.write(data)
                time.sleep(send_delay)

        except Exception as e:
            s = str(e)
            wx.MessageBox(s, 'Warning',wx.OK | wx.ICON_ERROR)
            
        
if __name__ == "__main__":
    app = wx.App(0)
    s2e_test = S2E_TestTool(None)
    app.SetTopWindow(s2e_test)
    s2e_test.Show()
    app.MainLoop()