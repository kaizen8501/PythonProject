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
import threading
import filecmp

class Unit1RecvThread(threading.Thread):
    def __init__(self, wxObject):
        threading.Thread.__init__(self)
        self.wxObject = wxObject
        self.start()
    
    def run(self):
        self.wxObject.m_listBox_ResultUnit2.Append("Test Start\r\n")
        
        try:
            send_file = open(self.wxObject.filename1,'rb')
            recv_file = open(self.wxObject.m_Unit2_recv_filename,'wb')
            
            for i in xrange(0,self.wxObject.filename1_size,1024):
                data = send_file.read(1024)
                self.wxObject.m_Unit1_ser.write(data)
                recv_data = self.wxObject.m_Unit2_ser.read(1024)
                recv_file.write(recv_data)
                self.wxObject.progressDialog1.Update(i)
            

            send_file.close()
            recv_file.close()
            self.wxObject.progressDialog1.Destroy()

            result = filecmp.cmp(self.wxObject.m_textCtrl_TestFile1.GetValue(), self.wxObject.m_Unit2_recv_filename)
            message = "Received Data : %s\r\n" % str(os.stat(self.wxObject.m_Unit2_recv_filename).st_size)
            self.wxObject.m_listBox_ResultUnit2.Append(message)
            message = "Test Result(File Compare) : %s\r\n" % str(result)
            self.wxObject.m_listBox_ResultUnit2.Append(message)
            
            if result == False:
                wx.MessageBox("Test Fail", 'Warning',wx.OK | wx.ICON_ERROR)
                return

        except Exception as e:
            s = str(e)
            self.wxObject.m_listBox_ResultUnit2.Append(s)
            send_file.close()
            recv_file.close()
            self.wxObject.progressDialog1.Destroy()
            self.wxObject.onSerialClose1()            
            self.wxObject.onSerialClose2()
        

class Unit2RecvThread(threading.Thread):
    def __init__(self, wxObject):
        threading.Thread.__init__(self)
        self.wxObject = wxObject
        self.start()

    def run(self):
        self.wxObject.m_listBox_ResultUnit1.Append("Test Start\r\n")
        
        try:
            send_file = open(self.wxObject.filename2,'rb')
            recv_file = open(self.wxObject.m_Unit1_recv_filename,'wb')
            
            for i in xrange(0,self.wxObject.filename2_size,1024):
                data = send_file.read(1024)
                self.wxObject.m_Unit2_ser.write(data)
                recv_data = self.wxObject.m_Unit1_ser.read(1024)
                recv_file.write(recv_data)
                self.wxObject.progressDialog2.Update(i)
            

            send_file.close()
            recv_file.close()
            self.wxObject.progressDialog2.Destroy()

            result = filecmp.cmp(self.wxObject.m_textCtrl_TestFile2.GetValue(), self.wxObject.m_Unit1_recv_filename)
            message = "Received Data : %s\r\n" % str(os.stat(self.wxObject.m_Unit1_recv_filename).st_size)
            self.wxObject.m_listBox_ResultUnit1.Append(message)
            message = "Test Result(File Compare) : %s\r\n" % str(result)
            self.wxObject.m_listBox_ResultUnit1.Append(message)
            
            if result == False:
                wx.MessageBox("Test Fail", 'Warning',wx.OK | wx.ICON_ERROR)
                return

        except:
            send_file.close()
            recv_file.close()
            self.wxObject.progressDialog2.Destroy()
            self.wxObject.onSerialClose1()            
            self.wxObject.onSerialClose2()    






###########################################################################
## Class S2E_TestTool
###########################################################################

class S2E_TestTool ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"S2E Test Tool", pos = wx.DefaultPosition, size = wx.Size( 500,487 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
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
        
        m_listBox_ResultUnit1Choices = []
        self.m_listBox_ResultUnit1 = wx.ListBox( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox_ResultUnit1Choices, wx.LB_ALWAYS_SB )
        bSizer30.Add( self.m_listBox_ResultUnit1, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        sbSizer4.Add( bSizer30, 1, wx.EXPAND, 5 )
        
        bSizer31 = wx.BoxSizer( wx.HORIZONTAL )
        
        m_listBox_ResultUnit2Choices = []
        self.m_listBox_ResultUnit2 = wx.ListBox( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox_ResultUnit2Choices, wx.LB_ALWAYS_SB )
        bSizer31.Add( self.m_listBox_ResultUnit2, 1, wx.ALL|wx.EXPAND, 5 )
        
        
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
        self.m_button_browse1.Bind( wx.EVT_BUTTON, self.onBrowse1 )
        self.m_button_browse2.Bind( wx.EVT_BUTTON, self.onBrowse2 )
        self.m_button_StartTest.Bind( wx.EVT_BUTTON, self.onStartTest )
        self.m_checkBox_Fullduplex.Bind( wx.EVT_CHECKBOX, self.onFullduplex )
        self.m_checkBox_Unit1toUnit2.Bind( wx.EVT_CHECKBOX, self.onUnit1toUnit2 )
        self.m_checkBox_Unit2toUnit1.Bind( wx.EVT_CHECKBOX, self.onUnit2toUnit1 )
        

        #User Code
        self.GetComPortList(1)
        self.GetComPortList(2)

        self.m_Unit1_ser_IsOpen = False
        self.m_Unit2_ser_IsOpen = False
        self.m_Unit1_recv_filename = "Unit1_Rx_File.txt"
        self.m_Unit2_recv_filename = "Unit2_Rx_File.txt"
        
        
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
        
        self.m_Unit1_ser = serial.Serial(com, baud, timeout = 0.3)
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
        
        self.m_Unit2_ser = serial.Serial(com, baud, timeout = 0.3)
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
        self.filename1 = self.m_textCtrl_TestFile1.GetValue()
        if self.filename1 == '':
            return
        
        self.filename1_size = os.stat(self.filename1).st_size
        self.progressDialog1 = wx.ProgressDialog('Send File','Unit1 send data to Unit2',self.filename1_size,
                                           style = wx.PD_ELAPSED_TIME | wx.PD_REMAINING_TIME )
        
        self.filename2 = self.m_textCtrl_TestFile2.GetValue()
        if self.filename2 == '':
            return
        
        self.filename2_size = os.stat(self.filename2).st_size
        self.progressDialog2 = wx.ProgressDialog('Send File','Unit2 send data to Unit1',self.filename2_size,
                                           style = wx.PD_ELAPSED_TIME | wx.PD_REMAINING_TIME )
        
        if self.m_checkBox_Unit1toUnit2.GetValue() == True:
            Unit1RecvThread(self)
           
        if self.m_checkBox_Unit2toUnit1.GetValue() == True:
            Unit2RecvThread(self)

        if self.m_checkBox_Fullduplex.GetValue() == True:
            Unit1RecvThread(self)
            Unit2RecvThread(self)
        
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

        
if __name__ == "__main__":
    app = wx.App(0)
    s2e_test = S2E_TestTool(None)
    app.SetTopWindow(s2e_test)
    s2e_test.Show()
    app.MainLoop()