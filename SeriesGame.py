import tkinter as tk
from tkinter import ttk, messagebox
import random
import math
import matplotlib.pyplot as plt
import io
from PIL import Image, ImageTk
import matplotlib

matplotlib.use('TkAgg')


class LaTeXRenderer:
    """Handles rendering of LaTeX expressions to images"""

    def __init__(self):
        plt.rcParams['mathtext.fontset'] = 'stix'
        plt.rcParams['font.family'] = 'serif'
        plt.rcParams['font.size'] = 18

    def render(self, latex_expr, bg_color='#ecf0f1', size=(700, 150)):
        """Render LaTeX expression to PhotoImage"""
        try:
            fig, ax = plt.subplots(figsize=(size[0] / 100, size[1] / 100), dpi=100)
            fig.patch.set_facecolor(bg_color)
            ax.set_facecolor(bg_color)

            ax.text(0.5, 0.5, f'${latex_expr}$',
                    fontsize=20, ha='center', va='center',
                    transform=ax.transAxes)
            ax.axis('off')

            buf = io.BytesIO()
            plt.savefig(buf, format='png', bbox_inches='tight',
                        facecolor=bg_color, dpi=100)
            buf.seek(0)
            img = Image.open(buf)
            photo = ImageTk.PhotoImage(img)
            plt.close(fig)

            return photo
        except Exception as e:
            print(f"LaTeX rendering error: {e}")
            return None

    def render_small(self, latex_expr, bg_color='#3498db', size=(300, 60)):
        """Render smaller LaTeX for buttons"""
        try:
            fig, ax = plt.subplots(figsize=(size[0] / 100, size[1] / 100), dpi=100)
            fig.patch.set_facecolor(bg_color)
            ax.set_facecolor(bg_color)

            ax.text(0.5, 0.5, f'${latex_expr}$',
                    fontsize=14, ha='center', va='center',
                    transform=ax.transAxes)
            ax.axis('off')

            buf = io.BytesIO()
            plt.savefig(buf, format='png', bbox_inches='tight',
                        facecolor=bg_color, dpi=100)
            buf.seek(0)
            img = Image.open(buf)
            photo = ImageTk.PhotoImage(img)
            plt.close(fig)

            return photo
        except Exception as e:
            print(f"LaTeX rendering error: {e}")
            return None

    def graph_sequence_from_latex(self, latex_expr, n_terms=15):
        """Parse LaTeX and create a graph for sequences, series, or functions"""
        try:
            # Use LaTeX for all text elements
            plt.rcParams['text.usetex'] = False  # Keep False to avoid requiring LaTeX installation
            plt.rcParams['mathtext.fontset'] = 'stix'

            fig, ax = plt.subplots(figsize=(7, 4), dpi=100)

            n_values = list(range(1, n_terms + 1))
            y_values = []

            # Check what type of expression we have
            if "sum" in latex_expr or "sum_{" in latex_expr:
                # It's a series - calculate partial sums
                for n in n_values:
                    try:
                        if "1/n^2" in latex_expr:
                            val = sum(1 / (i ** 2) for i in range(1, n + 1))
                        elif "1/n" in latex_expr:
                            val = sum(1 / i for i in range(1, n + 1))
                        elif "1/2" in latex_expr and "n" in latex_expr:
                            val = sum((1 / 2) ** i for i in range(0, n))
                        elif "2^n" in latex_expr:
                            val = sum(2 ** i for i in range(0, n))
                        else:
                            val = sum(1 / (i ** 2) for i in range(1, n + 1))
                        y_values.append(val)
                    except:
                        y_values.append(0)
                ax.set_ylabel(r'$S_n = \sum_{k=1}^{n} a_k$', fontsize=12)
                title = rf'Series Partial Sums: ${latex_expr}$'
            else:
                # It's a sequence - calculate terms
                expr = latex_expr.replace("a_n = ", "").replace("a_n=", "")

                for n in n_values:
                    try:
                        if "1/n" in expr:
                            val = 1 / n
                        elif "n/(n+1)" in expr:
                            val = n / (n + 1)
                        elif "2n/(3n+1)" in expr:
                            val = (2 * n) / (3 * n + 1)
                        elif "1/2^n" in expr or "1/2^{n}" in expr:
                            val = 1 / (2 ** n)
                        elif "2 + 1/n" in expr:
                            val = 2 + 1 / n
                        elif "ln" in expr:
                            val = math.log(n) / n if n > 1 else 0
                        elif "(1 + 1/n)^n" in expr:
                            val = (1 + 1 / n) ** n
                        elif "3^n / n!" in expr:
                            val = (3 ** n) / math.factorial(n)
                        elif "n^2/2^n" in expr:
                            val = (n ** 2) / (2 ** n)
                        else:
                            val = 1 / n
                        y_values.append(val)
                    except:
                        y_values.append(0)
                ax.set_ylabel(r'$a_n$', fontsize=12)
                title = rf'Sequence: ${latex_expr}$'

            # Create the plot with LaTeX labels
            ax.plot(n_values, y_values, 'bo-', linewidth=2, markersize=6)
            ax.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
            ax.grid(True, alpha=0.3)
            ax.set_xlabel(r'$n$', fontsize=12)
            ax.set_title(title, fontsize=10)
            ax.set_xticklabels([])
            ax.set_yticklabels([])
            ax.tick_params(axis='both', which='both', length=0)

            # Convert to PhotoImage
            buf = io.BytesIO()
            plt.savefig(buf, format='png', bbox_inches='tight', dpi=100, facecolor='white')
            buf.seek(0)
            img = Image.open(buf)
            photo = ImageTk.PhotoImage(img)
            plt.close(fig)

            return photo
        except Exception as e:
            print(f"Graph error: {e}")
            return None
