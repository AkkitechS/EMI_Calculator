from tkinter import Button, DoubleVar, Entry, Label, StringVar, Tk
from fpdf import FPDF
import datetime as dt


def calculate():
    p = principal.get()
    n = noi.get()
    r = roi.get()
    r = r / (12 * 100)
    n = n * 12
    rpn = ((1 + r) ** n)
    e = (p * r * rpn) / (rpn - 1)
    pa = e * n
    ta = pa - p
    emi.set(e)
    total_interest.set(ta)
    payable_amount.set(pa)


def conversion():
    month = conv.get()
    month = month / 12
    conv1.set(month)

def printPdf():
    pdf = FPDF()
    date = str(dt.datetime.now())
    pdf.add_page(orientation='L')
    pdf.set_font("Arial", size=30)
    pdf.set_margins(left=10.0, top=20.0, right=10.0)
    pdf.cell(w=0, h=10, txt="EMI report", align="C")
    pdf.set_font_size(size=20)
    pdf.cell(w=0, h=10, txt=f"{dt.datetime.now()}", align="R", ln=1)
    pdf.cell(w=0, h=10, txt=f"Loan Amount         :", align="L")
    pdf.cell(w=0, h=10, txt=f"{principal.get()}", align="R", ln=1)
    pdf.cell(w=0, h=10, txt=f"Rate of Interest    :", align="L")
    pdf.cell(w=0, h=10, txt=f"{roi.get()}", align="R", ln=1)
    pdf.cell(w=0, h=10, txt=f"Time period of loan :", align="L")
    pdf.cell(w=0, h=10, txt=f"{noi.get()}", align="R", ln=1)
    pdf.cell(w=0, h=10, txt=f"Monthly EMI         :", align="L")
    pdf.cell(w=0, h=10, txt=f"{emi.get()}", align="R", ln=1)
    pdf.cell(w=0, h=10, txt=f"Total Interest      :", align="L")
    pdf.cell(w=0, h=10, txt=f"{total_interest.get()}", align="R", ln=1)
    pdf.cell(w=0, h=10, txt=f"payable amount      :", align="L")
    pdf.cell(w=0, h=10, txt=f"{payable_amount.get()}", align="R", ln=1)
    pdf.output("emi-report-" + date[:10] + "-" + date[11:19].replace(":", "-") + ".pdf")


root = Tk()
root.geometry("700x200")
root.title("EMI Calculator")
Label(root, text="Enter Loan Amount").grid(row=0, column=1)
Label(root, text="Interest Rate per anum in %").grid(row=2, column=1)
Label(root, text="No of years").grid(row=4, column=1)
Label(root, text="Your EMI/month is").grid(row=6, column=1)
Label(root, text="Total Interest").grid(row=8, column=1)
Label(root, text="Payable Amount").grid(row=10, column=1)
Label(root, text="Enter no of months").grid(row=0, column=4)
Label(root, text="Months in years").grid(row=2, column=4)
principal = DoubleVar()
roi = DoubleVar()
noi = DoubleVar()
emi = DoubleVar()
total_interest = DoubleVar()
payable_amount = DoubleVar()
conv = DoubleVar()
conv1 = DoubleVar()
Entry(root, textvariable=principal).grid(row=0, column=3)
Entry(root, textvariable=roi).grid(row=2, column=3)
Entry(root, textvariable=noi).grid(row=4, column=3)
Entry(root, textvariable=emi).grid(row=6, column=3)
Entry(root, textvariable=total_interest).grid(row=8, column=3)
Entry(root, textvariable=payable_amount).grid(row=10, column=3)
Entry(root, textvariable=conv).grid(row=0, column=6)
Entry(root, textvariable=conv1).grid(row=2, column=6)
Button(root, text="Calculate", command=calculate).grid(row=13, column=1)
Button(root, text="Convert", command=conversion).grid(row=0, column=8)
Button(root, text="Print to pdf", command=printPdf).grid(row=16, column=5)

root.mainloop()