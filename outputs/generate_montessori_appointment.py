#!/usr/bin/env python3
"""Generate Facilitie De Montessori School appointment letter PDF (2024)."""

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
    y -= 16
    c.setFont("Times-Italic", 11)
    c.setFillColor(ACCENT)
    c.drawCentredString(width / 2, y, "Orlando, Florida")

    y -= 12
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
        if "\u2014" in text or "\u2013" in text:
            raise ValueError("Em/en dash found in text")
        c.setFont(font, size)
        c.setFillColor(TEXT)
        for line in wrap(text, font, size):
            c.drawString(margin_x, yy, line)
            yy -= leading
        return yy - gap

    y -= 24
    c.setFillColor(TEXT)
    c.setFont("Helvetica", 10)
    c.drawString(margin_x, y, "August 5, 2024")

    y -= 20
    c.setFont("Helvetica-Bold", 10)
    c.drawString(margin_x, y, "Prabhjot Singh")
    y -= 12
    c.setFont("Helvetica", 10)
    c.drawString(margin_x, y, "Orlando, Florida")

    y -= 18
    c.setFont("Helvetica-Bold", 10)
    c.drawString(margin_x, y, "Subject: Appointment Letter - Science Teacher")

    y -= 18
    c.setFont("Helvetica", 10)
    c.drawString(margin_x, y, "Dear Mr. Prabhjot Singh,")
    y -= 14

    y = draw_para(
        "I am writing to confirm your appointment as Science Teacher at Facilitie De "
        "Montessori School in Orlando. Your start date is August 19, 2024.",
        y,
        leading=12.2,
        gap=5,
    )

    y = draw_para(
        "As Science Teacher, you will plan and teach science lessons for our students, "
        "keep accurate records of student work and progress, work with other teachers on "
        "classroom activities, and keep in regular contact with parents. You are also "
        "expected to follow school policies and help maintain a safe, orderly classroom.",
        y,
        leading=12.2,
        gap=5,
    )

    y = draw_para(
        "This is a full-time position for the 2024-2025 school year. The main terms are "
        "listed below. A separate employment agreement may also be provided for your "
        "signature.",
        y,
        leading=12.2,
        gap=4,
    )

    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(NAVY)
    c.drawString(margin_x, y, "Appointment Details")
    y -= 6
    c.setStrokeColor(RULE)
    c.setLineWidth(0.8)
    c.line(margin_x, y, margin_x + 120, y)
    y -= 13

    particulars = [
        ("Position Title", "Science Teacher"),
        ("School", "Facilitie De Montessori School, Orlando"),
        ("Employment Type", "Full-Time"),
        ("Start Date", "August 19, 2024"),
        ("School Year", "2024-2025"),
        ("Reports To", "Angelica Casta, Head of School"),
        ("Work Location", "Orlando, Florida"),
        ("Compensation", "As agreed in writing upon acceptance"),
        ("Probation Period", "90 days from the start date"),
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
        "This appointment is subject to completion of the usual pre-employment checks "
        "required for school staff in Florida, including a background check and "
        "confirmation of your teaching credentials.",
        y,
        size=9.5,
        leading=12,
        gap=4,
    )

    y = draw_para(
        "Please sign and return a copy of this letter by August 12, 2024 to confirm that "
        "you accept the position. We are glad to have you join our staff for the coming "
        "school year.",
        y,
        size=9.5,
        leading=12,
        gap=3,
    )

    c.setFont("Helvetica", 10)
    c.setFillColor(TEXT)
    c.drawString(margin_x, y, "Sincerely,")
    y -= 36
    c.setFont("Times-Italic", 12)
    c.setFillColor(TEXT)
    c.drawString(margin_x, y, "Angelica Casta")
    y -= 14
    c.setFont("Helvetica-Bold", 10)
    c.drawString(margin_x, y, "Angelica Casta")
    y -= 12
    c.setFont("Helvetica", 9)
    c.setFillColor(MUTED)
    c.drawString(margin_x, y, "Head of School")
    y -= 11
    c.drawString(margin_x, y, "Facilitie De Montessori School, Orlando, Florida")

    y -= 18
    c.setStrokeColor(NAVY)
    c.setLineWidth(0.55)
    c.line(margin_x, y, width - margin_x, y)
    y -= 14
    c.setFont("Helvetica-Bold", 9.5)
    c.setFillColor(NAVY)
    c.drawString(margin_x, y, "Acceptance of Appointment")
    y -= 12
    y = draw_para(
        "I, Prabhjot Singh, accept the appointment of Science Teacher at Facilitie De "
        "Montessori School, Orlando, on the terms stated in this letter.",
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
        width / 2, 0.32 * inch, "Facilitie De Montessori School  |  Orlando, Florida"
    )
    c.drawCentredString(width / 2, 0.20 * inch, "Page 1 of 1")
    c.save()


if __name__ == "__main__":
    out = (
        sys.argv[1]
        if len(sys.argv) > 1
        else os.path.join(
            os.path.dirname(__file__),
            "Facilitie_De_Montessori_Science_Teacher_Appointment_Prabhjot_Singh.pdf",
        )
    )
    os.makedirs(os.path.dirname(os.path.abspath(out)) or ".", exist_ok=True)
    build_pdf(out)
    print(f"Wrote {out}")