class SequenceGame:
    """Game for practicing sequence convergence"""

    def __init__(self, parent):
        self.parent = parent
        self.parent.configure(bg='#2c3e50')

        self.latex_renderer = LaTeXRenderer()
        self.score = 0
        self.streak = 0
        self.lives = 3
        self.current_question = None
        self.difficulty = "Easy"

        self.sequence_database = self.build_sequence_database()
        self.setup_gui()
        self.new_question()

    def build_sequence_database(self):
        return {
            "Easy": [
                {"latex": r"a_n = \frac{1}{n}", "limit": "0", "explanation": "1/n → 0 as n→∞"},
                {"latex": r"a_n = \frac{n}{n+1}", "limit": "1", "explanation": "n/(n+1) → 1"},
                {"latex": r"a_n = \frac{2n}{3n+1}", "limit": r"\frac{2}{3}",
                 "explanation": "Divide numerator and denominator by n"},
                {"latex": r"a_n = \frac{1}{2^n}", "limit": "0", "explanation": "Geometric decay to 0"},
                {"latex": r"a_n = 2 + \frac{1}{n}", "limit": "2", "explanation": "2 + 1/n → 2"},
                {"latex": r"a_n = \frac{3n}{n+2}", "limit": "3", "explanation": "Divide by n: 3/(1+2/n) → 3"},
                {"latex": r"a_n = \frac{5}{n^2}", "limit": "0", "explanation": "5/n² → 0"},
                {"latex": r"a_n = \frac{n^2}{n^2+1}", "limit": "1", "explanation": "n²/(n²+1) → 1"},
                {"latex": r"a_n = \frac{4^n}{5^n}", "limit": "0", "explanation": "(4/5)^n → 0"},
                {"latex": r"a_n = (-1)^n \frac{1}{n}", "limit": "0", "explanation": "Alternating sequence → 0"},
            ],
            "Medium": [
                {"latex": r"a_n = \frac{\ln n}{n}", "limit": "0", "explanation": "ln n grows slower than n"},
                {"latex": r"a_n = \left(1 + \frac{1}{n}\right)^n", "limit": "e",
                 "explanation": "Famous limit → e ≈ 2.71828"},
                {"latex": r"a_n = \frac{3^n}{n!}", "limit": "0", "explanation": "Factorial dominates exponential"},
                {"latex": r"a_n = n \sin\left(\frac{1}{n}\right)", "limit": "1",
                 "explanation": "Use limit sin(x)/x → 1"},
                {"latex": r"a_n = \sqrt{n^2 + n} - n", "limit": r"\frac{1}{2}",
                 "explanation": "Rationalize: multiply by conjugate"},
                {"latex": r"a_n = \frac{n}{\ln n}", "limit": r"\infty", "explanation": "n grows faster than ln n → ∞"},
                {"latex": r"a_n = \left(1 + \frac{2}{n}\right)^{n}", "limit": "e^2", "explanation": "→ e² ≈ 7.389"},
                {"latex": r"a_n = \frac{\ln(n^2)}{n}", "limit": "0", "explanation": "2 ln n / n → 0"},
                {"latex": r"a_n = \frac{e^n}{n^n}", "limit": "0", "explanation": "Denominator grows faster"},
                {"latex": r"a_n = \frac{n^{100}}{1.01^n}", "limit": "0",
                 "explanation": "Exponential dominates polynomial"},
            ],
            "Hard": [
                {"latex": r"a_n = \frac{n!}{n^n}", "limit": "0", "explanation": "Stirling's approximation"},
                {"latex": r"a_n = \left(1 + \frac{2}{n}\right)^n", "limit": "e^2", "explanation": "→ e^2 ≈ 7.389"},
                {"latex": r"a_n = \frac{n^{1/n} - 1}{\ln n}", "limit": "0", "explanation": "Use L'Hôpital's rule"},
                {"latex": r"a_n = \frac{\sin n}{n}", "limit": "0", "explanation": "Bounded numerator / ∞ → 0"},
                {"latex": r"a_n = \left(\frac{n}{n+1}\right)^n", "limit": r"\frac{1}{e}",
                 "explanation": "→ 1/e ≈ 0.3679"},
                {"latex": r"a_n = \sqrt[n]{n}", "limit": "1", "explanation": "n^(1/n) → 1"},
                {"latex": r"a_n = \frac{\arctan n}{n}", "limit": "0",
                 "explanation": "arctan n → π/2, divided by n → 0"},
                {"latex": r"a_n = \left(1 + \frac{1}{n^2}\right)^n", "limit": "1", "explanation": "→ e^(1/n) → 1"},
                {"latex": r"a_n = \frac{n^n}{3^n n!}", "limit": "0", "explanation": "Stirling: (e/3)^n / √(2πn) → 0"},
                {"latex": r"a_n = \frac{\ln(n!)}{n \ln n}", "limit": "1",
                 "explanation": "Stirling: ln(n!) ~ n ln n - n"},
            ]
        }
    def setup_gui(self):
        self.create_widgets()

    def create_widgets(self):
        # Title
        title = tk.Label(self.parent, text="Sequence Convergence Practice",
                         font=('Arial', 20, 'bold'), bg='#2c3e50', fg='#ecf0f1')
        title.pack(pady=10)

        # Stats
        stats_frame = tk.Frame(self.parent, bg='#34495e', relief=tk.RAISED, bd=2)
        stats_frame.pack(pady=10, padx=20, fill=tk.X)

        self.score_label = tk.Label(stats_frame, text=f"Score: {self.score}",
                                    font=('Arial', 14), bg='#34495e', fg='#ecf0f1')
        self.score_label.pack(side=tk.LEFT, padx=20)

        self.streak_label = tk.Label(stats_frame, text=f"Streak: {self.streak} 🔥",
                                     font=('Arial', 14), bg='#34495e', fg='#e74c3c')
        self.streak_label.pack(side=tk.LEFT, padx=20)

        self.lives_label = tk.Label(stats_frame, text=f"Lives: {'❤️' * self.lives}",
                                    font=('Arial', 14), bg='#34495e', fg='#e74c3c')
        self.lives_label.pack(side=tk.LEFT, padx=20)

        # Sequence Display
        seq_frame = tk.Frame(self.parent, bg='#2c3e50', relief=tk.RIDGE, bd=3)
        seq_frame.pack(pady=10, padx=20, fill=tk.X)

        self.seq_canvas = tk.Canvas(seq_frame, bg='#ecf0f1', height=100)
        self.seq_canvas.pack(pady=10, fill=tk.X)
        self.seq_canvas.update_idletasks()

        # Question
        self.question_label = tk.Label(self.parent, text="What is the limit of this sequence (as n→∞)?",
                                       font=('Arial', 14), bg='#2c3e50', fg='#ecf0f1')
        self.question_label.pack(pady=10)

        # Answer
        answer_frame = tk.Frame(self.parent, bg='#2c3e50')
        answer_frame.pack(pady=10)

        self.answer_entry = tk.Entry(answer_frame, font=('Arial', 14), width=30)
        self.answer_entry.pack(side=tk.LEFT, padx=5)
        self.answer_entry.bind('<Return>', self.check_answer)

        submit_btn = tk.Button(answer_frame, text="Check Answer", command=self.check_answer,
                               font=('Arial', 12, 'bold'), bg='#3498db', fg='white')
        submit_btn.pack(side=tk.LEFT, padx=5)

        visualize_btn = tk.Button(answer_frame, text="Visualize", command=self.visualize_series,
                                  font=('Arial', 10, 'bold'), bg='#9b59b6', fg='white')
        visualize_btn.pack(side=tk.LEFT, padx=5)

        # Feedback
        self.feedback_label = tk.Label(self.parent, text="", font=('Arial', 12),
                                       bg='#2c3e50', fg='#ecf0f1', wraplength=700)
        self.feedback_label.pack(pady=10)

        # Next button
        self.next_btn = tk.Button(self.parent, text="Next Sequence →", command=self.new_question,
                                  font=('Arial', 12, 'bold'), bg='#27ae60', fg='white',
                                  state=tk.DISABLED)
        self.next_btn.pack(pady=10)

    def new_question(self):
        if self.difficulty in self.sequence_database:
            self.current_question = random.choice(self.sequence_database[self.difficulty])
            img = self.latex_renderer.render(self.current_question["latex"])
            if img:
                self.seq_canvas.delete("all")
                self.seq_canvas.create_image(350, 50, image=img, anchor='center')
                self.seq_canvas.image = img
            self.answer_entry.delete(0, tk.END)
            self.feedback_label.config(text="")
            self.next_btn.config(state=tk.DISABLED)

    def check_answer(self, event=None):
        user_answer = self.answer_entry.get().strip().lower()
        correct = self.current_question["limit"].lower()

        # Handle special cases
        is_correct = False
        if user_answer in ["e", "euler"] and correct == "e":
            is_correct = True
        elif user_answer == "1/e" and correct == r"\frac{1}{e}":
            is_correct = True
        elif user_answer == correct:
            is_correct = True
        else:
            try:
                if abs(float(eval(user_answer)) - float(eval(correct))) < 0.001:
                    is_correct = True
            except:
                pass

        if is_correct:
            points = 10 + (self.streak * 2)
            self.score += points
            self.streak += 1
            self.feedback_label.config(text=f"Correct! {self.current_question['explanation']}\n+{points} points!",
                                       fg='#2ecc71')
            self.next_btn.config(state=tk.NORMAL)
        else:
            self.lives -= 1
            self.streak = 0
            self.feedback_label.config(
                text=f"Wrong! Limit = {self.current_question['limit']}\n{self.current_question['explanation']}",
                fg='#e74c3c')
            self.lives_label.config(text=f"Lives: {'❤️' * max(0, self.lives)}")
            if self.lives <= 0:
                messagebox.showinfo("Game Over", f"Final score: {self.score}")
                self.reset_game()
            else:
                self.next_btn.config(state=tk.NORMAL)

        self.score_label.config(text=f"Score: {self.score}")
        self.streak_label.config(text=f"Streak: {self.streak} 🔥")

    def reset_game(self):
        self.score = 0
        self.streak = 0
        self.lives = 3
        self.score_label.config(text=f"Score: {self.score}")
        self.streak_label.config(text=f"Streak: {self.streak} 🔥")
        self.lives_label.config(text=f"Lives: {'❤️' * self.lives}")
        self.new_question()
        # graph visualization helper method

    def visualize_series(self):
        """Open a window showing a graph of the current series/sequence"""
        if hasattr(self, 'current_question') and self.current_question:
            latex_expr = self.current_question.get("latex", "")
        elif hasattr(self, 'current_series') and self.current_series:
            latex_expr = self.current_series.get("latex", "")
        elif hasattr(self, 'current_function') and self.current_function:
            latex_expr = self.current_function.get("function", "")
        else:
            messagebox.showinfo("Info", "No series to visualize")
            return

        # Generate the graph
        img = self.latex_renderer.graph_sequence_from_latex(latex_expr)

        if img:
            # Create popup window
            graph_window = tk.Toplevel(self.parent)
            graph_window.title("Mathematical Visualization")
            graph_window.geometry("700x600")
            graph_window.configure(bg='white')

            # Add LaTeX rendered function label at the top
            func_img = self.latex_renderer.render(latex_expr, bg_color='white', size=(600, 80))
            if func_img:
                func_label = tk.Label(graph_window, bg='white')
                func_label.pack(pady=10)
                func_label.config(image=func_img)
                func_label.image = func_img

            # Add canvas for the graph
            canvas = tk.Canvas(graph_window, bg='white', height=400, width=650)
            canvas.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
            canvas.create_image(325, 200, image=img, anchor='center')
            canvas.image = img

            # Add close button
            close_btn = tk.Button(graph_window, text="Close", command=graph_window.destroy,
                                  font=('Arial', 10), bg='#e74c3c', fg='white')
            close_btn.pack(pady=10)
        else:
            messagebox.showinfo("Info", "Graph not available for this expression")

