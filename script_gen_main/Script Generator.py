#import tkinter as tk
import customtkinter
import ipaddress
#from PIL import Image
from ctkdlib.custom_widgets import *


""" define the global variables to contain the entry box contents """
serv_int_value: int = 0
port_group_value: int = 0
binding_subnet_value: int = 0
gw_address_value = ""
sig_address_value: str = ""
media_address_value: str = ""
serv_add_value: str = ""
vlan_id_value: int = 0
realm_label_value: str = ""

adj_label_value: str = ""
acct_port_value: int = 0
cust_address_value: str = ""
cust_subnet_value: int = 0

gw_address_valid: bool = False
sig_address_valid: bool = False
media_address_valid: bool = False
cust_address_valid: bool = False


""" get the entry box contents entered by user and assign to the global variables """
def get_entries():
    preview_pane.delete(1.0, customtkinter.END)

    global serv_int_value
    serv_int_value = serv_int_num.get()

    global port_group_value
    port_group_value = port_group.get()

    global binding_subnet_value
    binding_subnet_value = binding_subnet.get()

    global gw_address_value
    gw_address_value = gw_address_entry.get()

    global sig_address_value
    sig_address_value = sig_address_entry.get()

    global media_address_value
    media_address_value = media_address_entry.get()

    global serv_add_value
    serv_add_value = serv_add_entry.get()

    global vlan_id_value
    vlan_id_value = vlan_id.get()

    global realm_label_value
    realm_label_value = realm_entry.get()

    global adj_label_value
    adj_label_value = adj_name_entry.get()

    global acct_port_value
    acct_port_value = acct_port.get()

    global cust_address_value
    cust_address_value = cust_address_entry.get()

    global cust_subnet_value
    cust_subnet_value = cust_subnet.get()

    validate_gw_address()
    validate_sig_address()
    validate_media_address()
    validate_cust_end_address()
    preview_script()

""" define the functions to validate the IP addresses in the related UI fields """
def validate_gw_address():
    if not validate_ip(gw_address_value):
        preview_pane.insert(customtkinter.END, "GW Address not valid ! \n")
        gw_address_label.configure(text_color="red")
    else:
        preview_pane.insert(customtkinter.END, "GW Address OK ! \n")
        gw_address_label.configure(text_color="white")

        global gw_address_valid
        gw_address_valid = True


def validate_sig_address():
    if not validate_ip(sig_address_value):
        preview_pane.insert(customtkinter.END, "Sig Address not valid ! \n")
        sig_address_label.configure(text_color="red")
    else:
        preview_pane.insert(customtkinter.END, "Sig Address OK ! \n")
        sig_address_label.configure(text_color="white")

        global sig_address_valid
        sig_address_valid = True

def validate_media_address():
    if not validate_ip(media_address_value):
        preview_pane.insert(customtkinter.END, "Media Address not valid ! \n")
        media_address_label.configure(text_color="red")
    else:
        preview_pane.insert(customtkinter.END, "Media Address OK ! \n")
        media_address_label.configure(text_color="white")

        global media_address_valid
        media_address_valid = True

def validate_cust_end_address():
    if not validate_ip(cust_address_value):
        preview_pane.insert(customtkinter.END, "Customer Address not valid ! \n")
        cust_address_label.configure(text_color="red")
    else:
        preview_pane.insert(customtkinter.END, "Customer Address OK ! \n")
        cust_address_label.configure(text_color="white")

        global cust_address_valid
        cust_address_valid = True


def validate_ip(address: str) -> bool:
    try:
        ip = ipaddress.ip_address(address)
        print(ip)
        return True
    except ValueError:
        return False

""" functions to create a remaining char count-down in name fields for a 30 char limit"""
CHAR_LIMIT = 30
def update_Serv_add_char_count(event=None):
    remaining = CHAR_LIMIT - len(serv_add_entry.get())
    service_address_label.configure(text=f"Service Address Label - chars left: {remaining}", bg_color=['gray86', 'gray17'])

