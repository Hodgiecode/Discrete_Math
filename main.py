from tkinter import *
from datetime import datetime
from tkinter import ttk

import os
path = os.path.dirname(os.path.dirname(__file__))


from handler import handler_task_list,generate_test
from little_calc import sub_block,basic

'''чтобы работало Вырезать+Вставить в окне программы'''

class Graphic_interface():
    def subprocess_cmd(self,command):
        process = run(command, stdout=PIPE, stderr=PIPE,shell=True)
        return process.returncode

    ############3
    def tasklist(self,value):
        self.in_entry_mid_right.delete(1.0,END)
        if value=="Алгебра логики":
            self.combo.pack_forget()
            self.doc = StringVar(self.frame_for_in_entry)
            self.doc.set("Выберите задачу")
            self.combo = OptionMenu(self.frame_for_in_entry, self.doc,'Монотонность','Линейность','Самодвойственность','Шефферовость','Базис','Полином Жегалкина','Оболочка' ,command=self.tasklist)
            self.combo.pack()

        if value=="K-значная логика":
            self.combo.pack_forget()
            self.doc = StringVar(self.frame_for_in_entry)
            self.doc.set("Выберите задачу")
            self.combo = OptionMenu(self.frame_for_in_entry, self.doc,'Монотонность','Сохранение','Сохранение 2','Сохранение 3','Шефферовость','Оболочка',command=self.tasklist)
            self.combo.pack()

        if value=="Автоматы":
            self.combo.pack_forget()
            self.doc = StringVar(self.frame_for_in_entry)
            self.doc.set("Выберите задачу")
            self.combo = OptionMenu(self.frame_for_in_entry, self.doc,'Состояния','Эквивалентность','Суперпозиция',command=self.tasklist)
            self.combo.pack()

        if value=="Миним.булевых функций":
            self.combo.pack_forget()
            self.doc = StringVar(self.frame_for_in_entry)
            self.doc.set("Выберите задачу")
            self.combo = OptionMenu(self.frame_for_in_entry, self.doc,'Алгоритм Квайна-МакКласки','Алгоритм Блейка','Алгоритм Блейка 2','Ядро','Тупиковые ДНФ',command=self.tasklist)
            self.combo.pack()

    def write_to_file(self):
        v=self.in_entry_down.get(1.0,END).strip()
        if self.doc0.get()!="Выберите раздел" and self.doc.get()!="Выберите задачу":
            v1=self.doc0.get()
            v2=self.doc.get()
            t=generate_test(v1,v2)
            for i in range(len(t)):
                f=open("test_"+str(i+1)+".txt","w",encoding="utf-8")
                f.write(t[i][0])
                f.close()

                f=open("ans_"+str(i+1)+".txt","w",encoding="utf-8")
                f.write(t[i][1])
                f.close()
        else:
            self.in_entry_down.insert(1.0,"Необходимо выбрать раздел и задачу из этого раздела")
        
        
    def test_generate(self):
        self.in_entry_mid_right.delete(1.0,END)
        v=self.in_entry_down.get(1.0,END).strip()
        if self.doc0.get()!="Выберите раздел" and self.doc.get()!="Выберите задачу":
            v1=self.doc0.get()
            v2=self.doc.get()
            t=generate_test(v1,v2)
            for i in range(len(t)):
                self.in_entry_mid_right.insert(END,"Тест "+str(i+1)+"\n")
                self.in_entry_mid_right.insert(END,t[i][0])
                self.in_entry_mid_right.insert(END,'\n\n')
                
        else:
            self.in_entry_down.insert(1.0,"Необходимо выбрать раздел и задачу из этого раздела")
            

    ####

    def create(self):
        self.open_option=0
        self.master=Tk()
        self.master.title("Anti DE v1.0")
        self.master.state('zoomed')
        self.master.bind_all("<Key>", self._onKeyRelease, "+")

        self.menu=Menu(self.master)
        self.master.config(menu=self.menu)
        
        filemenu=Menu(self.menu,tearoff=0)
        helpmenu=Menu(self.menu,tearoff=0)

        self.menu.add_command(label='Help')
        self.menu.add_command(label='Exit',command=self.master.destroy)
       
        self.frame_up=Frame(self.master)
        self.frame_up.pack()

        self.frame_down=Frame(self.master)
        self.frame_down.pack()

        self.frame_for_down=Frame(self.frame_down)
        self.frame_for_down.pack(side=BOTTOM)

        self.frame_for_down_temp=Frame(self.frame_for_down)
        self.frame_for_down_temp.pack()
        self.frame_for_down_temp.pack_forget()

        self.frame_for_button=Frame(self.frame_down)
        self.frame_for_button.pack(side=RIGHT)

        self.frame_for_in_entry=Frame(self.frame_up)
        self.frame_for_in_entry.pack(side=TOP)

        self.frame_for_button_one=Frame(self.frame_for_button)
        self.frame_for_button_one.pack(side=LEFT)

        self.frame_for_button_two=Frame(self.frame_for_button)
        self.frame_for_button_two.pack(side=RIGHT)

        self.in_entry=Text(self.frame_for_in_entry,height=2,width=120)
        self.in_entry.pack(side=LEFT,ipadx=10,ipady=5,padx=10,pady=5)

        self.in_entry_mid_left=Text(self.frame_up,height=29,width=60)
        self.in_entry_mid_left.pack(side=LEFT,fill = "both", expand = "yes",ipadx=10,ipady=5,padx=10,pady=5)

        self.in_entry_mid_right=Text(self.frame_up,height=29,width=30)
        self.in_entry_mid_right.pack(side=RIGHT,fill = "both", expand = "yes",ipadx=10,ipady=5,padx=10,pady=5)

        self.in_entry_down=Text(self.frame_down,height=3,width=97)
        self.in_entry_down.pack(side=LEFT,ipadx=10,ipady=5,padx=10,pady=5)

        self.doc0 = StringVar(self.frame_for_in_entry)
        self.doc0.set("Выберите раздел")
        self.combo_task = OptionMenu(self.frame_for_in_entry, self.doc0, "Выберите раздел","Алгебра логики", "K-значная логика", "Автоматы", "Миним.булевых функций",command=self.tasklist)
        self.combo_task.pack()

        self.button_ps = Button(self.frame_for_button_one, text='Parse', width=10,command=self.parse_formula)
        self.button_ps.pack(padx=10,pady=5)

        self.button_test = Button(self.frame_for_button_two, text='Генерация\nтестов', width=10,command=self.test_generate)
        self.button_test.pack(padx=10,pady=5)

        #self.button_edit_config = Button(self.frame_for_button_two, text='Edit_config', width=10)
        #self.button_edit_config.pack(padx=10,pady=5)

        #self.button_save_config = Button(self.frame_for_button_two, text='Save_config', width=10)
        #self.button_save_config.pack(padx=10,pady=5)
        #self.button_save_config.pack_forget()

        self.button_rn = Button(self.frame_for_button, text='Запись\nв файл', width=10,command=self.write_to_file)
        self.button_rn.pack(padx=10,pady=5)

        #self.button_sop=Button(self.frame_for_button, text='Show options', width=10)
        #self.button_sop.pack(padx=10,pady=5)

        #self.button_hop=Button(self.frame_for_button, text='Hide options', width=10)
        #self.button_hop.pack(padx=10,pady=5)
        #self.button_hop.pack_forget()

        #self.button_pic = Button(self.frame_for_button_one, text='Запись\nв файл', width=10)
        #self.button_pic.pack(padx=10,pady=5)
       
        self.button_cl = Button(self.frame_for_button_one, text='Очистить', width=12)
        self.button_cl.pack(padx=10,pady=5)

        #self.button_ld = Button(self.frame_for_in_entry, text='Load_and_run', width=12)
        #self.button_ld.pack(padx=10,pady=5)
        self.doc = StringVar(self.master)
        self.doc.set("Выберите задачу")
        self.combo = OptionMenu(self.frame_for_in_entry, self.doc, "Выберите задачу")
        self.combo.pack()
        
        self.master.mainloop()

    def _onKeyRelease(self,event):
        ctrl  = (event.state & 0x4) != 0
        
        if event.keycode==88 and  ctrl and event.keysym.lower() != "x": 
            event.widget.event_generate("<<Cut>>")

        if event.keycode==86 and  ctrl and event.keysym.lower() != "v": 
            event.widget.event_generate("<<Paste>>")

        if event.keycode==67 and  ctrl and event.keysym.lower() != "c":
            event.widget.event_generate("<<Copy>>")

    def parse_formula(self):
        s=self.in_entry.get(1.0,END)
        if s!="":
            self.in_entry_mid_right.delete(1.0,END)
            r=sub_block(s)
            self.in_entry_mid_right.insert(END,r[0]+"\n\n")
            self.in_entry_mid_right.insert(END,r[1]+"\n\n")
            self.in_entry_mid_right.insert(END,r[2]+"\n\n")
            self.in_entry_mid_right.insert(END,r[3]+"\n\n")
            self.in_entry_mid_right.insert(END,r[4]+"\n\n")
        else:
            self.in_entry_down.insert(1.0,"Необходимо ввести выражение")
        

       
            
            

 
   
     
   
        
        
   
    

A=Graphic_interface()
A.create()
