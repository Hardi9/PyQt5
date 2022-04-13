from sqlite3 import Cursor
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5.uic import loadUi


class R_form(QDialog):
    def __init__(self):
        super(R_form,self).__init__()
        loadUi("Registrationform.ui",self)
        self.b1.clicked.connect(self.rform)
        
    def rform(self):
        fna=self.Tb1.text()
        mna=self.Tb2.text()
        ln=self.Tb3.text()
        age=self.Tb4.text()
        bod=self.Tb5.text()
        addre=self.Tb6.text()
        cn=self.Tb7.text()
        email=self.Tb8.text()
        
       
      
        
        
        cursor.execute("select * from reglist where fname='"+  fna  +"' and mname='"+ mna +"' and lname='"+ ln +"' and age='"+ age +"' and bdate='"+ bod +"' and address='"+ addre +"' and phone='"+ cn +"' and email='"+ email +"' " )
        #query="insert into reglist values({},{})".values(fna,mna)
        result=cursor.fetchone()
        
        """if result:
            QMessageBox.information(self,"Registration form","Congo!! You Register Successfully.")
        else:
            #QMessageBox.information(self,"Registration form","Congo!!")
            cursor.execute("insert into reglist values('"+ fna +"' ,'"+ mna + "','" + ln +"')")
            """
       # db.execute(query)
        db.commit()
        QMessageBox.information(self,"Registrationform","Congo!! You Register Successfully.")    
        
        cursor.close()
        db.close()
        
app=QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()
regform=R_form()
widget.addWidget(regform)
widget.setCurrentIndex(0)
widget.setFixedWidth(800)
widget.setFixedHeight(1500)
widget.show()



app.exec_()