class SeriesTestGame:
    """Comprehensive series convergence test practice"""

    def __init__(self, parent):
        self.parent = parent
        self.parent.configure(bg='#2c3e50')

        self.latex_renderer = LaTeXRenderer()
        self.score = 0
        self.streak = 0
        self.lives = 3
        self.current_series = None
        self.difficulty = "Medium"

        self.series_database = self.build_series_database()
        self.setup_gui()
        self.new_question()

    def build_series_database(self):
        return {
            "Easy": [
                {"latex": r"\sum_{n=1}^{\infty} \frac{1}{n^2}", "test": "p-series", "answer": "Converges",
                 "explanation": "p=2>1"},
                {"latex": r"\sum_{n=1}^{\infty} \frac{1}{n}", "test": "p-series", "answer": "Diverges",
                 "explanation": "Harmonic series diverges"},
                {"latex": r"\sum_{n=1}^{\infty} \frac{1}{\sqrt{n}}", "test": "p-series", "answer": "Diverges",
                 "explanation": "p=1/2<1"},
                {"latex": r"\sum_{n=0}^{\infty} \left(\frac{1}{2}\right)^n", "test": "Geometric", "answer": "Converges",
                 "explanation": "|r|=1/2<1"},
                {"latex": r"\sum_{n=0}^{\infty} 2^n", "test": "Geometric", "answer": "Diverges",
                 "explanation": "|r|=2>1"},
                {"latex": r"\sum_{n=1}^{\infty} \frac{1}{n^3}", "test": "p-series", "answer": "Converges",
                 "explanation": "p=3>1"},
                {"latex": r"\sum_{n=0}^{\infty} \left(\frac{3}{4}\right)^n", "test": "Geometric", "answer": "Converges",
                 "explanation": "|r|=3/4<1"},
                {"latex": r"\sum_{n=0}^{\infty} \left(\frac{4}{3}\right)^n", "test": "Geometric", "answer": "Diverges",
                 "explanation": "|r|=4/3>1"},
                {"latex": r"\sum_{n=1}^{\infty} \frac{1}{n^{0.5}}", "test": "p-series", "answer": "Diverges",
                 "explanation": "p=0.5<1"},
                {"latex": r"\sum_{n=1}^{\infty} \frac{1}{n^{2.5}}", "test": "p-series", "answer": "Converges",
                 "explanation": "p=2.5>1"},
            ],
            "Medium": [
                {"latex": r"\sum_{n=1}^{\infty} \frac{n}{n^2+1}", "test": "Limit Comparison", "answer": "Diverges",
                 "explanation": "Compare to 1/n"},
                {"latex": r"\sum_{n=1}^{\infty} \frac{1}{n^2+1}", "test": "Comparison", "answer": "Converges",
                 "explanation": "Compare to 1/n^2"},
                {"latex": r"\sum_{n=1}^{\infty} \frac{2^n}{3^n+1}", "test": "Geometric", "answer": "Converges",
                 "explanation": "~ (2/3)^n"},
                {"latex": r"\sum_{n=1}^{\infty} \frac{n^2}{2^n}", "test": "Ratio Test", "answer": "Converges",
                 "explanation": "Ratio = 1/2 < 1"},
                {"latex": r"\sum_{n=1}^{\infty} \frac{n!}{2^n}", "test": "Ratio Test", "answer": "Diverges",
                 "explanation": "Ratio = (n+1)/2 → ∞"},
                {"latex": r"\sum_{n=1}^{\infty} \frac{(-1)^n}{n}", "test": "Alternating Series", "answer": "Converges",
                 "explanation": "Alternating harmonic series converges conditionally"},
                {"latex": r"\int_{1}^{\infty} \frac{1}{x^2} dx", "test": "Integral Test", "answer": "Converges",
                 "explanation": "∫₁^∞ dx/x² = 1"},
                {"latex": r"\int_{1}^{\infty} \frac{1}{x} dx", "test": "Integral Test", "answer": "Diverges",
                 "explanation": "∫₁^∞ dx/x diverges"},
                {"latex": r"\sum_{n=1}^{\infty} \frac{3^n}{n^3}", "test": "Root Test", "answer": "Diverges",
                 "explanation": "Limit = 3 > 1"},
                {"latex": r"\sum_{n=1}^{\infty} \frac{n^3}{e^n}", "test": "Ratio Test", "answer": "Converges",
                 "explanation": "Ratio = 1/e < 1"},
                {"latex": r"\sum_{n=1}^{\infty} \frac{(-1)^n}{n^2}", "test": "Alternating Series",
                 "answer": "Converges", "explanation": "Absolutely convergent"},
                {"latex": r"\sum_{n=1}^{\infty} \frac{1}{n \ln n}", "test": "Integral Test", "answer": "Diverges",
                 "explanation": "∫ dx/(x ln x) diverges"},
            ],
            "Hard": [
                {"latex": r"\sum_{n=1}^{\infty} \frac{3^n n!}{n^n}", "test": "Ratio Test", "answer": "Diverges",
                 "explanation": "Ratio = 3/e > 1"},
                {"latex": r"\sum_{n=1}^{\infty} \left(\frac{n}{n+1}\right)^{n^2}", "test": "Root Test",
                 "answer": "Converges", "explanation": "Limit = 1/e < 1"},
                {"latex": r"\sum_{n=1}^{\infty} \frac{1}{n \ln n}", "test": "Integral Test", "answer": "Diverges",
                 "explanation": "∫ dx/(x ln x) = ln(ln x) diverges"},
                {"latex": r"\sum_{n=1}^{\infty} \frac{1}{n (\ln n)^2}", "test": "Integral Test", "answer": "Converges",
                 "explanation": "∫ dx/(x (ln x)²) = -1/ln x converges"},
                {"latex": r"\sum_{n=1}^{\infty} \frac{(-1)^n}{\sqrt{n}}", "test": "Alternating Series",
                 "answer": "Converges", "explanation": "Alternating series, terms → 0"},
                {"latex": r"\sum_{n=1}^{\infty} \frac{\sin n}{n^2}", "test": "Comparison", "answer": "Converges",
                 "explanation": "|sin n| ≤ 1, compare to 1/n²"},
                {"latex": r"\sum_{n=1}^{\infty} \frac{n!}{n^n}", "test": "Ratio Test", "answer": "Converges",
                 "explanation": "Ratio = (n+1)^{n} / n^{n} / (n+1) → 1/e < 1"},
                {"latex": r"\sum_{n=1}^{\infty} \frac{(-1)^n n}{n^2+1}", "test": "Alternating Series",
                 "answer": "Converges", "explanation": "Terms decrease to 0"},
                {"latex": r"\sum_{n=1}^{\infty} \frac{1}{n^{1+1/n}}", "test": "Limit Comparison", "answer": "Diverges",
                 "explanation": "Compare to 1/n"},
                {"latex": r"\sum_{n=1}^{\infty} \left(1 - \frac{1}{n}\right)^{n^2}", "test": "Root Test",
                 "answer": "Converges", "explanation": "Limit = 1/e < 1"},
            ]
        }
    def setup_gui(self):
        # Title
        title = tk.Label(self.parent, text="Series Convergence Test Master",
                         font=('Arial', 20, 'bold'), bg='#2c3e50', fg='#ecf0f1')
        title.pack(pady=10)

        # Stats
        stats_frame = tk.Frame(self.parent, bg='#34495e', relief=tk.RAISED, bd=2)
        stats_frame.pack(pady=10, padx=20, fill=tk.X)

        self.score_label = tk.Label(stats_frame, text=f"Score: {self.score}", font=('Arial', 14), bg='#34495e',
                                    fg='#ecf0f1')
        self.score_label.pack(side=tk.LEFT, padx=20)

        self.streak_label = tk.Label(stats_frame, text=f"Streak: {self.streak} 🔥", font=('Arial', 14), bg='#34495e',
                                     fg='#e74c3c')
        self.streak_label.pack(side=tk.LEFT, padx=20)

        self.lives_label = tk.Label(stats_frame, text=f"Lives: {'❤️' * self.lives}", font=('Arial', 14), bg='#34495e',
                                    fg='#e74c3c')
        self.lives_label.pack(side=tk.LEFT, padx=20)

        # Difficulty
        diff_frame = tk.Frame(stats_frame, bg='#34495e')
        diff_frame.pack(side=tk.RIGHT, padx=20)
        tk.Label(diff_frame, text="Difficulty:", bg='#34495e', fg='#ecf0f1').pack(side=tk.LEFT)
        self.diff_var = tk.StringVar(value="Medium")
        diff_menu = ttk.Combobox(diff_frame, textvariable=self.diff_var, values=["Easy", "Medium", "Hard"],
                                 state="readonly")
        diff_menu.pack(side=tk.LEFT, padx=5)
        diff_menu.bind('<<ComboboxSelected>>', self.change_difficulty)

        # Series Display
        series_frame = tk.Frame(self.parent, bg='#ecf0f1', relief=tk.RIDGE, bd=3)
        series_frame.pack(pady=10, padx=20, fill=tk.X)

        self.series_canvas = tk.Canvas(series_frame, bg='#ecf0f1', height=100)
        self.series_canvas.pack(pady=10, fill=tk.X)

        # Test selection
        self.test_question = tk.Label(self.parent, text="Which test is most appropriate? Then determine convergence:",
                                      font=('Arial', 14), bg='#2c3e50', fg='#ecf0f1')
        self.test_question.pack(pady=5)

        self.test_choice_var = tk.StringVar()
        test_frame = tk.Frame(self.parent, bg='#2c3e50')
        test_frame.pack(pady=5)

        tests = ["p-series", "Geometric", "Ratio Test", "Root Test", "Integral Test", "Comparison", "Limit Comparison",
                 "Alternating Series"]
        self.test_menu = ttk.Combobox(test_frame, textvariable=self.test_choice_var, values=tests, width=20)
        self.test_menu.pack(side=tk.LEFT, padx=5)

        self.conv_question = tk.Label(self.parent, text="Does it converge or diverge?",
                                      font=('Arial', 14), bg='#2c3e50', fg='#ecf0f1')
        self.conv_question.pack(pady=5)

        self.conv_var = tk.StringVar()
        conv_frame = tk.Frame(self.parent, bg='#2c3e50')
        conv_frame.pack(pady=5)

        self.conv_menu = ttk.Combobox(conv_frame, textvariable=self.conv_var, values=["Converges", "Diverges"],
                                      width=15)
        self.conv_menu.pack(side=tk.LEFT, padx=5)

        check_btn = tk.Button(conv_frame, text="Check Answer", command=self.check_answer,
                              font=('Arial', 12, 'bold'), bg='#3498db', fg='white')
        check_btn.pack(side=tk.LEFT, padx=5)

        visualize_btn = tk.Button(conv_frame, text="Visualize", command=self.visualize_series,
                                  font=('Arial', 10, 'bold'), bg='#9b59b6', fg='white')
        visualize_btn.pack(side=tk.LEFT, padx=5)


        # Feedback
        self.feedback_label = tk.Label(self.parent, text="", font=('Arial', 12), bg='#2c3e50', fg='#ecf0f1',
                                       wraplength=700)
        self.feedback_label.pack(pady=10)

        self.next_btn = tk.Button(self.parent, text="Next Series →", command=self.new_question,
                                  font=('Arial', 12, 'bold'), bg='#27ae60', fg='white', state=tk.DISABLED)
        self.next_btn.pack(pady=10)

    def new_question(self):
        self.current_series = random.choice(self.series_database[self.difficulty])
        img = self.latex_renderer.render(self.current_series["latex"])
        if img:
            self.series_canvas.delete("all")
            self.series_canvas.create_image(350, 50, image=img, anchor='center')
            self.series_canvas.image = img
        self.test_choice_var.set("")
        self.conv_var.set("")
        self.feedback_label.config(text="")
        self.next_btn.config(state=tk.DISABLED)

    def check_answer(self):
        selected_test = self.test_choice_var.get().lower()
        selected_conv = self.conv_var.get().lower()
        correct_test = self.current_series["test"].lower()
        correct_conv = self.current_series["answer"].lower()

        test_correct = selected_test == correct_test
        conv_correct = selected_conv == correct_conv

        if test_correct and conv_correct:
            points = 20 + (self.streak * 3)
            self.score += points
            self.streak += 1
            self.feedback_label.config(text=f"Perfect! {self.current_series['explanation']}\n+{points} points!",
                                       fg='#2ecc71')
            self.next_btn.config(state=tk.NORMAL)
        elif test_correct or conv_correct:
            points = 10
            self.score += points
            self.streak = max(0, self.streak - 1)
            self.feedback_label.config(
                text=f"Partially correct. Test: {correct_test}, Result: {correct_conv}\n+{points} points",
                fg='#f39c12')
            self.next_btn.config(state=tk.NORMAL)
        else:
            self.lives -= 1
            self.streak = 0
            self.feedback_label.config(
                text=f"Wrong! Test: {correct_test}, Result: {correct_conv}\n{self.current_series['explanation']}",
                fg='#e74c3c')
            self.lives_label.config(text=f"Lives: {'❤️' * max(0, self.lives)}")
            if self.lives <= 0:
                messagebox.showinfo("Game Over", f"Final score: {self.score}")
                self.reset_game()
                return
            else:
                self.next_btn.config(state=tk.NORMAL)

        self.score_label.config(text=f"Score: {self.score}")
        self.streak_label.config(text=f"Streak: {self.streak} 🔥")

    def change_difficulty(self, event=None):
        self.difficulty = self.diff_var.get()
        self.new_question()

    def reset_game(self):
        self.score = 0
        self.streak = 0
        self.lives = 5
        self.score_label.config(text=f"Score: {self.score}")
        self.streak_label.config(text=f"Streak: {self.streak} 🔥")
        self.lives_label.config(text=f"Lives: {'❤️' * self.lives}")
        self.new_question()

    def visualize_series(self):
        """Open a window showing a graph of the current series/sequence"""
        if hasattr(self, 'current_question') and self.current_question:
            latex_expr = self.current_question.get("latex", "")
        elif hasattr(self, 'current_series') and self.current_series:
            latex_expr = self.current_series.get("latex", "")
        elif hasattr(self, 'current_function') and self.current_function:
            latex_expr = self.current_function.get("function", "")
        else:
            messagebox.showinfo("Info", "No series to visualize")
            return

        # Generate the graph
        img = self.latex_renderer.graph_sequence_from_latex(latex_expr)

        if img:
            # Create popup window
            graph_window = tk.Toplevel(self.parent)
            graph_window.title("Mathematical Visualization")
            graph_window.geometry("700x600")
            graph_window.configure(bg='white')

            # Add LaTeX rendered function label at the top
            func_img = self.latex_renderer.render(latex_expr, bg_color='white', size=(600, 80))
            if func_img:
                func_label = tk.Label(graph_window, bg='white')
                func_label.pack(pady=10)
                func_label.config(image=func_img)
                func_label.image = func_img

            # Add canvas for the graph
            canvas = tk.Canvas(graph_window, bg='white', height=400, width=650)
            canvas.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
            canvas.create_image(325, 200, image=img, anchor='center')
            canvas.image = img

            # Add close button
            close_btn = tk.Button(graph_window, text="Close", command=graph_window.destroy,
                                  font=('Arial', 10), bg='#e74c3c', fg='white')
            close_btn.pack(pady=10)
        else:
            messagebox.showinfo("Info", "Graph not available for this expression")