def update_realm_char_count(event=None):
    remaining = CHAR_LIMIT - len(realm_entry.get())
    realm_label.configure(text=f"Realm Label - chars left: {remaining}", bg_color=['gray86', 'gray17'])

def update_adj_name_char_count(event=None):
    remaining = CHAR_LIMIT - len(adj_name_entry.get())
    adj_name_label.configure(text=f"Adjacency Name - chars left: {remaining}", bg_color=['gray86', 'gray17'])

def preview_script():
    if gw_address_valid and sig_address_valid and media_address_valid and cust_address_valid:
        preview_pane.delete(1.0, customtkinter.END)
        preview_pane.insert(customtkinter.END, "Preview of script - check then enter filename\n\n")
        preview_pane.insert(customtkinter.END, "config\n")
        preview_pane.insert(customtkinter.END, "system\n")
        preview_pane.insert(customtkinter.END, "service-interface serv" + serv_int_value + "\n")
        preview_pane.insert(customtkinter.END, "service-network" + serv_int_value + "\n")
        preview_pane.insert(customtkinter.END, "port-group-name PortGroup" + port_group_value + "\n")
        preview_pane.insert(customtkinter.END, "ipv4" + "\n")
        preview_pane.insert(customtkinter.END, "subnet-prefix-length " + binding_subnet_value + "\n")
        preview_pane.insert(customtkinter.END, "gateway-ip-address " + gw_address_value + "\n")
        preview_pane.insert(customtkinter.END, "local-ip-address " + sig_address_value + "\n")
        preview_pane.insert(customtkinter.END, "service-address " + serv_add_value + "\n")
        preview_pane.insert(customtkinter.END, "end\n\n")

        preview_pane.insert(customtkinter.END, "config\n")
        preview_pane.insert(customtkinter.END, "system\n")
        preview_pane.insert(customtkinter.END, "service-interface serv" + serv_int_value + "\n")
        preview_pane.insert(customtkinter.END, "ipv4\n")
        preview_pane.insert(customtkinter.END, "local-ip-address " + media_address_value + "\n")
        preview_pane.insert(customtkinter.END, "probes-source-style specific-source\n")
        preview_pane.insert(customtkinter.END, "no activate\n")
        preview_pane.insert(customtkinter.END, "vlan-id " + vlan_id_value + "\n")
        preview_pane.insert(customtkinter.END, "network-security trusted\n")
        preview_pane.insert(customtkinter.END, "criticality 1000\n")
        preview_pane.insert(customtkinter.END, "end\n\n")

        preview_pane.insert(customtkinter.END, "config\n")
        preview_pane.insert(customtkinter.END, "sbc\n")
        preview_pane.insert(customtkinter.END, "media\n")
        preview_pane.insert(customtkinter.END, "media-address ipv4 " + media_address_value + " service-network " + serv_int_value + "\n")
        preview_pane.insert(customtkinter.END, "realm " + realm_label_value)
        preview_pane.insert(customtkinter.END, "end\n\n")

        preview_pane.insert(customtkinter.END, "config\n")
        preview_pane.insert(customtkinter.END, "sbc\n")
        preview_pane.insert(customtkinter.END, "signalling\n")
        preview_pane.insert(customtkinter.END, "adjacency sip " + adj_label_value + "\n")
        preview_pane.insert(customtkinter.END, "deactivation-mode normal\n")
        preview_pane.insert(customtkinter.END, "account Port" + acct_port_value + "\n")
        preview_pane.insert(customtkinter.END, "call-media-policy\n")
        preview_pane.insert(customtkinter.END, "media-bypass-policy forbid\n")
        preview_pane.insert(customtkinter.END, "interop\n")
        preview_pane.insert(customtkinter.END, "message-manipulation\n")
        preview_pane.insert(customtkinter.END, "edit-profiles outbound addAllowUPDATE\n")
        preview_pane.insert(customtkinter.END, "force-signaling-peer all-requests\n")
        preview_pane.insert(customtkinter.END, "adjacency-type preset-peering\n")
        preview_pane.insert(customtkinter.END, "privacy trusted\n")
        preview_pane.insert(customtkinter.END, "realm " + realm_label_value + "\n")
        preview_pane.insert(customtkinter.END, "service-address " + serv_add_value + "\n")
        preview_pane.insert(customtkinter.END, "signaling-local-port 5060\n")
        preview_pane.insert(customtkinter.END, "remote-address-range ipv4 " + cust_address_value + " prefix-len " + cust_subnet_value + "\n")
        preview_pane.insert(customtkinter.END, "signaling-peer " + cust_address_value + "\n")
        preview_pane.insert(customtkinter.END, "dynamic-routing-domain-match " + cust_address_value + "\n")
        preview_pane.insert(customtkinter.END, "signaling-peer-port 5060\n")
        preview_pane.insert(customtkinter.END, "statistics-setting detail\n")
        preview_pane.insert(customtkinter.END, "default-interop-profile Peer\n")
        preview_pane.insert(customtkinter.END, "no activate\n")
        preview_pane.insert(customtkinter.END, "end\n\n")


