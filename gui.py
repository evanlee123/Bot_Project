import tkinter as tk
from tkinter import ttk
from store_info import *



class Window(tk.Frame):

    def __init__(self, master=None):
        super().__init__()
        self._payments = []
        self._orders = []
        self._background_color = "black"
        self._border_color = "red"

        self.load_saves()


        self.master = master

        self._init_window()

    def _init_window(self):
        self.master.title("Supreme Bot")
        # allowing the widget to take the full space of the root window
        self.pack(fill="both", expand=1)


        frame_style = {"bg":self._background_color, "highlightbackground":self._border_color, "highlightcolor":self._border_color, "highlightthickness":1}

        self.master.resizable(False,False)
        main_frame = tk.Frame(self, **frame_style)
        main_frame.pack(fill="both", expand=1)
        confirmation_frame = tk.Frame(self, relief="raised", borderwidth=1)
        confirmation_frame.pack()

        top_frame = tk.Frame(main_frame, bg=self._background_color, highlightbackground=self._border_color, highlightcolor=self._border_color)
        top_frame.pack(fill="both", expand=1)

        bottom_frame = tk.Frame(main_frame, bg=self._background_color, highlightbackground=self._border_color, highlightcolor=self._border_color)
        bottom_frame.pack(fill="both", expand=1)

        payment_frame = tk.Frame(top_frame, **frame_style)
        payment_frame.pack(side="left", fill="both", expand=1)

        debug_frame = tk.Frame(top_frame, **frame_style)
        debug_frame.pack(side="right", fill="both", expand=1)

        order_frame = tk.Frame(bottom_frame, **frame_style)
        order_frame.pack(fill="both", expand=1)

        self._init_payment_frame(payment_frame)
        self._init_debug_frame(debug_frame)




    def _init_menu(self):
        pass

    def _init_payment_frame(self, payment_frame):


        #fill payment_frame

        #frames
        inner_frame = tk.Frame(payment_frame, bg=self._background_color, highlightbackground=self._border_color, highlightcolor=self._border_color, highlightthickness=0)
        left_frame = tk.Frame(inner_frame, bg=self._background_color, highlightbackground=self._border_color, highlightcolor=self._border_color, highlightthickness=1)
        right_frame = tk.Frame(inner_frame, bg=self._background_color, highlightbackground=self._border_color, highlightcolor=self._border_color, highlightthickness=1)
        button_frame = tk.Frame(inner_frame, bg=self._background_color, highlightbackground=self._border_color, highlightcolor=self._border_color, highlightthickness=1)


        #labels
        payment_label = tk.Label(payment_frame, text="Payment Information", bg=self._background_color, fg=self._border_color,
                                 highlightbackground=self._border_color, highlightcolor=self._border_color, highlightthickness=1)
        tk.Label(left_frame, text="Inactive Payments", bg=self._background_color, fg=self._border_color,
                 highlightbackground=self._border_color, highlightcolor=self._border_color, highlightthickness=1).pack(fill="x")
        tk.Label(right_frame, text="Active Payments", bg=self._background_color, fg=self._border_color,
                 highlightbackground=self._border_color, highlightcolor=self._border_color, highlightthickness=1).pack(fill="x")

        #listboxes
        inactive_payments = tk.Listbox(left_frame, bg=self._background_color, fg=self._border_color, highlightbackground=self._border_color, highlightcolor=self._border_color, highlightthickness=1)
        active_payments = tk.Listbox(right_frame, bg=self._background_color, fg=self._border_color, highlightbackground=self._border_color, highlightcolor=self._border_color, highlightthickness=1)

        #buttons for the payments
        button_active = tk.Button(button_frame, text=">>", fg=self._border_color, bg=self._background_color, highlightbackground=self._border_color, highlightcolor=self._border_color, highlightthickness=0)
        button_inactive = tk.Button(button_frame, text="<<", fg=self._border_color, bg=self._background_color, highlightbackground=self._border_color, highlightcolor=self._border_color, highlightthickness=0)
        button_add = tk.Button(button_frame, text="+", fg=self._border_color, bg=self._background_color, highlightbackground=self._border_color, highlightcolor=self._border_color, highlightthickness=0)
        button_delete = tk.Button(button_frame, text="x",  fg=self._border_color, bg=self._background_color, highlightbackground=self._border_color, highlightcolor=self._border_color, highlightthickness=0)

        payment_label.pack(fill="x")
        inner_frame.pack(fill="both", expand=1)
        left_frame.pack(side="left",fill="both", expand=1)
        right_frame.pack(side="right",fill="both", expand=1)
        button_frame.pack(side="bottom", fill="both", expand=1)

        button_active.pack(pady=5, padx=10, fill="x")
        button_inactive.pack(pady=5, padx=10, fill="x")
        button_add.pack(pady=5, padx=10, fill="x")
        button_delete.pack(pady=5, padx=10, fill="x")
        inactive_payments.pack(fill="both", expand=1)
        active_payments.pack(fill="both",  expand=1)




        for payment in self._payments:
            if payment.is_active():
                active_payments.insert("end", payment)
            else:
                inactive_payments.insert("end", payment)

    def _init_debug_frame(self, debug_frame):


        debug_label = tk.Label(debug_frame, text="Debug Pane", bg=self._background_color, fg=self._border_color, highlightbackground=self._border_color, highlightcolor=self._border_color, highlightthickness=1)
        debug_label.pack(fill="x")

        inner_frame = tk.Frame(debug_frame, bg=self._background_color, highlightbackground=self._border_color, highlightcolor=self._border_color, highlightthickness=1)
        inner_frame.pack(fill="both", expand=1)


        pass





    def load_saves(self):
        pass


    def client_exit(self):
        exit()