class PowerSeriesGame:
    """Practice radius and interval of convergence for power series"""

    def __init__(self, parent):
        self.parent = parent
        self.parent.configure(bg='#2c3e50')

        self.latex_renderer = LaTeXRenderer()
        self.score = 0
        self.streak = 0
        self.lives = 3
        self.current_series = None

        self.power_series_db = [
            {"latex": r"\sum_{n=0}^{\infty} x^n", "radius": "1", "interval": "(-1,1)", "center": "0"},
            {"latex": r"\sum_{n=0}^{\infty} \frac{x^n}{n!}", "radius": r"\infty", "interval": "(-\\infty, \\infty)",
             "center": "0"},
            {"latex": r"\sum_{n=1}^{\infty} \frac{x^n}{n}", "radius": "1", "interval": "[-1,1)", "center": "0"},
            {"latex": r"\sum_{n=1}^{\infty} \frac{(-1)^n x^n}{n}", "radius": "1", "interval": "(-1,1]", "center": "0"},
            {"latex": r"\sum_{n=0}^{\infty} n x^n", "radius": "1", "interval": "(-1,1)", "center": "0"},
            {"latex": r"\sum_{n=0}^{\infty} \frac{(x-2)^n}{3^n}", "radius": "3", "interval": "(-1,5)", "center": "2"},
            {"latex": r"\sum_{n=0}^{\infty} \frac{(-1)^n (x+1)^n}{\sqrt{n}}", "radius": "1", "interval": "(-2,0]",
             "center": "-1"},
            {"latex": r"\sum_{n=0}^{\infty} \frac{x^{2n}}{n!}", "radius": r"\infty", "interval": "(-\\infty, \\infty)",
             "center": "0"},
            {"latex": r"\sum_{n=1}^{\infty} \frac{x^n}{\sqrt{n}}", "radius": "1", "interval": "[-1,1)", "center": "0"},
            {"latex": r"\sum_{n=1}^{\infty} \frac{(-1)^n x^{2n}}{n}", "radius": "1", "interval": "[-1,1]",
             "center": "0"},
            {"latex": r"\sum_{n=0}^{\infty} \frac{(x+3)^n}{2^n}", "radius": "2", "interval": "(-5,-1)", "center": "-3"},
            {"latex": r"\sum_{n=0}^{\infty} \frac{n! x^n}{n^n}", "radius": "e", "interval": "(-e, e)", "center": "0"},
            {"latex": r"\sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{(2n+1)!}", "radius": r"\infty",
             "interval": "(-\\infty, \\infty)", "center": "0"},
            {"latex": r"\sum_{n=0}^{\infty} \frac{(-1)^n x^{2n}}{(2n)!}", "radius": r"\infty",
             "interval": "(-\\infty, \\infty)", "center": "0"},
        ]

        self.setup_gui()
        self.new_question()

    def setup_gui(self):
        title = tk.Label(self.parent, text="Power Series: Radius & Interval of Convergence",
                         font=('Arial', 20, 'bold'), bg='#2c3e50', fg='#ecf0f1')
        title.pack(pady=10)

        self.score_label = tk.Label(self.parent, text=f"Score: {self.score}", font=('Arial', 14), bg='#2c3e50',
                                    fg='#ecf0f1')
        self.score_label.pack()

        self.streak_label = tk.Label(self.parent, text=f"Streak: {self.streak} 🔥", font=('Arial', 14), bg='#2c3e50',
                                     fg='#e74c3c')
        self.streak_label.pack()

        self.lives_label = tk.Label(self.parent, text=f"Lives: {'❤️' * self.lives}", font=('Arial', 14), bg='#2c3e50',
                                    fg='#e74c3c')
        self.lives_label.pack()

        series_frame = tk.Frame(self.parent, bg='#ecf0f1', relief=tk.RAISED, bd=3)
        series_frame.pack(pady=10, padx=20, fill=tk.X)

        self.series_canvas = tk.Canvas(series_frame, bg='#ecf0f1', height=100)
        self.series_canvas.pack(pady=10, fill=tk.X)

        # Questions
        q_frame = tk.Frame(self.parent, bg='#2c3e50')
        q_frame.pack(pady=10)

        tk.Label(q_frame, text="Radius of Convergence:", bg='#2c3e50', fg='#ecf0f1', font=('Arial', 12)).grid(row=0,
                                                                                                              column=0,
                                                                                                              padx=5)
        self.radius_entry = tk.Entry(q_frame, font=('Arial', 12), width=15)
        self.radius_entry.grid(row=0, column=1, padx=5)

        tk.Label(q_frame, text="Interval of Convergence:", bg='#2c3e50', fg='#ecf0f1', font=('Arial', 12)).grid(row=1,
                                                                                                                column=0,
                                                                                                                padx=5)
        self.interval_entry = tk.Entry(q_frame, font=('Arial', 12), width=25)
        self.interval_entry.grid(row=1, column=1, padx=5)

        submit_btn = tk.Button(q_frame, text="Check Answer", command=self.check_answer,
                               font=('Arial', 12, 'bold'), bg='#3498db', fg='white')
        submit_btn.grid(row=2, column=0, columnspan=2, pady=10)

        visualize_btn = tk.Button(q_frame, text="Visualize", command=self.visualize_series,
                                  font=('Arial', 10, 'bold'), bg='#9b59b6', fg='white')
        visualize_btn.grid(row=2, column=2, padx=5, pady=10)

        self.feedback_label = tk.Label(self.parent, text="", font=('Arial', 12), bg='#2c3e50', fg='#ecf0f1',
                                       wraplength=700)
        self.feedback_label.pack(pady=10)

        self.next_btn = tk.Button(self.parent, text="Next Series →", command=self.new_question,
                                  font=('Arial', 12, 'bold'), bg='#27ae60', fg='white', state=tk.DISABLED)
        self.next_btn.pack(pady=10)

    def new_question(self):
        self.current_series = random.choice(self.power_series_db)
        img = self.latex_renderer.render(self.current_series["latex"], bg_color='#ecf0f1')
        if img:
            self.series_canvas.delete("all")
            self.series_canvas.create_image(350, 50, image=img, anchor='center')
            self.series_canvas.image = img
        self.radius_entry.delete(0, tk.END)
        self.interval_entry.delete(0, tk.END)
        self.feedback_label.config(text="")
        self.next_btn.config(state=tk.DISABLED)

    def check_answer(self):
        user_radius = self.radius_entry.get().strip()
        user_interval = self.interval_entry.get().strip()
        correct_radius = self.current_series["radius"]
        correct_interval = self.current_series["interval"]

        radius_correct = user_radius == correct_radius
        interval_correct = user_interval == correct_interval

        if radius_correct and interval_correct:
            points = 20 + (self.streak * 3)
            self.score += points
            self.streak += 1
            self.feedback_label.config(text=f"Perfect! R = {correct_radius}, I = {correct_interval}\n+{points} points!",
                                       fg='#2ecc71')
            self.next_btn.config(state=tk.NORMAL)
        elif radius_correct or interval_correct:
            points = 10
            self.score += points
            self.streak = max(0, self.streak - 1)
            self.feedback_label.config(
                text=f"Partially correct. R = {correct_radius}, I = {correct_interval}\n+{points} points",
                fg='#f39c12')
            self.next_btn.config(state=tk.NORMAL)
        else:
            self.lives -= 1
            self.streak = 0
            self.feedback_label.config(text=f"Wrong! R = {correct_radius}, I = {correct_interval}", fg='#e74c3c')
            self.lives_label.config(text=f"Lives: {'❤️' * max(0, self.lives)}")
            if self.lives <= 0:
                messagebox.showinfo("Game Over", f"Final score: {self.score}")
                self.reset_game()
                return
            else:
                self.next_btn.config(state=tk.NORMAL)

        self.score_label.config(text=f"Score: {self.score}")
        self.streak_label.config(text=f"Streak: {self.streak} 🔥")

    def reset_game(self):
        self.score = 0
        self.streak = 0
        self.lives = 3
        self.score_label.config(text=f"Score: {self.score}")
        self.streak_label.config(text=f"Streak: {self.streak} 🔥")
        self.lives_label.config(text=f"Lives: {'❤️' * self.lives}")
        self.new_question()

    def visualize_series(self):
        """Open a window showing a graph of the current series/sequence"""
        if hasattr(self, 'current_question') and self.current_question:
            latex_expr = self.current_question.get("latex", "")
        elif hasattr(self, 'current_series') and self.current_series:
            latex_expr = self.current_series.get("latex", "")
        elif hasattr(self, 'current_function') and self.current_function:
            latex_expr = self.current_function.get("function", "")
        else:
            messagebox.showinfo("Info", "No series to visualize")
            return

        # Generate the graph
        img = self.latex_renderer.graph_sequence_from_latex(latex_expr)

        if img:
            # Create popup window
            graph_window = tk.Toplevel(self.parent)
            graph_window.title("Mathematical Visualization")
            graph_window.geometry("700x600")
            graph_window.configure(bg='white')

            # Add LaTeX rendered function label at the top
            func_img = self.latex_renderer.render(latex_expr, bg_color='white', size=(600, 80))
            if func_img:
                func_label = tk.Label(graph_window, bg='white')
                func_label.pack(pady=10)
                func_label.config(image=func_img)
                func_label.image = func_img

            # Add canvas for the graph
            canvas = tk.Canvas(graph_window, bg='white', height=400, width=650)
            canvas.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
            canvas.create_image(325, 200, image=img, anchor='center')
            canvas.image = img

            # Add close button
            close_btn = tk.Button(graph_window, text="Close", command=graph_window.destroy,
                                  font=('Arial', 10), bg='#e74c3c', fg='white')
            close_btn.pack(pady=10)
        else:
            messagebox.showinfo("Info", "Graph not available for this expression")