""" set up the UI """
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

Label3 = customtkinter.CTkLabel(master=root, bg_color=['gray86', 'gray17'], text="Service Interface Number", text_color="#3698cd")
Label3.place(x=14, y=40)

serv_int_num = customtkinter.CTkEntry(master=root, bg_color=['gray86', 'gray17'], width=234, placeholder_text="")
serv_int_num.place(x=14, y=64)
CTkTooltip(serv_int_num, text='Example VID112', delay=1.5)

Label4 = customtkinter.CTkLabel(master=root, bg_color=['gray86', 'gray17'], text="Port Group 1-4", text_color="#3698cd")
Label4.place(x=14, y=98)

port_group = customtkinter.CTkEntry(master=root, bg_color=['gray86', 'gray17'], width=234)
port_group.place(x=14, y=121)
CTkTooltip(port_group, text='Number 1 to 4', delay=1.5)

Label5 = customtkinter.CTkLabel(master=root, bg_color=['gray86', 'gray17'], text="Subnet Prefix Length", text_color="#3698cd")
Label5.place(x=14, y=155)

binding_subnet = customtkinter.CTkEntry(master=root, bg_color=['gray86', 'gray17'], width=234)
binding_subnet.place(x=14, y=178)
CTkTooltip(binding_subnet, text='Example 24 for /24', delay=1.5)

gw_address_label = customtkinter.CTkLabel(master=root, bg_color=['gray86', 'gray17'], text="Nasstar GW Address", text_color="#3698cd")
gw_address_label.place(x=14, y=211)

gw_address_entry = customtkinter.CTkEntry(master=root, bg_color=['gray86', 'gray17'], width=234)
gw_address_entry.place(x=14, y=234)

sig_address_label = customtkinter.CTkLabel(master=root, bg_color=['gray86', 'gray17'], text="Nasstar Signalling Address", text_color="#3698cd")
sig_address_label.place(x=14, y=271)

sig_address_entry = customtkinter.CTkEntry(master=root, bg_color=['gray86', 'gray17'], width=234)
sig_address_entry.place(x=14, y=294)

media_address_label = customtkinter.CTkLabel(master=root, bg_color=['gray86', 'gray17'], text="Nasstar Media Address", text_color="#3698cd")
media_address_label.place(x=14, y=330)

media_address_entry = customtkinter.CTkEntry(master=root, bg_color=['gray86', 'gray17'], width=234)
media_address_entry.place(x=14, y=353)

# service address entry with a character countdown from a max 30 chars
######################################################################
service_address_label = customtkinter.CTkLabel(master=root, bg_color=['gray86', 'gray17'], text=f"Service Address Label - chars left: {CHAR_LIMIT}", text_color="#3698cd")
service_address_label.place(x=14, y=389)

