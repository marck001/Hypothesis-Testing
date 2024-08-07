
import tkinter as tk
from tkinter import messagebox
from t_distribution.calculate_values import calculate_t_value, calculate_p_value
from t_distribution.plot_distribution import plot_t_distribution

def calculate_button_click():
    try:
        # Clear previous results and plots
        result_text.delete(1.0, tk.END)
        for widget in canvas_frame.winfo_children():
            widget.destroy()

        # Test Parameters
        x_bar = float(entry_mean.get())  
        mean_0 = float(entry_h0.get())  
        deviation = float(entry_std.get())  
        n = int(entry_n.get()) 

        # Calculations
        t_value = calculate_t_value(x_bar, mean_0, deviation, n)
        p_value, df = calculate_p_value(n, t_value)

       
        result = (
            f"Calculo paso a paso:\n"
            f"1. Promedio muestral (x̄): {x_bar}\n"
            f"2. Hipotesis nula (μ0): {mean_0}\n"
            f"3. Desviación muestral standar (s): {deviation}\n"
            f"4. Muestra (n): {n}\n"
            f"5. Grados de Libertad (df): {df}\n"
            f"6. t-value :\n"
            f"   t = (x̄ - μ0) / (s / sqrt(n))\n"
            f"   t = ({x_bar} - {mean_0}) / ({deviation} / sqrt({n}))\n"
            f"   t = {t_value:.4f}\n"
            f"7. p-value :\n"
            f"   p = 2 * (1 - stats.t.cdf(abs(t), df))\n"
            f"   p = 2 * (1 - stats.t.cdf({abs(t_value):.4f}, {df}))\n"
            f"   p = {p_value:.4f}\n\n"
            f"Results:\n"
            f"t-value: {t_value:.4f}\n"
            f"p-value: {p_value:.4f}\n"
        )
        
        if p_value < 0.05:  
            result += "Conclusion: Se rechaza la hipotesis nula (H0)."
        else:
            result += "Conclusion: No se rechaza hipotesis nula (H0)."

        result_text.insert(tk.END, result)
        plot_t_distribution(t_value, df, canvas_frame)

    except ValueError:
        messagebox.showerror("Input error", "Please enter valid numbers.")

def create_gui():
 
    window = tk.Tk()
    window.title("Calculator")
    
    frame = tk.Frame(window, padx=30, pady=40, bg="#fafafa")
    frame.pack(expand=True,  fill=tk.NONE, anchor='center')
    
    tk.Label(window, text="Prueba Hipotesis",font=('Helvetica', 24), bg='white',fg='blue').pack()
    
    tk.Label(frame, text="H₀:", font=('Helvetica', 12)).grid(row=0, column=0, sticky='w')
    tk.Label(frame, text="μ", font=('Helvetica', 12)).grid(row=0, column=1)
    #tk.Entry(frame, width=5).grid(row=0, column=2)
    
    tk.Label(frame, text="=", font=('Helvetica', 12)).grid(row=0, column=2)

    global entry_h0
    entry_h0 =  tk.Entry(frame, width=5)
    entry_h0.grid(row=0, column=4)


    tk.Label(frame, text="Hₐ:", font=('Helvetica', 12)).grid(row=1, column=0, sticky='w')
    tk.Label(frame, text="μ", font=('Helvetica', 12)).grid(row=1, column=1)
    #tk.Entry(frame, width=5).grid(row=1, column=2)
    tk.Label(frame, text="≠", font=('Helvetica', 12)).grid(row=1, column=2)
    tk.Entry(frame, width=5).grid(row=1, column=4)

   
    tk.Label(frame, text="n =", font=('Helvetica', 12)).grid(row=2, column=0, sticky='e')
    global entry_n
    entry_n = tk.Entry(frame, width=10)
    entry_n.grid(row=2, column=1, sticky='w')

    
    tk.Label(frame, text="x̄ =", font=('Helvetica', 12)).grid(row=3, column=0, sticky='e')
    global entry_mean
    entry_mean = tk.Entry(frame, width=10)
    entry_mean.grid(row=3, column=1, sticky='w')

    #
    tk.Label(frame, text="s =", font=('Helvetica', 12)).grid(row=4, column=0, sticky='e')
    global entry_std
    entry_std = tk.Entry(frame, width=10)
    entry_std.grid(row=4, column=1, sticky='w')

   
    tk.Label(frame, text="Level of Significance: α =", font=('Helvetica', 12)).grid(row=5, column=0, columnspan=2, sticky='w')
    tk.Label(frame, text="0.05", font=('Helvetica', 12)).grid(row=5, column=2, sticky='w')

    # Solve button
    calculate_button = tk.Button(frame, text="Solve", command=calculate_button_click, activebackground='light sea green', font=('Times', 15, 'bold'))
    calculate_button.grid(row=6, column=0, columnspan=3, pady=10)
    
    global result_text
    result_text = tk.Text(window, height=5, width=50)
    result_text.pack()
    
   
    
    global canvas_frame
    canvas_frame = tk.Frame(window)
    canvas_frame.pack()
    
    
  





  

    return window