class TaylorSeriesGame:
    """Practice constructing Taylor and Maclaurin series with LaTeX buttons"""

    def __init__(self, parent):
        self.parent = parent
        self.parent.configure(bg='#2c3e50')

        self.latex_renderer = LaTeXRenderer()
        self.score = 0
        self.streak = 0
        self.lives = 3
        self.current_function = None
        self.current_term_index = None
        self.button_images = []

        self.taylor_db = [
            # Original functions
            {"function": r"e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!}",
             "center": "0",
             "terms": ["1", "x", r"\frac{x^2}{2!}", r"\frac{x^3}{3!}", r"\frac{x^4}{4!}", r"\frac{x^5}{5!}"]},

            {"function": r"\sin x = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{(2n+1)!}",
             "center": "0",
             "terms": ["x", r"-\frac{x^3}{3!}", r"\frac{x^5}{5!}", r"-\frac{x^7}{7!}", r"\frac{x^9}{9!}"]},

            {"function": r"\cos x = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n}}{(2n)!}",
             "center": "0",
             "terms": ["1", r"-\frac{x^2}{2!}", r"\frac{x^4}{4!}", r"-\frac{x^6}{6!}", r"\frac{x^8}{8!}"]},

            {"function": r"\ln(1+x) = \sum_{n=1}^{\infty} \frac{(-1)^{n-1} x^n}{n}",
             "center": "0",
             "terms": ["x", r"-\frac{x^2}{2}", r"\frac{x^3}{3}", r"-\frac{x^4}{4}", r"\frac{x^5}{5}"]},

            {"function": r"\arctan x = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{2n+1}",
             "center": "0",
             "terms": ["x", r"-\frac{x^3}{3}", r"\frac{x^5}{5}", r"-\frac{x^7}{7}", r"\frac{x^9}{9}"]},

            {"function": r"\frac{1}{1-x} = \sum_{n=0}^{\infty} x^n",
             "center": "0",
             "terms": ["1", "x", "x^2", "x^3", "x^4"]},

            # New additional functions
            {"function": r"\frac{1}{1+x} = \sum_{n=0}^{\infty} (-1)^n x^n",
             "center": "0",
             "terms": ["1", "-x", "x^2", "-x^3", "x^4"]},

            {"function": r"\frac{1}{1-x^2} = \sum_{n=0}^{\infty} x^{2n}",
             "center": "0",
             "terms": ["1", "x^2", "x^4", "x^6", "x^8"]},

            {"function": r"\tan^{-1}(x^2) = \sum_{n=0}^{\infty} \frac{(-1)^n x^{4n+2}}{2n+1}",
             "center": "0",
             "terms": ["x^2", r"-\frac{x^6}{3}", r"\frac{x^{10}}{5}", r"-\frac{x^{14}}{7}", r"\frac{x^{18}}{9}"]},

            {"function": r"\sinh x = \sum_{n=0}^{\infty} \frac{x^{2n+1}}{(2n+1)!}",
             "center": "0",
             "terms": ["x", r"\frac{x^3}{3!}", r"\frac{x^5}{5!}", r"\frac{x^7}{7!}", r"\frac{x^9}{9!}"]},

            {"function": r"\cosh x = \sum_{n=0}^{\infty} \frac{x^{2n}}{(2n)!}",
             "center": "0",
             "terms": ["1", r"\frac{x^2}{2!}", r"\frac{x^4}{4!}", r"\frac{x^6}{6!}", r"\frac{x^8}{8!}"]},

            {"function": r"\frac{1}{(1-x)^2} = \sum_{n=0}^{\infty} (n+1)x^n",
             "center": "0",
             "terms": ["1", "2x", "3x^2", "4x^3", "5x^4"]},
        ]
        self.setup_gui()
        self.new_question()

    def setup_gui(self):
        # Title
        title = tk.Label(self.parent, text="Taylor & Maclaurin Series Constructor",
                         font=('Arial', 20, 'bold'), bg='#2c3e50', fg='#ecf0f1')
        title.pack(pady=10)

        # Score and Stats
        self.score_label = tk.Label(self.parent, text=f"Score: {self.score}",
                                    font=('Arial', 14), bg='#2c3e50', fg='#ecf0f1')
        self.score_label.pack()

        self.streak_label = tk.Label(self.parent, text=f"Streak: {self.streak} 🔥",
                                     font=('Arial', 14), bg='#2c3e50', fg='#e74c3c')
        self.streak_label.pack()

        self.lives_label = tk.Label(self.parent, text=f"Lives: {'❤️' * self.lives}",
                                    font=('Arial', 14), bg='#2c3e50', fg='#e74c3c')
        self.lives_label.pack()

        # Function display
        func_frame = tk.Frame(self.parent, bg='#ecf0f1', relief=tk.RIDGE, bd=3)
        func_frame.pack(pady=20, padx=20, fill=tk.X)

        self.func_canvas = tk.Canvas(func_frame, bg='#ecf0f1', height=100)
        self.func_canvas.pack(pady=10, fill=tk.BOTH, expand=True)

        self.center_label = tk.Label(func_frame, text="", font=('Arial', 14),
                                     bg='#ecf0f1', fg='#2c3e50')
        self.center_label.pack(pady=5)

        # Series display
        series_frame = tk.Frame(self.parent, bg='#2c3e50')
        series_frame.pack(pady=10)

        self.series_label = tk.Label(series_frame, text="Current series:",
                                     font=('Arial', 14), bg='#2c3e50', fg='#ecf0f1')
        self.series_label.pack()

        self.series_canvas = tk.Canvas(series_frame, bg='#2c3e50', height=80)
        self.series_canvas.pack(pady=5, fill=tk.BOTH, expand=True)

        # Question
        self.question_label = tk.Label(self.parent, text="Select the correct next term:",
                                       font=('Arial', 14, 'bold'), bg='#2c3e50', fg='#ecf0f1')
        self.question_label.pack(pady=10)
        # Add this after the question_label (before choice_frame)
        button_frame = tk.Frame(self.parent, bg='#2c3e50')
        button_frame.pack(pady=5)

        visualize_btn = tk.Button(button_frame, text="Visualize Series", command=self.visualize_series,
                                  font=('Arial', 10, 'bold'), bg='#9b59b6', fg='white')
        visualize_btn.pack()

        # Multiple choice frame with grid layout (2 rows x 2 columns)
        self.choice_frame = tk.Frame(self.parent, bg='#2c3e50')
        self.choice_frame.pack(pady=20, padx=20, fill=tk.X)

        self.choice_buttons = []

        # Feedback
        self.feedback_canvas = tk.Canvas(self.parent, bg='#2c3e50', height=60)
        self.feedback_canvas.pack(pady=10, fill=tk.X)

        # Next button
        self.next_btn = tk.Button(self.parent, text="Next Function →", command=self.new_question,
                                  font=('Arial', 12, 'bold'), bg='#27ae60', fg='white',
                                  state=tk.DISABLED, cursor='hand2')
        self.next_btn.pack(pady=10)

    def new_question(self):
        # Clear previous button images
        self.button_images.clear()

        # Clear ALL widgets from choice_frame
        for widget in self.choice_frame.winfo_children():
            widget.destroy()
        self.choice_buttons.clear()

        # Reconfigure grid columns and rows
        for i in range(2):
            self.choice_frame.grid_columnconfigure(i, weight=1)
        for i in range(2):
            self.choice_frame.grid_rowconfigure(i, weight=1)

        # Select random function
        self.current_function = random.choice(self.taylor_db)

        # Display function
        func_img = self.latex_renderer.render(self.current_function["function"],
                                              bg_color='#ecf0f1', size=(600, 80))
        if func_img:
            self.func_canvas.delete("all")
            self.func_canvas.create_image(300, 50, image=func_img, anchor='center')
            self.func_canvas.image = func_img

        self.center_label.config(text=f"Center at x = {self.current_function['center']}")

        # Randomly choose which term to ask for (0-indexed)
        max_index = len(self.current_function["terms"]) - 1
        self.current_term_index = random.randint(0, max_index)

        # Display series so far
        if self.current_term_index > 0:
            terms_so_far = self.current_function["terms"][:self.current_term_index]
            series_so_far = " + ".join(terms_so_far) + " + \\cdots"
            series_img = self.latex_renderer.render(series_so_far, bg_color='#2c3e50', size=(600, 60))
            if series_img:
                self.series_canvas.delete("all")
                self.series_canvas.create_image(300, 40, image=series_img, anchor='center')
                self.series_canvas.image = series_img
        else:
            series_img = self.latex_renderer.render("\\text{Empty series} + \\cdots",
                                                    bg_color='#2c3e50', size=(400, 60))
            if series_img:
                self.series_canvas.delete("all")
                self.series_canvas.create_image(200, 40, image=series_img, anchor='center')
                self.series_canvas.image = series_img

        self.question_label.config(text=f"What is term #{self.current_term_index + 1} of the series?")

        # Generate options
        correct_term = self.current_function["terms"][self.current_term_index]

        # Generate wrong options
        wrong_options = []
        for _ in range(3):
            other_func = random.choice(self.taylor_db)
            wrong_idx = random.randint(0, len(other_func["terms"]) - 1)
            wrong_term = other_func["terms"][wrong_idx]
            while wrong_term in wrong_options or wrong_term == correct_term:
                other_func = random.choice(self.taylor_db)
                wrong_idx = random.randint(0, len(other_func["terms"]) - 1)
                wrong_term = other_func["terms"][wrong_idx]
            wrong_options.append(wrong_term)

        options = [correct_term] + wrong_options
        random.shuffle(options)

        # Create new buttons
        for i, option in enumerate(options):
            btn_img = self.latex_renderer.render_small(option, bg_color='#3498db', size=(400, 50))
            if btn_img:
                btn = tk.Button(self.choice_frame, image=btn_img,
                                command=lambda x=option: self.check_answer(x),
                                bg='#3498db', activebackground='#2980b9',
                                borderwidth=0, cursor='hand2')
                btn.image = btn_img
                self.button_images.append(btn_img)
            else:
                btn = tk.Button(self.choice_frame, text=option, font=('Courier', 12),
                                command=lambda x=option: self.check_answer(x),
                                bg='#3498db', fg='white', activebackground='#2980b9',
                                cursor='hand2')

            row = i // 2
            col = i % 2
            btn.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
            self.choice_buttons.append(btn)

        self.current_correct = correct_term
        self.feedback_canvas.delete("all")
        self.next_btn.config(state=tk.DISABLED)
    def check_answer(self, selected_term):
        if selected_term == self.current_correct:
            # Correct answer
            points = 15 + (self.streak * 2)
            self.score += points
            self.streak += 1

            # Show correct feedback with LaTeX
            feedback_text = f"\\text{{Correct! }} {self.current_correct} \\text{{ is the right term.}} +{points} \\text{{ points!}}"
            feedback_img = self.latex_renderer.render_small(feedback_text, bg_color='#2c3e50', size=(600, 40))
            if feedback_img:
                self.feedback_canvas.delete("all")
                self.feedback_canvas.create_image(300, 30, image=feedback_img, anchor='center')
                self.feedback_canvas.image = feedback_img
        else:
            # Wrong answer
            self.lives -= 1
            self.streak = 0

            feedback_text = f"\\text{{Wrong! The correct term is }} {self.current_correct}"
            feedback_img = self.latex_renderer.render_small(feedback_text, bg_color='#2c3e50', size=(600, 40))
            if feedback_img:
                self.feedback_canvas.delete("all")
                self.feedback_canvas.create_image(300, 30, image=feedback_img, anchor='center')
                self.feedback_canvas.image = feedback_img

            self.lives_label.config(text=f"Lives: {'❤️' * max(0, self.lives)}")

            if self.lives <= 0:
                messagebox.showinfo("Game Over", f"Game Over! Your final score: {self.score}")
                self.reset_game()
                return

        self.score_label.config(text=f"Score: {self.score}")
        self.streak_label.config(text=f"Streak: {self.streak} 🔥")

        # Disable all answer buttons after answering
        for btn in self.choice_buttons:
            btn.config(state=tk.DISABLED)

        # Enable the Next button
        self.next_btn.config(state=tk.NORMAL)

    def visualize_series(self):
        """Open a window showing a graph of the current series/sequence"""
        if hasattr(self, 'current_question') and self.current_question:
            latex_expr = self.current_question.get("latex", "")
        elif hasattr(self, 'current_series') and self.current_series:
            latex_expr = self.current_series.get("latex", "")
        elif hasattr(self, 'current_function') and self.current_function:
            latex_expr = self.current_function.get("function", "")
        else:
            messagebox.showinfo("Info", "No series to visualize")
            return

        # Generate the graph
        img = self.latex_renderer.graph_sequence_from_latex(latex_expr)

        if img:
            # Create popup window
            graph_window = tk.Toplevel(self.parent)
            graph_window.title("Mathematical Visualization")
            graph_window.geometry("700x600")
            graph_window.configure(bg='white')

            # Add LaTeX rendered function label at the top
            func_img = self.latex_renderer.render(latex_expr, bg_color='white', size=(600, 80))
            if func_img:
                func_label = tk.Label(graph_window, bg='white')
                func_label.pack(pady=10)
                func_label.config(image=func_img)
                func_label.image = func_img

            # Add canvas for the graph
            canvas = tk.Canvas(graph_window, bg='white', height=400, width=650)
            canvas.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
            canvas.create_image(325, 200, image=img, anchor='center')
            canvas.image = img

            # Add close button
            close_btn = tk.Button(graph_window, text="Close", command=graph_window.destroy,
                                  font=('Arial', 10), bg='#e74c3c', fg='white')
            close_btn.pack(pady=10)
        else:
            messagebox.showinfo("Info", "Graph not available for this expression")

    def reset_game(self):
        self.score = 0
        self.streak = 0
        self.lives = 3
        self.score_label.config(text=f"Score: {self.score}")
        self.streak_label.config(text=f"Streak: {self.streak} 🔥")
        self.lives_label.config(text=f"Lives: {'❤️' * self.lives}")
        self.new_question()

