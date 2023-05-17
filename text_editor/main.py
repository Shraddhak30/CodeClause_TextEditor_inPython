from tkinter import *
from tkinter.ttk import *
from tkinter import font,colorchooser,filedialog,messagebox
import os
import tempfile
from datetime import datetime


#Functionality 
def date_time(event=None):
    currdatetime=datetime.now()
    formatdatetime=currdatetime.strftime('%B %d, %Y %H:%M:%S')
    textarea.insert(1.0,formatdatetime)


def change_theme(fg_color,bg_color):
    textarea.config(fg=fg_color,bg=bg_color)

def toolbarfunc():
    if show_toolbar.get()==False:
        tool_barv.pack_forget()

    if show_toolbar.get()==True:
        textarea.pack_forget()
        tool_barv.pack(fill=X)
        textarea.pack(fill=BOTH,expand=1)

def statusbarFunc():
    if show_statusbar.get()==False:
        status_barv.pack_forget()
    
    else:
        status_barv.pack()

   


    

def findf():
    def find_button():
        textarea.tag_remove('match',1.0,END)
        start_pos='1.0'
        findentry=entryf.get()
        if findentry:
            while True:
                start_pos=textarea.search(findentry,start_pos,stopindex=END)
                if not start_pos:
                    break
                end_pos=f'{start_pos}+{len(findentry)}c'
                textarea.tag_add('match',start_pos,end_pos)

                textarea.tag_config('match',foreground='red',background='yellow')
                start_pos=end_pos

    def replace_text():
        findentry=entryf.get()
        replaceword=entryr.get()
        content=textarea.get(1.0,END)
        new_content=content.replace(findentry,replaceword)
        textarea.delete(1.0,END)
        textarea.insert(1.0,new_content)




    root1=Toplevel()
    root1.title('Find')
    root1.geometry('450x250+500+200')
    root1.resizable(False,False)

    labelFrame=LabelFrame(root1,text='Find/Replace')
    labelFrame.pack(pady=20)

    findLabel=Label(labelFrame,text='Find')
    findLabel.grid(row=0,column=0,padx=5,pady=5)
    entryf=Entry(labelFrame)
    entryf.grid(row=0,column=1)

    replaceLabel=Label(labelFrame,text='Replace')
    replaceLabel.grid(row=1,column=0,padx=5,pady=5)
    entryr=Entry(labelFrame)
    entryr.grid(row=1,column=1)

    fbtn=Button(labelFrame,text='Find',command=find_button)
    fbtn.grid(row=2,column=0,padx=5,pady=10)

    rbtn=Button(labelFrame,text='Replace',command=replace_text)
    rbtn.grid(row=2,column=1,padx=5,pady=10)

    def doSomething():
        textarea.tag_remove('match',1.0,END)
        root1.destroy()
    root1.protocol('WM_DELETE_WINDOW',doSomething)

    root1.mainloop()

    

def statusbarfunc(event):
    if textarea.edit_modified():
        sbr=len(textarea.get(0.0,END).split())
        characters=len(textarea.get(0.0,'end-1c').replace('',''))
        status_barv.config(text=f'Characters:{characters}  Words:{sbr}')
    textarea.edit_modified(False)
url=''
def new_file(event=None):
    global url
    url=''
    textarea.delete(0.0,END)


def open_file(event=None):
    global url
    url=filedialog.askopenfilename(initialdir=os.getcwd,title='Select File',filetypes=(('Text File','txt'),('All Files','*.*')))
    
    if url !='':
        data=open(url,'r')
        textarea.insert(0.0,data.read())
    root.title(os.path.basename(url))

def save_file(event=None):
    if url=='':
        save_url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','txt'),('All files','*.*')))
        if save_url is None:
            pass
        else:
            content=textarea.get(0.0,END)
            save_url.write(content)
            save_url.close()

    else:
        content=textarea.get(0.0,END)
        file=open(url,'w')
        file.write(content)

def saveas_file(event=None):
     save_url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','txt'),('All files','*.*')))
     content=textarea.get(0.0,END)
     save_url.write(content)
     save_url.close()
     if url!='':
         os.remove(url)

def print_file(event=None):
    file=tempfile.mktemp('.txt')
    open(file,'w').write(textarea.get(1.0,END))
    os.startfile(file,'print')

def iexit(event=None):
    if textarea.edit_modified():
        result=messagebox.askyesnocancel('Warning','Do you want to save the file?')
        if result is True:
            if url!='':
                content=textarea.get(0.0,END)
                file=open(url,'w')
                file.write(content)
                root.destroy()

            else:
                content=textarea.get(0.0,END)
                save_url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','txt'),('All files','*.*')))
                save_url.write(content)
                save_url.close()
                root.destroy()

        elif result is False:
            root.destroy()

        else:
            pass

    else:
        root.destroy()





