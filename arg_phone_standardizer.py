import pandas as pd
import re
import tkinter as tk
from tkinter import filedialog, messagebox
import tkinter.font as tkfont
import os

# Función que estandariza los números de teléfono
def normalize_phone(phone, area_codes_set):
    # Convertir a string si no lo es
    phone = str(phone)
    
    # Eliminar caracteres no numéricos
    phone = re.sub(r'\D', '', phone)
    
    # Eliminar ceros a la izquierda
    phone = phone.lstrip('0')
    
    # Agregar 54 al principio si empieza con 9
    if phone.startswith('9'):
        phone = '54' + phone
    
    # Agregar 549 al principio si empieza con un código de área
    if any(phone.startswith(str(code)) for code in area_codes_set):
        phone = '549' + phone
    
    # Eliminar el 15 después del código de área
    for code in area_codes_set:
        if phone.startswith('549' + str(code) + '15'):
            phone = phone[:len('549' + str(code))] + phone[len('549' + str(code) + '15'):]
            break
    
    # Verificar longitud final
    if len(phone) != 13:
        return None
    
    return phone

class PhoneNormalizer:
    def __init__(self, master):
        self.master = master
        master.title("Normalizador - Apex ARG")
        master.geometry("550x500")
        master.configure(bg='#ffffff')

        # Cambiar el icono de la ventana
        icon_path = os.path.join(os.path.dirname(__file__), "icon.ico")
        if os.path.exists(icon_path):
            master.iconbitmap(icon_path)
        
        # Definir estilos de fuente
        title_font = tkfont.Font(family="Calibri", size=12, weight="bold")
        step_font = tkfont.Font(family="Calibri", size=12, weight="bold")
        button_font = tkfont.Font(family="Calibri", size=9, weight="bold")
        label_font = tkfont.Font(family="Calibri", size=9, slant="italic")
        instruction_font = tkfont.Font(family="Calibri", size=10)

        # Título principal
        title_label = tk.Label(master, text="Estandarizar números de teléfono", font=title_font, bg='#ffffff', fg='#333333')
        title_label.pack(pady=(10,5), anchor='w', padx=20)

        # Instrucciones generales
        general_instructions = tk.Label(master, text="Utilice este programa para convertir bases de números telefónicos con distintos formatos en una lista normalizada al formato 549(CA)(-15).", 
                                        font=instruction_font, bg='#ffffff', fg='#555555', wraplength=510, justify="left")
        general_instructions.pack(pady=(0,10), anchor='w', padx=20)

        # Frame para el Paso 1
        step1_frame = tk.Frame(master, bg='#e8e1f5', bd=2, relief=tk.GROOVE)
        step1_frame.pack(fill=tk.X, padx=20, pady=10, anchor='w')

        step1_title = tk.Label(step1_frame, text="Paso 1: Cargue su base de datos", font=step_font, bg='#e8e1f5', fg='#333333')
        step1_title.pack(pady=(5,0), anchor='w', padx=10)

        step1_instructions = tk.Label(step1_frame, text="Seleccione el archivo .CSV que contiene los números de teléfono a normalizar. Recuerde que el archivo debe tener una columna llamada 'phone' con los números de teléfono.", 
                                      font=instruction_font, bg='#e8e1f5', fg='#555555', wraplength=490, justify="left")
        step1_instructions.pack(pady=(0,5), anchor='w', padx=10)

        self.step1_button = tk.Button(step1_frame, text="SELECCIONAR", command=self.select_input_file, bg='#a893cf', fg='white', font=button_font)
        self.step1_button.pack(pady=5, anchor='w', padx=10)

        self.input_file_label = tk.Label(step1_frame, text="Archivo no seleccionado", wraplength=450, font=label_font, bg='#e8e1f5', fg='purple')
        self.input_file_label.pack(pady=5, anchor='w', padx=10)

        # Frame para el Paso 2
        step2_frame = tk.Frame(master, bg='#e1e9f5', bd=2, relief=tk.GROOVE)
        step2_frame.pack(fill=tk.X, padx=20, pady=10, anchor='w')

        step2_title = tk.Label(step2_frame, text="Paso 2: Ubicar resultados", font=step_font, bg='#e1e9f5', fg='#333333')
        step2_title.pack(pady=(5,0), anchor='w', padx=10)

        step2_instructions = tk.Label(step2_frame, text="Elija la carpeta donde desea guardar los resultados. Recuerde que se generarán dos archivos: uno con los números normalizados y otro con los descartados.", 
                                      font=instruction_font, bg='#e1e9f5', fg='#555555', wraplength=490, justify="left")
        step2_instructions.pack(pady=(0,5), anchor='w', padx=10)

        self.step2_button = tk.Button(step2_frame, text="UBICAR", command=self.select_output_dir, state=tk.DISABLED, bg='#7d97bd', fg='white', font=button_font)
        self.step2_button.pack(pady=5, anchor='w', padx=10)

        self.output_dir_label = tk.Label(step2_frame, text="Directorio no seleccionado", wraplength=450, font=label_font, bg='#e1e9f5', fg='blue')
        self.output_dir_label.pack(pady=5, anchor='w', padx=10)

        # Botón de procesamiento
        self.process_button = tk.Button(master, text="PROCESAR", command=self.process_file, state=tk.DISABLED, bg='#ebe6e6', fg='#333333', font=button_font)
        self.process_button.pack(pady=20, anchor='center')

        self.input_file = None
        self.output_dir = None

    def select_input_file(self):
        input_file = filedialog.askopenfilename(title="Seleccionar archivo CSV con columna 'phone'", filetypes=[("CSV files", "*.csv")])
        if input_file:
            confirm = messagebox.askokcancel("Confirmar selección", f"¿Desea usar este archivo?\n\n{input_file}")
            if confirm:
                self.input_file = input_file
                self.input_file_label.config(text=f"Archivo seleccionado: {os.path.basename(self.input_file)}")
                self.step2_button.config(state=tk.NORMAL)
            else:
                self.input_file = None
                self.input_file_label.config(text="Archivo no seleccionado")

    def select_output_dir(self):
        output_dir = filedialog.askdirectory(title="Seleccionar ubicación para guardar resultados")
        if output_dir:
            confirm = messagebox.askokcancel("Confirmar selección", f"¿Usar esta ubicación para los resultados?\n\n{output_dir}")
            if confirm:
                self.output_dir = output_dir
                self.output_dir_label.config(text=f"Directorio seleccionado: {self.output_dir}")
                self.process_button.config(state=tk.NORMAL)
            else:
                self.output_dir = None
                self.output_dir_label.config(text="Directorio no seleccionado")

    def process_file(self):
        try:
            # Cargar códigos de área
            script_dir = os.path.dirname(os.path.abspath(__file__))
            area_codes_file = os.path.join(script_dir, 'area_codes_dataset', 'area_codes.csv')
            
            if not os.path.exists(area_codes_file):
                messagebox.showerror("Error", "No se encontró el archivo de códigos de área.")
                return

            area_codes = pd.read_csv(area_codes_file)['code'].astype(str).tolist()
            area_codes_set = set(area_codes)

            # Leer el archivo de entrada
            df = pd.read_csv(self.input_file)
            df['phone'] = df['phone'].astype(str)

            # Aplicar la normalización
            df['normalized_phone'] = df['phone'].apply(lambda x: normalize_phone(x, area_codes_set))

            # Separar números válidos y descartados
            valid_phones = df[df['normalized_phone'].notnull()]
            discarded_phones = df[df['normalized_phone'].isnull()]

            # Generar nombres de archivo basados en el archivo de entrada
            input_filename = os.path.splitext(os.path.basename(self.input_file))[0]
            valid_file = os.path.join(self.output_dir, f"{input_filename}_valid.csv")
            discarded_file = os.path.join(self.output_dir, f"{input_filename}_invalid.csv")

            # Guardar resultados
            valid_phones.to_csv(valid_file, index=False)
            discarded_phones.to_csv(discarded_file, index=False)
            
            messagebox.showinfo("Normalización completada", 
                                f"Resultados\n"
                                f"Números válidos: {len(valid_phones)}\n"
                                f"Números descartados: {len(discarded_phones)}\n\n"
                                f"Archivos generados\n"
                                f"{os.path.basename(valid_file)}\n"
                                f"{os.path.basename(discarded_file)}\n\n"
                                f"En el directorio:\n{self.output_dir}")

        except Exception as e:
            messagebox.showerror("Error", f"Se produjo un error: {str(e)}")

root = tk.Tk()
app = PhoneNormalizer(root)
root.mainloop()