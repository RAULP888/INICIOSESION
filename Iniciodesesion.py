import tkinter as tk
from tkinter import messagebox
import os

# === FUNCIONES DE ARCHIVO ===

# Cargar usuarios desde archivo
def cargar_usuarios():
    if not os.path.exists("usuarios.txt"):
        return {}
    with open("usuarios.txt", "r") as f:
        return dict(line.strip().split(":") for line in f if ":" in line)

# Guardar nuevo usuario en el archivo
def guardar_usuario(usuario, contrasena):
    with open("usuarios.txt", "a") as f:
        f.write(f"{usuario}:{contrasena}\n")

# === LÓGICA DEL SISTEMA ===

usuarios = cargar_usuarios()

def validar_login():
    usuario = entry_usuario.get().strip()
    contrasena = entry_contrasena.get().strip()
    if usuario in usuarios and usuarios[usuario] == contrasena:
        messagebox.showinfo("Inicio de sesión", "Inicio de sesión exitoso.")
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

def agregar_usuario():
    nuevo_usuario = entry_nuevo_usuario.get().strip()
    nueva_contrasena = entry_nueva_contrasena.get().strip()
    
    if not nuevo_usuario or not nueva_contrasena:
        messagebox.showwarning("Campos vacíos", "⚠️ Llena ambos campos.")
        return
    
    if nuevo_usuario in usuarios:
        messagebox.showerror("Usuario existente", "⚠️ El nombre de usuario ya existe.")
    else:
        usuarios[nuevo_usuario] = nueva_contrasena
        guardar_usuario(nuevo_usuario, nueva_contrasena)
        messagebox.showinfo("Usuario agregado", f"✅ Usuario '{nuevo_usuario}' agregado correctamente.")
        entry_nuevo_usuario.delete(0, tk.END)
        entry_nueva_contrasena.delete(0, tk.END)

# === INTERFAZ GRÁFICA ===

ventana = tk.Tk()
ventana.title("Inicio de Sesión")
ventana.geometry("450x480")
ventana.configure(bg="#f0f4f8")

# Título
tk.Label(ventana, text="INICIO DE SESIÓN", font=("Helvetica", 16, "bold"), bg="#f0f4f8", fg="#333").pack(pady=15)

# Formulario de login
frame_login = tk.Frame(ventana, bg="#f0f4f8")
frame_login.pack(pady=10)

tk.Label(frame_login, text="Usuario:", font=("Helvetica", 12), bg="#f0f4f8").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_usuario = tk.Entry(frame_login, width=25, font=("Helvetica", 12))
entry_usuario.grid(row=0, column=1, pady=5)

tk.Label(frame_login, text="Contraseña:", font=("Helvetica", 12), bg="#f0f4f8").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_contrasena = tk.Entry(frame_login, width=25, show="*", font=("Helvetica", 12))
entry_contrasena.grid(row=1, column=1, pady=5)

btn_login = tk.Button(ventana, text="Iniciar sesión", font=("Helvetica", 12), bg="#007acc", fg="white", width=20, command=validar_login)
btn_login.pack(pady=10)

# Separador
tk.Label(ventana, text="------------------------", bg="#f0f4f8", fg="#999").pack(pady=5)

# Sección para agregar usuarios
tk.Label(ventana, text="REGISTRAR NUEVO USUARIO", font=("Helvetica", 14, "bold"), bg="#f0f4f8", fg="#333").pack(pady=10)

frame_nuevo = tk.Frame(ventana, bg="#f0f4f8")
frame_nuevo.pack(pady=10)

tk.Label(frame_nuevo, text="Nuevo usuario:", font=("Helvetica", 12), bg="#f0f4f8").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_nuevo_usuario = tk.Entry(frame_nuevo, width=25, font=("Helvetica", 12))
entry_nuevo_usuario.grid(row=0, column=1, pady=5)

tk.Label(frame_nuevo, text="Nueva contraseña:", font=("Helvetica", 12), bg="#f0f4f8").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_nueva_contrasena = tk.Entry(frame_nuevo, width=25, font=("Helvetica", 12), show="*")
entry_nueva_contrasena.grid(row=1, column=1, pady=5)

btn_agregar = tk.Button(ventana, text="Agregar usuario", font=("Helvetica", 12), bg="#28a745", fg="white", width=20, command=agregar_usuario)
btn_agregar.pack(pady=10)

# Ejecutar interfaz
ventana.mainloop()
