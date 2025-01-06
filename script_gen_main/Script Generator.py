import tkinter
import customtkinter
from PIL import Image
from ctkdlib.custom_widgets import *

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

HEIGHT = 900
WIDTH = 700

root = customtkinter.CTk()
root.title("Meta-Script Generator v0.2 - D Graham 2024")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.resizable(False, False)


entry_frame = customtkinter.CTkFrame(master=root, width=340, height=886, border_width=3, border_color="#474747")
entry_frame.place(x=7, y=8)

feedback_pane = customtkinter.CTkFrame(master=root, width=340, height=886, border_width=3, border_color="#474747")
feedback_pane.place(x=354, y=8)

Label1 = customtkinter.CTkLabel(
    master=root,
    bg_color=[
        'gray86',
        'gray17'],
    font=customtkinter.CTkFont(
        'Service Interface / SIP Binding',
        size=22,
        weight='bold'),
    text="Service Interface / SIP Binding",
    text_color="#3698cd",
    text_color_disabled="#3698cd")
Label1.place(x=24, y=13)

Label2 = customtkinter.CTkLabel(
    master=root,
    bg_color=[
        'gray86',
        'gray17'],
    font=customtkinter.CTkFont(
        'Roboto',
        size=22,
        weight='bold'),
    text="Error / Preview",
    text_color="#3698cd",
    text_color_disabled="#3698cd")
Label2.place(x=446, y=15)

preview_pane = customtkinter.CTkTextbox(
    master=root,
    bg_color=[
        'gray86',
        'gray17'],
    width=318,
    height=729,
    border_width=2)
preview_pane.place(x=365, y=48)
preview_pane.insert(1.0, '')

Label3 = customtkinter.CTkLabel(master=root, bg_color=['gray86', 'gray17'], text="Service Interface Number")
Label3.place(x=14, y=40)

serv_int_num = customtkinter.CTkEntry(master=root, bg_color=['gray86', 'gray17'], width=234, placeholder_text="")
serv_int_num.place(x=14, y=64)
CTkTooltip(serv_int_num, text='Example VID112', delay=1.5)

Label4 = customtkinter.CTkLabel(master=root, bg_color=['gray86', 'gray17'], text="Port Group 1-4")
Label4.place(x=14, y=98)

port_group = customtkinter.CTkEntry(master=root, bg_color=['gray86', 'gray17'], width=234)
port_group.place(x=14, y=121)
CTkTooltip(port_group, text='Number 1 to 4', delay=1.5)

Label5 = customtkinter.CTkLabel(master=root, bg_color=['gray86', 'gray17'], text="Subnet Prefix Length")
Label5.place(x=14, y=155)

binding_subnet = customtkinter.CTkEntry(master=root, bg_color=['gray86', 'gray17'], width=234)
binding_subnet.place(x=14, y=178)
CTkTooltip(binding_subnet, text='Example 24 for /24', delay=1.5)

Label6 = customtkinter.CTkLabel(master=root, bg_color=['gray86', 'gray17'], text="Nasstar GW Address")
Label6.place(x=14, y=211)

gw_address = customtkinter.CTkEntry(master=root, bg_color=['gray86', 'gray17'], width=234)
gw_address.place(x=14, y=234)

Label7 = customtkinter.CTkLabel(master=root, bg_color=['gray86', 'gray17'], text="Nasstar Signalling Address")
Label7.place(x=14, y=271)

sig_address = customtkinter.CTkEntry(master=root, bg_color=['gray86', 'gray17'], width=234)
sig_address.place(x=14, y=294)

Label8 = customtkinter.CTkLabel(master=root, bg_color=['gray86', 'gray17'], text="Nasstar Media Address")
Label8.place(x=14, y=330)

media_address = customtkinter.CTkEntry(master=root, bg_color=['gray86', 'gray17'], width=234)
media_address.place(x=14, y=353)