fontSize=12
fontStyle='arial'
def font_style(event):
    global fontStyle
    fontStyle=font_fam_var.get()
    textarea.config(font=(fontStyle,fontSize))

def font_size(event):
    global fontSize
    fontSize=size_var.get()
    textarea.config(font=(fontStyle,fontSize))

def bold_text():
    text_property=font.Font(font=textarea['font']).actual()
    if text_property['weight']=='normal':
        textarea.config(font=(fontStyle,fontSize,'bold'))

    if text_property['weight']=='bold':
        textarea.config(font=(fontStyle,fontSize,'normal'))

def italic_text():
    text_property=font.Font(font=textarea['font']).actual()
    if text_property['slant']=='roman':
        textarea.config(font=(fontStyle,fontSize,'italic'))

    if text_property['slant']=='italic':
        textarea.config(font=(fontStyle,fontSize,'roman'))

def underline_text():
    text_property=font.Font(font=textarea['font']).actual()
    if text_property['underline']==0:
        textarea.config(font=(fontStyle,fontSize,'underline'))

    if text_property['underline']==1:
        textarea.config(font=(fontStyle,fontSize))

def colorselect():
    color=colorchooser.askcolor()
    textarea.config(fg=color[1])

def right_align():
    data=textarea.get(0.0,END)
    textarea.tag_config('right',justify=RIGHT)
    textarea.delete(0.0,END)
    textarea.insert(INSERT,data,'right')

def left_align():
    data=textarea.get(0.0,END)
    textarea.tag_config('left',justify=LEFT)
    textarea.delete(0.0,END)
    textarea.insert(INSERT,data,'left')

def center_align():
    data=textarea.get(0.0,END)
    textarea.tag_config('center',justify=CENTER)
    textarea.delete(0.0,END)
    textarea.insert(INSERT,data,'center')



root=Tk()
root.title("TEXT EDITOR")
root.geometry("1280x720+10+10")
#root.resizable(False,True)
menubar=Menu(root)
root.config(menu=menubar)


#FILEMENU
filemenu=Menu(menubar,tearoff=False)
menubar.add_cascade(label='File',menu=filemenu)
new=PhotoImage(file='new.png')
filemenu.add_command(label='New File',accelerator='Ctrl+N',image=new,compound=LEFT,command=new_file)
openf=PhotoImage(file='open.png')
filemenu.add_command(label='Open File',accelerator='Ctrl+O',image=openf,compound=LEFT,command=open_file)
save=PhotoImage(file='save.png')
filemenu.add_command(label='Save',accelerator='Ctrl+S',image=save,compound=LEFT,command=save_file)
saveas=PhotoImage(file='save_as.png')
filemenu.add_command(label='Save As',accelerator='Ctrl+Alt+S',image=saveas,compound=LEFT,command=saveas_file)
printimg=PhotoImage(file='print.png')
filemenu.add_command(label='Print',accelerator='Ctrl+P',image=printimg,compound=LEFT,command=print_file)
filemenu.add_separator()
exit=PhotoImage(file='exit.png')
filemenu.add_command(label='Exit',accelerator='Ctrl+Q',image=exit,compound=LEFT,command=iexit)





#toolbar

tool_barv=Label(root)
tool_barv.pack(side=TOP,fill=X)
font_families=font.families()
font_fam_var=StringVar()
fontfam=Combobox(tool_barv,width=30,values=font_families,state='readonly',textvariable=font_fam_var)
fontfam.grid(row=0,column=0,padx=5)
fontfam.current(font_families.index('Arial'))



size_var=IntVar()
fontsize=Combobox(tool_barv,width=15,textvariable=size_var,state='readonly',values=tuple(range(8,81)))
fontsize.current(4)
fontsize.grid(row=0,column=1,padx=5)

fontfam.bind('<<ComboboxSelected>>',font_style)
fontsize.bind('<<ComboboxSelected>>',font_size)

#button

bold=PhotoImage(file='bold.png')
boldbtn=Button(tool_barv,image=bold,command=bold_text)
boldbtn.grid(row=0,column=2,padx=5)

italic=PhotoImage(file='italic.png')
ibtn=Button(tool_barv,image=italic,command=italic_text)
ibtn.grid(row=0,column=3,padx=5)

uline=PhotoImage(file='underline.png')
ubtn=Button(tool_barv,image=uline,command=underline_text)
ubtn.grid(row=0,column=4,padx=5)

