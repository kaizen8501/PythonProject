# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  6 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import serial
import serial.tools.list_ports
import time
import threading
import os

import wx
import wx.xrc

###########################################################################
## Class WIZnetMACTool
###########################################################################
class WIZnetMACTool ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 646,435 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer_root = wx.BoxSizer( wx.VERTICAL )
        
        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText_serialPort = wx.StaticText( self, wx.ID_ANY, u"Serial Port", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_serialPort.Wrap( -1 )
        bSizer5.Add( self.m_staticText_serialPort, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        m_comboBox_serialCOMChoices = []
        self.m_comboBox_serialCOM = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBox_serialCOMChoices, 0 )
        bSizer5.Add( self.m_comboBox_serialCOM, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText_baudrate = wx.StaticText( self, wx.ID_ANY, u"Baudrate", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_baudrate.Wrap( -1 )
        bSizer5.Add( self.m_staticText_baudrate, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        m_comboBox_baudrateChoices = [ u"4800", u"9600", u"14400", u"19200", u"38400", u"57600", u"115200" ]
        self.m_comboBox_baudrate = wx.ComboBox( self, wx.ID_ANY, u"57600", wx.DefaultPosition, wx.DefaultSize, m_comboBox_baudrateChoices, 0 )
        bSizer5.Add( self.m_comboBox_baudrate, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_button_SerialConnect = wx.Button( self, wx.ID_ANY, u"Connect", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.m_button_SerialConnect, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_button_SerialClose = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button_SerialClose.Enable( False )
        
        bSizer5.Add( self.m_button_SerialClose, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer_root.Add( bSizer5, 0, wx.EXPAND, 5 )
        
        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText_mac_addr = wx.StaticText( self, wx.ID_ANY, u"MAC", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_mac_addr.Wrap( -1 )
        bSizer2.Add( self.m_staticText_mac_addr, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_textCtrl_mac_addr = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_textCtrl_mac_addr, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText_StartHeader = wx.StaticText( self, wx.ID_ANY, u"Start Header", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_StartHeader.Wrap( -1 )
        bSizer2.Add( self.m_staticText_StartHeader, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_textCtrl_StartHeader = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_textCtrl_StartHeader, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText_EndHeader = wx.StaticText( self, wx.ID_ANY, u"End Heaer", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_EndHeader.Wrap( -1 )
        bSizer2.Add( self.m_staticText_EndHeader, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_textCtrl_EndHeader = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_textCtrl_EndHeader, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_button_writeMAC = wx.Button( self, wx.ID_ANY, u"Write MAC", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_button_writeMAC, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer_root.Add( bSizer2, 0, wx.EXPAND, 5 )
        
        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_checkBox_mac_type1 = wx.CheckBox( self, wx.ID_ANY, u"Type1 : 00:08:DC:00:00:00", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_checkBox_mac_type1.SetValue(True) 
        bSizer6.Add( self.m_checkBox_mac_type1, 0, wx.ALL, 5 )
        
        self.m_checkBox_mac_type2 = wx.CheckBox( self, wx.ID_ANY, u"Type2 : 0008DC000000", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.m_checkBox_mac_type2, 0, wx.ALL, 5 )
        
        
        bSizer_root.Add( bSizer6, 0, 0, 5 )
        
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_textCtrl_SerialMonitor = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.TE_MULTILINE )
        bSizer3.Add( self.m_textCtrl_SerialMonitor, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer_root.Add( bSizer3, 1, wx.EXPAND, 5 )
        
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_textCtrl_SerialInput = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.m_textCtrl_SerialInput, 1, wx.ALL, 5 )
        
        self.m_button_SendSerial = wx.Button( self, wx.ID_ANY, u"Send", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.m_button_SendSerial, 0, wx.ALL, 5 )
        
        
        bSizer_root.Add( bSizer4, 0, wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer_root )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.Bind( wx.EVT_ACTIVATE, self.StartApp )
        self.m_comboBox_serialCOM.Bind( wx.EVT_LEFT_DOWN, self.onSerialPort )
        self.m_button_SerialConnect.Bind( wx.EVT_BUTTON, self.onSerialConnect )
        self.m_button_SerialClose.Bind( wx.EVT_BUTTON, self.onSerialClose )
        self.m_button_writeMAC.Bind( wx.EVT_BUTTON, self.onWriteMAC )
        self.m_checkBox_mac_type1.Bind( wx.EVT_CHECKBOX, self.onCheckBox_Type1 )
        self.m_checkBox_mac_type2.Bind( wx.EVT_CHECKBOX, self.onCheckBox_Type2 )
        self.m_button_SendSerial.Bind( wx.EVT_BUTTON, self.onSerialSend )

        # User
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.SerialMonitoring, self.timer)
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def StartApp( self, event ):
        self.GetComPortList()

        if os.path.isfile("config.ini"):
            f = open("config.ini","r")
            while True:
                str_config = f.readline()
                if str_config[0] != '#':
                    break
            f.close()
        else:
            f = open("config.ini","w")
            f.write("# MAC_ADDRESS,BAUD_RATE,START_HEADER,END_HEADER\r\n")
            str_config = "00:08:DC:00:00:00,57600,MC,,"
            f.write(str_config)
            f.close()
        
        mac_addr = str_config.split(',')[0]
        if mac_addr.count(':') == 5:
            self.m_checkBox_mac_type1.SetValue(True)
            self.m_checkBox_mac_type2.SetValue(False)
        elif mac_addr.count(':') == 0:
            self.m_checkBox_mac_type1.SetValue(False)
            self.m_checkBox_mac_type2.SetValue(True)
        else:
            wx.MessageBox("File information is wrong", 'Warning',wx.OK | wx.ICON_ERROR)
            return
            
        self.m_textCtrl_mac_addr.SetValue(str_config.split(',')[0])
        self.m_comboBox_baudrate.SetValue(str_config.split(',')[1])
        self.m_textCtrl_StartHeader.SetValue(str_config.split(',')[2])
        self.m_textCtrl_EndHeader.SetValue(str_config.split(',')[3])
        
    def onSerialPort( self, event ):
        self.GetComPortList()
    
    def onSerialConnect( self, event ):
        com = self.m_comboBox_serialCOM.GetValue()
        baud = int(self.m_comboBox_baudrate.GetValue())
        if com =='':
            wx.MessageBox("Please Select Serial Port", 'Warning',wx.OK | wx.ICON_ERROR)
            return
        
        self.ser = serial.Serial(com, baud, timeout = 0.3)
        if(self.ser == -1):
            self.ser.close()
            wx.MessageBox("Serial Open Error.\r\n", 'Warning',wx.OK | wx.ICON_ERROR)
            return
        
        self.m_button_SerialConnect.Disable()
        self.m_button_SerialClose.Enable()
        self.m_serialIsOpen = True
        
        self.timer.Start(500)
        

    def onSerialClose( self, event ):
        self.timer.Stop()
        self.ser.close()
        self.m_button_SerialConnect.Enable()
        self.m_button_SerialClose.Disable()
        self.m_serialIsOpen = False
    

    def onWriteMAC( self, event ):
        command = self.m_textCtrl_StartHeader.GetValue()
        command += self.m_textCtrl_mac_addr.GetValue()
        command += "\r\n\r\n"
        self.ser.write(command)
        
        if self.m_checkBox_mac_type1.IsChecked():
            mac = self.m_textCtrl_mac_addr.GetValue()
            r = int(mac.replace(':',''),16) + 1
            mac = '{:X}'.format(r).zfill(12)
            self.m_textCtrl_mac_addr.SetValue(":".join(x+y for x,y in zip(mac[::2],mac[1::2])))
        else:
            mac = self.m_textCtrl_mac_addr.GetValue()
            r = int(mac.replace(':',''),16) + 1
            mac = '{:X}'.format(r).zfill(12)
            self.m_textCtrl_mac_addr.SetValue(mac)

    def onCheckBox_Type1( self, event ):
        mac = self.m_textCtrl_mac_addr.GetValue()
        self.m_textCtrl_mac_addr.SetValue(":".join(x+y for x,y in zip(mac[::2],mac[1::2])))
        self.m_checkBox_mac_type2.SetValue(False)
    
    def onCheckBox_Type2( self, event ):
        mac = self.m_textCtrl_mac_addr.GetValue()
        self.m_textCtrl_mac_addr.SetValue(mac.replace(':',''))
        self.m_checkBox_mac_type1.SetValue(False)

    def onSerialSend( self, event ):
        cmd = self.m_textCtrl_SerialInput.GetValue()
        self.ser.write(cmd)

    def SerialMonitoring(self,event):
        self.m_textCtrl_SerialMonitor.AppendText(self.ser.readall().decode('utf-8'))
        
    def GetComPortList(self):
        comboBox_serial_portChoices = []
        
        self.available_ports = list(serial.tools.list_ports.comports())
        for self.port in self.available_ports:
            if(self.port[2] != 'n/a'):
                comboBox_serial_portChoices.append(self.port[0])
                 
        self.m_comboBox_serialCOM.SetItems(comboBox_serial_portChoices)


if __name__ == "__main__":
    app = wx.App(0)
    wiz_mac_tool = WIZnetMACTool(None)
    app.SetTopWindow(wiz_mac_tool)
    wiz_mac_tool.Show()
    app.MainLoop()