Label9 = customtkinter.CTkLabel(master=root, bg_color=['gray86', 'gray17'], text="Service Address Label")
Label9.place(x=14, y=389)

serv_add_label = customtkinter.CTkEntry(master=root, bg_color=['gray86', 'gray17'], width=234)
serv_add_label.place(x=14, y=411)
CTkTooltip(serv_add_label, text='Max 30 chars', delay=1.5)

Label10 = customtkinter.CTkLabel(master=root, bg_color=['gray86', 'gray17'], text="VLAN ID")
Label10.place(x=14, y=448)

vlan_id = customtkinter.CTkEntry(master=root, bg_color=['gray86', 'gray17'], width=234)
vlan_id.place(x=14, y=471)
CTkTooltip(vlan_id, text='Just the number - ie 130', delay=1.5)

Label11 = customtkinter.CTkLabel(master=root, bg_color=['gray86', 'gray17'], text="Realm Label")
Label11.place(x=14, y=510)

realm_label = customtkinter.CTkEntry(master=root, bg_color=['gray86', 'gray17'], width=234)
realm_label.place(x=14, y=534)
CTkTooltip(realm_label, text='Max 30 chars', delay=1.5)

Label12 = customtkinter.CTkLabel(
    master=root,
    bg_color=[
        'gray86',
        'gray17'],
    font=customtkinter.CTkFont(
        'Service Interface / SIP Binding',
        size=22,
        weight='bold'),
    text="Adjacency",
    text_color="#3698cd",
    text_color_disabled="#3698cd")
Label12.place(x=119, y=566)

Label13 = customtkinter.CTkLabel(master=root, bg_color=['gray86', 'gray17'], text="Adjacency Name")
Label13.place(x=14, y=596)

adj_label = customtkinter.CTkEntry(master=root, bg_color=['gray86', 'gray17'], width=234)
adj_label.place(x=14, y=620)
CTkTooltip(adj_label, text='Max 30 Chars', delay=1.5)

Label14 = customtkinter.CTkLabel(master=root, bg_color=['gray86', 'gray17'], text="Account Port")
Label14.place(x=14, y=658)

acct_port = customtkinter.CTkEntry(master=root, bg_color=['gray86', 'gray17'], width=234)
acct_port.place(x=14, y=682)
CTkTooltip(acct_port, text='For port 3 & 4 enter in format 34', delay=1.5)

Label15 = customtkinter.CTkLabel(master=root, bg_color=['gray86', 'gray17'], text="Customer End Address")
Label15.place(x=14, y=723)

cust_address = customtkinter.CTkEntry(master=root, bg_color=['gray86', 'gray17'], width=234)
cust_address.place(x=14, y=747)
CTkTooltip(cust_address, text='Example 24 for /24', delay=1.5)

Label16 = customtkinter.CTkLabel(master=root, bg_color=['gray86', 'gray17'], text="Subnet Prefix Length")
Label16.place(x=14, y=786)

cust_subnet = customtkinter.CTkEntry(master=root, bg_color=['gray86', 'gray17'], width=234)
cust_subnet.place(x=14, y=810)
CTkTooltip(cust_subnet, text='Example 24 for /24', delay=1.5)

Label17 = customtkinter.CTkLabel(master=root, bg_color=['gray86', 'gray17'], text="Filename:")
Label17.place(x=367, y=789)

filename_box = customtkinter.CTkEntry(master=root, bg_color=['gray86', 'gray17'], width=257)
filename_box.place(x=427, y=789)
CTkTooltip(filename_box, text='Filename without an extension - will be saved as <name>.txt', delay=1.5)

submit = customtkinter.CTkButton(master=root, bg_color=['gray86', 'gray17'], text="Submit")
submit.place(x=104, y=853)

write_file = customtkinter.CTkButton(master=root, bg_color=['gray86', 'gray17'], text="Write File")
write_file.place(x=455, y=853)

root.mainloop()