fontcolor=PhotoImage(file='font_color.png')
fcbtn=Button(tool_barv,image=fontcolor,command=colorselect)
fcbtn.grid(row=0,column=5,padx=5)

leftalign=PhotoImage(file='left.png')
labtn=Button(tool_barv,image=leftalign,command=left_align)
labtn.grid(row=0,column=6,padx=5)

rightalign=PhotoImage(file='right.png')
rabtn=Button(tool_barv,image=rightalign,command=right_align)
rabtn.grid(row=0,column=7,padx=5)

centeralign=PhotoImage(file='center.png')
cabtn=Button(tool_barv,image=centeralign,command=center_align)
cabtn.grid(row=0,column=8,padx=5)

scrollbar=Scrollbar(root)
scrollbar.pack(fill=Y,side=RIGHT)
textarea=Text(root,yscrollcommand=scrollbar.set,font=('arial',12),undo=True)
textarea.pack(fill=BOTH,expand=True)
scrollbar.config(command=textarea.yview)

status_barv=Label(root,text='STATUS BAR')
status_barv.pack(side=BOTTOM)

textarea.bind('<<Modified>>',statusbarfunc)

#EDIT MENU

editmenu=Menu(menubar,tearoff=False)
menubar.add_cascade(label='Edit',menu=editmenu)
undo=PhotoImage(file='undo.png')
editmenu.add_command(label='Undo',accelerator='Ctrl+Z',image=undo,compound=LEFT,command=lambda :textarea.event_generate('<Control z>'))
cut=PhotoImage(file='cut.png')
editmenu.add_command(label='Cut',accelerator='Ctrl+X',image=cut,compound=LEFT,command=lambda :textarea.event_generate('<Control x>'))
copy=PhotoImage(file='copy.png')
editmenu.add_command(label='Copy',accelerator='Ctrl+C',image=copy,compound=LEFT,command=lambda :textarea.event_generate('<Control c>'))
paste=PhotoImage(file='paste.png')
editmenu.add_command(label='Paste',accelerator='Ctrl+V',image=paste,compound=LEFT,command=lambda :textarea.event_generate('<Control v>'))
selectall=PhotoImage(file='selectall.png')
editmenu.add_command(label='Select All',accelerator='Ctrl+A',image=selectall,compound=LEFT,command=lambda :textarea.event_generate('<Control a>'))
clear=PhotoImage(file='clear_all.png')
editmenu.add_command(label='Clear',accelerator='Ctrl+Alt+X',image=clear,compound=LEFT,command=lambda :textarea.delete(0.0,END))
datetimeimg=PhotoImage(file='schedule.png')
editmenu.add_command(label='Date & Time',accelerator='Ctr+D',image=datetimeimg,compound=LEFT,command=date_time)

#VIEW MENU

viewmenu=Menu(menubar,tearoff=False)
menubar.add_cascade(label='View',menu=viewmenu)
show_toolbar=BooleanVar()
show_toolbar.set(True)
tool=PhotoImage(file='tool_bar.png')
viewmenu.add_checkbutton(label='Tool Bar',variable=show_toolbar,onvalue=True,offvalue=False,image=tool,compound=LEFT,command=toolbarfunc)
show_statusbar=BooleanVar()
show_statusbar.set(True)
statusbar=PhotoImage(file='status_bar.png')
viewmenu.add_checkbutton(label='Status Bar',variable=show_statusbar,onvalue=True,offvalue=False,image=statusbar,compound=LEFT,
                         command=statusbarFunc)

#THEME

themesmenu=Menu(menubar,tearoff=False)
menubar.add_cascade(label='Color Theme',menu=themesmenu)
themechoice=StringVar()
light=PhotoImage(file='light_default.png')
themesmenu.add_radiobutton(label='Light (Default)',image=light,compound=LEFT,command=lambda:change_theme('black','white'))
dark=PhotoImage(file='dark.png')
themesmenu.add_radiobutton(label='Dark',image=dark,compound=LEFT,command=lambda:change_theme('gray70','black'))
pink=PhotoImage(file='red.png')
themesmenu.add_radiobutton(label='Pink',image=pink,compound=LEFT,command=lambda:change_theme('black','pink'))
monokai=PhotoImage(file='monokai.png')
themesmenu.add_radiobutton(label='Monokai',image=monokai,compound=LEFT,command=lambda:change_theme('black','orange'))


root.bind("<Control-o>",open_file)
root.bind("<Control-n>",new_file)
root.bind("<Control-s>",save_file)
root.bind("<Control-Alt-s>",saveas_file)
root.bind("<Control-q>",iexit)
root.bind("<Control-p>",print_file)
root.bind("<Control-d>",date_time)







root.mainloop()

