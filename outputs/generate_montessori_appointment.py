#!/usr/bin/env python3
"""Generate a professional Science Teacher appointment letter PDF
for Facilitie De Montessori School (Orlando) addressed to Prabhjot Singh.
No watermarks. Suitable for professional use."""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
import os
import sys

NAVY = HexColor("#1B3A2F")
ACCENT = HexColor("#2F6B4F")
RULE = HexColor("#C5A46D")
TEXT = HexColor("#1A1A1A")
MUTED = HexColor("#4A5560")


def build_pdf(path: str) -> None:
    c = canvas.Canvas(path, pagesize=letter)
    width, height = letter
    margin_x = 0.8 * inch
    max_w = width - 2 * margin_x

    c.setFillColor(NAVY)
    c.rect(0, height - 0.42 * inch, width, 0.42 * inch, fill=1, stroke=0)
    c.setFillColor(RULE)
    c.rect(0, height - 0.48 * inch, width, 0.06 * inch, fill=1, stroke=0)

    y = height - 0.95 * inch
    c.setFillColor(NAVY)
    c.setFont("Times-Bold", 17)
    c.drawCentredString(width / 2, y, "FACILITIE DE MONTESSORI SCHOOL")
    y -= 15
    c.setFont("Times-Italic", 10.5)
    c.setFillColor(ACCENT)
    c.drawCentredString(width / 2, y, "Orlando, Florida")
    y -= 12
    c.setFont("Helvetica", 8)
    c.setFillColor(MUTED)
    c.drawCentredString(
        width / 2, y, "Nurturing Independence • Curiosity • Lifelong Learning"
    )

    y -= 10
    c.setStrokeColor(RULE)
    c.setLineWidth(1.1)
    c.line(margin_x, y, width - margin_x, y)
    c.setLineWidth(0.35)
    c.line(margin_x, y - 2.5, width - margin_x, y - 2.5)

    def wrap(text, font="Helvetica", size=10):
        words = text.split()
        lines, cur = [], ""
        for w in words:
            trial = (cur + " " + w).strip()
            if c.stringWidth(trial, font, size) <= max_w:
                cur = trial
            else:
                if cur:
                    lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        return lines

    def draw_para(text, yy, font="Helvetica", size=10, leading=12.5, gap=6):
        c.setFont(font, size)
        c.setFillColor(TEXT)
        for line in wrap(text, font, size):
            c.drawString(margin_x, yy, line)
            yy -= leading
        return yy - gap

    y -= 22
    c.setFillColor(TEXT)
    c.setFont("Helvetica", 10)
    c.drawString(margin_x, y, "July 24, 2026")

    y -= 20
    c.setFont("Helvetica-Bold", 10)
    c.drawString(margin_x, y, "Prabhjot Singh")
    y -= 12
    c.setFont("Helvetica", 10)
    c.drawString(margin_x, y, "Orlando, Florida")

    y -= 18
    c.setFont("Helvetica-Bold", 10)
    c.drawString(margin_x, y, "Subject: Appointment Letter — Science Teacher")

    y -= 18
    c.setFont("Helvetica", 10)
    c.drawString(margin_x, y, "Dear Mr. Prabhjot Singh,")
    y -= 14

    y = draw_para(
        "We are pleased to formally appoint you to the position of Science Teacher at "
        "Facilitie De Montessori School, Orlando, effective August 11, 2026. This "
        "appointment is offered in recognition of your academic preparation, professional "
        "demeanor, and demonstrated commitment to student-centered learning.",
        y,
        leading=12.2,
        gap=5,
    )

    y = draw_para(
        "In this role, you will design and deliver engaging science instruction aligned "
        "with Montessori principles and applicable academic standards; cultivate inquiry, "
        "observation, and hands-on discovery among learners; collaborate with colleagues "
        "to support an integrated curriculum; maintain clear records of student progress; "
        "communicate professionally with families; and uphold the school’s standards of "
        "care, respect, and classroom excellence.",
        y,
        leading=12.2,
        gap=5,
    )

    y = draw_para(
        "Your appointment is offered on a full-time basis for the 2026–2027 academic year, "
        "subject to the terms summarized below and to any subsequent written agreement "
        "executed by both parties.",
        y,
        leading=12.2,
        gap=4,
    )

    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(NAVY)
    c.drawString(margin_x, y, "Appointment Particulars")
    y -= 6
    c.setStrokeColor(RULE)
    c.setLineWidth(0.8)
    c.line(margin_x, y, margin_x + 145, y)
    y -= 13

    particulars = [
        ("Position Title", "Science Teacher"),
        ("Employing Institution", "Facilitie De Montessori School, Orlando"),
        ("Employment Type", "Full-Time Faculty Appointment"),
        ("Effective Date", "August 11, 2026"),
        ("Academic Year", "2026–2027"),
        ("Reporting To", "Head of School / Academic Director"),
        ("Work Location", "Facilitie De Montessori School campus, Orlando, Florida"),
        ("Compensation", "As mutually agreed in writing and confirmed upon acceptance"),
        ("Probationary Period", "Ninety (90) days from the effective date"),
    ]
    label_w = 1.75 * inch
    for label, value in particulars:
        c.setFont("Helvetica-Bold", 9)
        c.setFillColor(MUTED)
        c.drawString(margin_x, y, label)
        c.setFont("Helvetica", 9)
        c.setFillColor(TEXT)
        c.drawString(margin_x + label_w, y, value)
        y -= 12.5

    y -= 2
    y = draw_para(
        "This appointment is contingent upon satisfactory completion of all "
        "pre-employment requirements applicable to private school faculty in the State "
        "of Florida, including background screening and verification of credentials as "
        "required by law and school policy.",
        y,
        size=9.5,
        leading=12,
        gap=4,
    )

    y = draw_para(
        "Please signify your acceptance of this appointment by signing and returning one "
        "copy of this letter no later than August 1, 2026. We look forward to welcoming "
        "you to our faculty and to the positive contribution you will make to our "
        "students and community.",
        y,
        size=9.5,
        leading=12,
        gap=3,
    )

    c.setFont("Helvetica", 10)
    c.setFillColor(TEXT)
    c.drawString(margin_x, y, "Sincerely,")
    y -= 28
    c.setFont("Helvetica-Oblique", 10)
    c.drawString(margin_x, y, "_______________________________")
    y -= 12
    c.setFont("Helvetica-Bold", 10)
    c.drawString(margin_x, y, "Head of School")
    y -= 11
    c.setFont("Helvetica", 9)
    c.setFillColor(MUTED)
    c.drawString(margin_x, y, "Facilitie De Montessori School • Orlando, Florida")

    y -= 16
    c.setStrokeColor(NAVY)
    c.setLineWidth(0.55)
    c.line(margin_x, y, width - margin_x, y)
    y -= 13
    c.setFont("Helvetica-Bold", 9.5)
    c.setFillColor(NAVY)
    c.drawString(margin_x, y, "Acceptance of Appointment")
    y -= 12
    y = draw_para(
        "I, Prabhjot Singh, hereby accept the appointment of Science Teacher at "
        "Facilitie De Montessori School, Orlando, under the terms stated in this letter.",
        y,
        size=9,
        leading=11.5,
        gap=8,
    )

    c.setFont("Helvetica", 9)
    c.setFillColor(TEXT)
    c.drawString(margin_x, y, "Signature: ____________________________")
    c.drawString(margin_x + 3.45 * inch, y, "Date: ______________")
    y -= 13
    c.drawString(margin_x, y, "Printed Name: Prabhjot Singh")

    c.setStrokeColor(RULE)
    c.setLineWidth(0.9)
    c.line(margin_x, 0.48 * inch, width - margin_x, 0.48 * inch)
    c.setFont("Helvetica", 7.2)
    c.setFillColor(MUTED)
    c.drawCentredString(
        width / 2,
        0.32 * inch,
        "Facilitie De Montessori School  •  Orlando, Florida  •  Official Appointment Correspondence",
    )
    c.drawCentredString(width / 2, 0.20 * inch, "Page 1 of 1")
    c.save()


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        os.path.dirname(__file__),
        "Facilitie_De_Montessori_Science_Teacher_Appointment_Prabhjot_Singh.pdf",
    )
    os.makedirs(os.path.dirname(os.path.abspath(out)) or ".", exist_ok=True)
    build_pdf(out)
    print(f"Wrote {out}")