serv_add_entry = customtkinter.CTkEntry(master=root, bg_color=['gray86', 'gray17'], width=234)
serv_add_entry.place(x=14, y=411)
serv_add_entry.bind("<KeyRelease>", update_Serv_add_char_count)
CTkTooltip(serv_add_entry, text='Max 30 chars', delay=1.5)

Label10 = customtkinter.CTkLabel(master=root, bg_color=['gray86', 'gray17'], text="VLAN ID", text_color="#3698cd")
Label10.place(x=14, y=448)

vlan_id = customtkinter.CTkEntry(master=root, bg_color=['gray86', 'gray17'], width=234)
vlan_id.place(x=14, y=471)
CTkTooltip(vlan_id, text='Just the number - ie 130', delay=1.5)

# realm label character countdown
######################################################################
realm_label = customtkinter.CTkLabel(master=root, bg_color=['gray86', 'gray17'], text=f"Realm Label - chars left: {CHAR_LIMIT}", text_color="#3698cd")
realm_label.place(x=14, y=510)

realm_entry = customtkinter.CTkEntry(master=root, bg_color=['gray86', 'gray17'], width=234)
realm_entry.place(x=14, y=534)
realm_entry.bind("<KeyRelease>", update_realm_char_count)
CTkTooltip(realm_entry, text='Max 30 chars', delay=1.5)

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

# adjacency name character countdown
######################################################################

adj_name_label = customtkinter.CTkLabel(master=root, bg_color=['gray86', 'gray17'], text=f"Adjacency Name - chars left: {CHAR_LIMIT}", text_color="#3698cd")
adj_name_label.place(x=14, y=596)

adj_name_entry = customtkinter.CTkEntry(master=root, bg_color=['gray86', 'gray17'], width=234)
adj_name_entry.place(x=14, y=620)
adj_name_entry.bind("<KeyRelease>", update_adj_name_char_count)
CTkTooltip(adj_name_entry, text='Max 30 Chars', delay=1.5)

######################################################################

Label14 = customtkinter.CTkLabel(master=root, bg_color=['gray86', 'gray17'], text="Account Port", text_color="#3698cd")
Label14.place(x=14, y=658)

acct_port = customtkinter.CTkEntry(master=root, bg_color=['gray86', 'gray17'], width=234)
acct_port.place(x=14, y=682)
CTkTooltip(acct_port, text='For port 3 & 4 enter in format 34', delay=1.5)

cust_address_label = customtkinter.CTkLabel(master=root, bg_color=['gray86', 'gray17'], text="Customer End Address", text_color="#3698cd")
cust_address_label.place(x=14, y=723)

cust_address_entry = customtkinter.CTkEntry(master=root, bg_color=['gray86', 'gray17'], width=234)
cust_address_entry.place(x=14, y=747)


Label16 = customtkinter.CTkLabel(master=root, bg_color=['gray86', 'gray17'], text="Subnet Prefix Length", text_color="#3698cd")
Label16.place(x=14, y=786)

cust_subnet = customtkinter.CTkEntry(master=root, bg_color=['gray86', 'gray17'], width=234)
cust_subnet.place(x=14, y=810)
CTkTooltip(cust_subnet, text='Example 24 for /24', delay=1.5)

Label17 = customtkinter.CTkLabel(master=root, bg_color=['gray86', 'gray17'], text="Filename:", text_color="#3698cd")
Label17.place(x=367, y=789)

filename_box = customtkinter.CTkEntry(master=root, bg_color=['gray86', 'gray17'], width=257)
filename_box.place(x=427, y=789)
CTkTooltip(filename_box, text='Filename - will be saved as <name>.txt', delay=1.5)

submit = customtkinter.CTkButton(master=root, bg_color=['gray86', 'gray17'], text="Submit", command=get_entries)
submit.place(x=104, y=853)

write_file = customtkinter.CTkButton(master=root, bg_color=['gray86', 'gray17'], text="Write File")
write_file.place(x=455, y=853)

update_Serv_add_char_count()

root.mainloop()