class Payment_GUI(tk.Frame):
    def __init__(self, master=None, payment=[]):
        super().__init__()
        self._background_color = "black"
        self._border_color = "red"
        self.payments = payment
        self._init_window()


    def _init_window(self):
        self.master.title("Add Payment Information")
        #self.master.geometry("900x300")
        self.master.resizable(False,False)

        self._init_fields()

    def _init_fields(self):
        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.columnconfigure(3, pad=3)

        self.style = ttk.Style()
        self.style.theme_use("default")

        self.pack(fill="both", expand=True)
        # self.columnconfigure(1, weight=1)
        # self.columnconfigure(3, pad=7)
        # self.rowconfigure(3, weight=1)
        # self.rowconfigure(5, pad=7)

        #The Frames
        information_frame = tk.Frame(self,relief="raised", borderwidth=1)
        information_frame.pack(fill="both", expand=True)

        bill_address_frame = tk.Frame(information_frame, relief="sunken", borderwidth=1)
        bill_address_frame.pack(side="left", fill="both", expand=True)

        card_frame = tk.Frame(information_frame, relief="sunken", borderwidth=1)
        card_frame.pack(side="right", fill="both", expand=True)

        self._init_payments(bill_address_frame)
        self._init_card(card_frame)

        #Card Info

        #for the save, clear, and close buttons
        confirmation_frame = tk.Frame(self)
        confirmation_frame.pack(fill="both")
        closeButton = tk.Button(confirmation_frame, text="Close", command=self.master.destroy, width = 20)
        closeButton.pack(side="right", padx=5, pady=5)
        clearButton = tk.Button(confirmation_frame, text="Clear", command = self.clear_inputs, width = 20)
        clearButton.pack(side="right", padx=5, pady=5)
        saveButton = tk.Button(confirmation_frame, text="Save", command=self.save_payment, width = 20)
        saveButton.pack(side="right", padx=5, pady=5)


    def _init_payments(self,bill_address_frame):
        #Billing info

        bill_label = tk.Label(bill_address_frame, text="Billing Information", bg=self._border_color)
        bill_label.grid(row=0, sticky="NESW", columnspan=6)

        #name
        tk.Label(bill_address_frame, text="Full Name").grid(row=1, column=0)
        self.name_entry = tk.Entry(bill_address_frame)
        self.name_entry.grid(row=1, column=1, pady=5, columnspan=5, sticky="WE")

        #email
        tk.Label(bill_address_frame, text="Email").grid(row=2, column=0)
        self.email_entry = tk.Entry(bill_address_frame)
        self.email_entry.grid(row=2, column=1, pady=5, columnspan=5, sticky="WE")

        #telephone
        tk.Label(bill_address_frame, text="telephone").grid(row=3, column=0)
        self.phone_entry = tk.Entry(bill_address_frame)
        self.phone_entry.grid(row=3, column=1, pady=5, columnspan=5, sticky="WE")

        #Address
        tk.Label(bill_address_frame, text="Address").grid(row=4, column=0)
        self.address_entry = tk.Entry(bill_address_frame)
        self.address_entry.grid(row=4, column=1, pady=5, columnspan=5, sticky="WE")

        #Apt, zipcode and city
        tk.Label(bill_address_frame, text="Apt").grid(row=5, column=0, sticky="WE")
        self.apt_entry = tk.Entry(bill_address_frame)
        self.apt_entry.grid(row=5, column=1, pady=5)

        tk.Label(bill_address_frame, text="Zip Code").grid(row=5, column=2)
        self.zip_entry = tk.Entry(bill_address_frame)
        self.zip_entry.grid(row=5, column=3, pady=5)

        tk.Label(bill_address_frame, text="City").grid(row=5, column=4)
        self.city_entry = tk.Entry(bill_address_frame)
        self.city_entry.grid(row=5, column=5, pady=5)

        #State
        tk.Label(bill_address_frame, text="State").grid(row=6, sticky= "WE")
        states = ["AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID",
                  "IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS",
                  "MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR",
                  "PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]
        self.current_state = tk.StringVar(bill_address_frame)
        self.current_state.set(states[0])
        state_menu = tk.OptionMenu(bill_address_frame, self.current_state, *states)
        state_menu.grid(row=6, column =1, sticky="WE")

        #Country
        tk.Label(bill_address_frame, text="Country").grid(row=6, column=2, sticky= "WE")
        self.current_country = tk.StringVar(bill_address_frame)
        self.current_country.set("USA")
        country_menu = tk.OptionMenu(bill_address_frame, self.current_country, "USA")
        country_menu.grid(row=6, column =3, sticky="WE")

    def _init_card(self, card_frame):
        tk.Label(card_frame, text="Credit Card Information", bg=self._border_color).grid(row=0, sticky="NESW", columnspan=7)

        #Card Number
        tk.Label(card_frame, text="Credit Card Number").grid(row=1, column=0)
        self.card_number_entry = tk.Entry(card_frame)
        self.card_number_entry.grid(row=1, column=1, pady=5, columnspan=6, sticky="WE")

        #Exp Month, Exp Year, CCV
        tk.Label(card_frame, text="Exp Month").grid(row=2, sticky= "WE")
        months = ["01", "02", "03","04","05","06","07","08","09","10","11","12"]
        self.current_month = tk.StringVar(card_frame)
        self.current_month.set(months[0])
        month_menu = tk.OptionMenu(card_frame, self.current_month, *months)
        month_menu.grid(row=2, column =1, sticky="WE")

        tk.Label(card_frame, text="Exp Year").grid(row=2, column=2, sticky= "WE")
        years = [x for x in range(2018,2018+15)]
        self.curr_year = tk.StringVar(card_frame)
        self.curr_year.set(years[0])
        year_menu = tk.OptionMenu(card_frame, self.curr_year, *years)
        year_menu.grid(row=2, column =3, sticky="WE")

        tk.Label(card_frame, text="CCV").grid(row=2, column=4)
        self.ccv_entry = tk.Entry(card_frame)
        self.ccv_entry.grid(row=2, column=5, pady=5,  sticky="WE")


    def clear_inputs(self):
        name = self.name_entry
        email = self.email_entry
        phone = self.phone_entry
        address = self.address_entry
        address2 = self.apt_entry
        zipcode = self.zip_entry
        city = self.city_entry
        state = self.current_state
        country = self.current_country
        card_number = self.card_number_entry
        exp_month = self.current_month
        exp_year = self.curr_year
        ccv = self.ccv_entry

        parameters = {"name": name, "email": email, "phone": phone,"address": address,
                      "address 2": address2,"zipcode": zipcode, "city": city,
                      "state": state, "country": country, "card number": card_number,
                      "exp_month": exp_month, "exp_year": exp_year, "ccv": ccv}
        for param in parameters:
            if param not in ["country", "state", "exp_month", "exp_year"]:
                parameters[param].delete(0, last=len(parameters[param].get()))
    def save_payment(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        address = self.address_entry.get()
        address2 = self.apt_entry.get()
        zipcode = self.zip_entry.get()
        city = self.city_entry.get()
        state = self.current_state.get()
        country = self.current_country.get()
        card_number = self.card_number_entry.get()
        exp_month = self.current_month.get()
        exp_year = self.curr_year.get()
        ccv = self.ccv_entry.get()

        parameters = {"name": name, "email": email, "phone": phone,"address": address,
                      "address 2": address2,"zipcode": zipcode, "city": city,
                      "state": state, "country": country, "card number": card_number,
                      "exp_month": exp_month, "exp_year": exp_year, "ccv": ccv}

        for param in parameters:
            if parameters[param] is None or parameters[param] is "":
                self.popup_msg("{} is not filled!".format(param))
                return

        self.payments.append(Payment_info(*parameters))
        print(self.payments)

        print(parameters)

        #Create Grid

    def popup_msg(self, msg):
        popup = tk.Tk()
        popup.wm_title("!")
        label = tk.Label(popup, text=msg, font=("Helvettica", 10))
        label.pack(side="top",fill="x", pady=10)
        B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
        B1.pack()
        popup.mainloop()

        pass

class Order_GUI(tk.Frame):
    def __init__(self,master=None, orders=[]):
        super().__init__()

        self.orders = orders
        self._init_window()

    def _init_window(self):
        self.master.title("Add Order Information")
        self.master.resizable(False,False)
        self.pack(fill="both", expand=True)

        information_frame = tk.Frame(self, relief="sunken", borderwidth=1)
        information_frame.pack(fill="both", expand="True")

        left_frame = tk.Frame(information_frame, relief="sunken", borderwidth=1)
        left_frame.pack(side="left", fill="both",expand=True)

        right_frame = tk.Frame(information_frame, relief="sunken", borderwidth=1)
        right_frame.pack(side="right", fill="both", expand=True)

        confirmation_frame = tk.Frame(self, relief="ridge", borderwidth=1)
        confirmation_frame.pack(side="bottom", fill="x")

        self._init_sizes(left_frame)
        self._init_types(left_frame)

        self._init_right(right_frame)
        self._init_confirm(confirmation_frame)

    def _init_sizes(self,left_frame):
        sizes = [("S", "Small"),
                 ("M", "Medium"),
                 ("L", "Large"),
                 ("XL", "Xlarge"),
                 ("Any Size", "")]
        tk.Label(left_frame, text="Choose Size", bg="light blue").pack(fill="both", expand=True)
        self.size_out = tk.StringVar()
        self.size_out.set(None)
        for size, val in sizes:
            tk.Radiobutton(left_frame, text=size,
                           indicatoron = 0, variable=self.size_out, selectcolor="pink",
                           command=lambda: self._show_size(),
                           value=val).pack(fill="x", anchor="w", expand=True)

    def _init_types(self, left_frame):
        types = ["jackets", "shirts", "tops", "sweatshirts", "t-shirts",
                 "pants", "hats", "bags", "accessories", "shoes", "skates"]
        tk.Label(left_frame, text="Choose Type", bg="light blue").pack(fill="both", expand=True)

        type_frame = tk.Frame(left_frame)
        type_frame.pack(fill="both", expand="true")

        self.type_out = tk.StringVar()
        self.type_out.set(None)

        for type in types:
            c = types.index(type)%2
            r = types.index(type)//2
            tk.Radiobutton(type_frame, text=type, selectcolor="pink",
                           indicator=0, variable=self.type_out,
                           value=type).grid(row=r, column=c , sticky="WE")

    def _init_right(self, right_frame):
        #keyword
        tk.Label(right_frame, text="Keyword").grid(row=0, column=0)
        self.keyword_entry = tk.Entry(right_frame)
        self.keyword_entry.grid(row=0, column=1, pady=5,sticky="WE")

        #color
        tk.Label(right_frame, text="Color").grid(row=1, column=0)
        self.color_entry = tk.Entry(right_frame)
        self.color_entry.grid(row=1, column=1, pady=5,sticky="WE")

        #quantity
        tk.Label(right_frame, text="Quantity").grid(row=2, sticky= "WE")
        qtys = ["01", "02", "03","04","05","06","07","08","09","10",
                  "11", "12", "13", "14","15","16","17","18","19","20"]
        self.current_qty = tk.StringVar(right_frame)
        self.current_qty.set("")
        qty_menu = tk.OptionMenu(right_frame, self.current_qty, *qtys)
        qty_menu.grid(row=2, column =1, sticky="WE")

    def _init_confirm(self, confirmation_frame):
        closeButton = tk.Button(confirmation_frame, text="Close", command=self.master.destroy )
        closeButton.pack(side="right", padx=5, pady=5)
        clearButton = tk.Button(confirmation_frame, text="Clear", command = self._clear_inputs )
        clearButton.pack(side="right", padx=5, pady=5)
        saveButton = tk.Button(confirmation_frame, text="Save", command=self._save_order)
        saveButton.pack(side="right", padx=5, pady=5)

    def _save_order(self):
        #check if valid
        name = self.keyword_entry.get()
        type = self.type_out.get()
        color = self.color_entry.get()
        size = self.size_out.get()
        qty = self.current_qty.get()

        args = [name,type,color,size,qty]

        for elem in (size, type):
            if elem is None:
                self.popup_msg("Not fully filled!")
                return
        for elem in (name, color, qty):
            if elem is "":
                self.popup_msg("Not fully filled!")
                return

        self.orders.append(Order_info(*args))
        for order in self.orders:
            print(order.make_list)

        pass
    def _clear_inputs(self):
        self.keyword_entry.delete(0, 'end')
        self.type_out.set(None)
        self.color_entry.delete(0,'end')
        self.size_out.set(None)
        self.current_qty.set("")
        pass


    def _show_size(self):
        print(self.size_out.get())

    def popup_msg(self, msg):
        popup = tk.Tk()
        popup.wm_title("!")
        label = tk.Label(popup, text=msg, font=("Helvettica", 10))
        label.pack(side="top",fill="x", pady=10)
        B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
        B1.pack()
        popup.mainloop()



root = tk.Tk()

app = Window(root)


#app = Payment_GUI(root)

root.mainloop()