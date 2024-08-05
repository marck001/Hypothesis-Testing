
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
            f"Step-by-step Calculation:\n"
            f"1. Sample Mean (x̄): {x_bar}\n"
            f"2. Hypothesized Mean (μ0): {mean_0}\n"
            f"3. Sample Standard Deviation (s): {deviation}\n"
            f"4. Sample Size (n): {n}\n"
            f"5. Degrees of Freedom (df): {df}\n"
            f"6. t-value Calculation:\n"
            f"   t = (x̄ - μ0) / (s / sqrt(n))\n"
            f"   t = ({x_bar} - {mean_0}) / ({deviation} / sqrt({n}))\n"
            f"   t = {t_value:.4f}\n"
            f"7. p-value Calculation:\n"
            f"   p = 2 * (1 - stats.t.cdf(abs(t), df))\n"
            f"   p = 2 * (1 - stats.t.cdf({abs(t_value):.4f}, {df}))\n"
            f"   p = {p_value:.4f}\n\n"
            f"Results:\n"
            f"t-value: {t_value:.4f}\n"
            f"p-value: {p_value:.4f}\n"
        )
        
        if p_value < 0.05:  # Significance Level
            result += "Conclusion: Reject the null hypothesis (H0)."
        else:
            result += "Conclusion: Do not reject the null hypothesis (H0)."

        result_text.insert(tk.END, result)
        plot_t_distribution(t_value, df, canvas_frame)

    except ValueError:
        messagebox.showerror("Input error", "Please enter valid numbers.")

def create_gui():
 
    window = tk.Tk()
    window.title("Calculator")

    tk.Label(window, text="Prueba Hipotesis",font=('Helvetica', 24), bg='white',fg='blue').pack()
    
    tk.Label(window, text="Promedio muestral (x̄)",font=('Helvetica', 15)).pack()
    global entry_mean
    entry_mean = tk.Entry(window,width=25)
    entry_mean.pack()

    tk.Label(window, text="Hipótesis nula (μ0)",font=('Helvetica', 15)).pack()
    global entry_h0
    entry_h0 = tk.Entry(window, width=25)
    entry_h0.pack()

    tk.Label(window, text="Desviación estándar  (s)",font=('Helvetica', 15)).pack()
    global entry_std
    entry_std = tk.Entry(window, width=25)
    entry_std.pack()

    tk.Label(window, text="Muestra (n)",font=('Helvetica', 15)).pack()
    global entry_n
    entry_n = tk.Entry(window,width=25)
    entry_n.pack()

  
    global result_text
    result_text = tk.Text(window, height=5, width=50)
    result_text.pack()

   
    global canvas_frame
    canvas_frame = tk.Frame(window)
    canvas_frame.pack()

    calculate_button = tk.Button(window, text="Calculate", command=calculate_button_click, activebackground='light sea green',font=('Times', 20, 'bold') )
    calculate_button.pack()

    return window