def main():
    root = tk.Tk()
    root.title("Complete Series Master - All Topics Covered!")
    root.geometry("1000x1280")

    # Create notebook for all game modes
    notebook = ttk.Notebook(root)
    notebook.pack(fill='both', expand=True)

    style = ttk.Style()
    style.theme_use('clam')
    style.configure('TNotebook', tabmargins=[10, 5, 10, 5])
    style.configure('TNotebook.Tab', font=('Arial', 15, 'bold'), padding=[40, 15])

    # Force the style to apply
    style.layout('TNotebook.Tab', [('Notebook.tab', {'sticky': 'nswe', 'children': [
        ('Notebook.padding', {'side': 'top', 'sticky': 'nswe', 'children': [
            ('Notebook.focus', {'side': 'top', 'sticky': 'nswe', 'children': [
                ('Notebook.label', {'side': 'top', 'sticky': ''})
            ]})
        ]})
    ]})])

    # 1. Sequences Game
    frame1 = tk.Frame(notebook)
    frame1.configure(bg='#2c3e50')
    notebook.add(frame1, text='1. Sequences')
    SequenceGame(frame1)

    # 2. Series Tests Game
    frame2 = tk.Frame(notebook)
    frame2.configure(bg='#2c3e50')
    notebook.add(frame2, text='2. Series Tests')
    SeriesTestGame(frame2)

    # 3. Power Series Game
    frame3 = tk.Frame(notebook)
    frame3.configure(bg='#2c3e50')
    notebook.add(frame3, text='3. Power Series')
    PowerSeriesGame(frame3)

    # 4. Taylor/Maclaurin Series Game
    frame4 = tk.Frame(notebook)
    frame4.configure(bg='#2c3e50')
    notebook.add(frame4, text='4. Taylor/Maclaurin')
    TaylorSeriesGame(frame4)

    root.mainloop()


if __name__ == "__main__":
    main()