import tkinter as tk
import base_convert as bc

# >> ====================================== >> Reset function <<
def reset():
    nm_in.set('')                           # Number: empty string
    ba_fr.set(ba[2])                        # Base From: DEN
    ba_to.set(ba[0])                        # Base From: BIN
    nm_ot.set('')                           # Number: empty string


# >> ====================================== >> Convert function <<
def convert():
    arg1 = ba_fr.get()[:2]                  # Base From
    arg2 = nm_in.get()                      # Number
    arg3 = ba_to.get()[:2]                  # Base To
    result = bc.base_base(arg1,arg2,arg3)   # Convert
    nm_ot.set(result)                       


# >> -------------------------------------- >> Variables <<

root = tk.Tk()                              # Instance of Tk created
root.title('Videorials')                    # Window title set
root.iconbitmap('favicon.ico')              # Default icon replaced
root.resizable(False, False)                # Resize turned off

# >> -------------------------------------- >> Widget Fonts <<

ttl_fnt = ('Calibri', 20, 'bold')           # Frame widget
lbl_fnt = ('Calibri', 13)                   # Label widget
opt_fnt = ('Calibri', 12)                   # Entry widget

# >> -------------------------------------- >> Widget values <<
ba = [' 2 BIN',                             # Base options
      ' 8 OCT',
      '10 DEN',
      '16 HEX']
nm_in = tk.StringVar()                      # Number entry
ba_fr = tk.StringVar()                      # Base From list box
ba_to = tk.StringVar()                      # Base To list box
nm_ot = tk.StringVar()                      # Result entry (readonly)
reset()                                     # Reset above

# >> -------------------------------------- >> Frame (wrapper) <<
frame = tk.LabelFrame(root, text=' Base Converter ')
frame.config(padx=12, pady=10, font=ttl_fnt, fg='#5c5c5c', labelanchor='n')
frame.grid(padx=12, pady=12)

# >> -------------------------------------- >> Number: Label <<
num_lbl = tk.Label(frame, text='Enter number:')
num_lbl.config(font=lbl_fnt, fg='#5c5c5c', anchor='w')
num_lbl.grid(row=0, columnspan=4, sticky='EW')

# >> -------------------------------------- >> Number: Entry <<
num_ent = tk.Entry(frame, textvariable=nm_in)
num_ent.config(font=opt_fnt, fg='#5c5c5c')
num_ent.grid(row=1, columnspan=4, pady=4, ipady=2, sticky='EW')

# >> -------------------------------------- >> Base From: Label <<
ba_fr_lbl = tk.Label(frame, text='From: ')
ba_fr_lbl.config(font=lbl_fnt, fg='#5c5c5c', anchor='e')
ba_fr_lbl.grid(column=0, row=2, padx=0, pady=12, sticky='E')

# >> -------------------------------------- >> Base From: Option Menu <<
ba_fr_cmb = tk.OptionMenu(frame, ba_fr, *ba)
ba_fr_cmb.config(font=opt_fnt, fg='#5c5c5c', width=12, anchor='w')
ba_fr_cmb.grid(column=1, row=2, columnspan=3)

# >> -------------------------------------- >> Base To: Label <<
ba_to_lbl = tk.Label(frame, text='To: ')
ba_to_lbl.config(font=lbl_fnt, fg='#5c5c5c', anchor='e')
ba_to_lbl.grid(column=0, row=3, padx=0, pady=6, sticky='EW')

# >> -------------------------------------- >> Base To: Option Menu <<
ba_to_cmb = tk.OptionMenu(frame, ba_to, *ba)
ba_to_cmb.config(font=opt_fnt, fg='#5c5c5c', width=12, anchor='w')
ba_to_cmb.grid(column=1, row=3, columnspan=3)

# >> -------------------------------------- >> Convert: Button <<
cv_but = tk.Button(frame, text='Convert', command=convert)
cv_but.config(font=opt_fnt, fg='#5c5c5c')
cv_but.grid(column=0, row=4, columnspan=2, pady=12, sticky='EW')

# >> -------------------------------------- >> Reset: Button <<
rs_but = tk.Button(frame, text='Reset', command=reset)
rs_but.config(font=opt_fnt, fg='#5c5c5c')
rs_but.grid(column=2, row=4, columnspan=2, pady=12, sticky='EW')

# >> -------------------------------------- >> Result: Label <<
num_lbl = tk.Label(frame, text='Result')
num_lbl.config(font=lbl_fnt, fg='#5c5c5c', anchor='w')
num_lbl.grid(column=0, row=5, columnspan=4, sticky='EW')

# >> -------------------------------------- >> Result: Entry (readonly) <<
num_out = tk.Entry(frame, textvariable=nm_ot, state='readonly')
num_out.config(font=opt_fnt, fg='#5c5c5c', readonlybackground='white')
num_out.grid(column=0, row=6, columnspan=4, ipady=2, sticky='EW')

root.mainloop()
