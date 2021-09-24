import io
import os
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, portrait, letter
from reportlab.pdfbase.pdfmetrics import registerFont
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, Spacer, PageBreak, SimpleDocTemplate, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors

from .models import User, Building, Gate, Device, Log

# 源真ゴシックのフォント登録
registerFont(TTFont('GenShinGothic', os.path.join(os.getcwd(), "gatechecker/fonts/GenShinGothic-Monospace-Normal.ttf")))


# POST: http://localhost:8000/gatechecker/report
def report(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    doc = SimpleDocTemplate(buffer, portrait=letter)

    elements = []

    cover_page(elements)

    user_table(elements)

    doc.build(elements)

    # FileResponse sets the Content-Disposition header so that browsers present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='report.pdf')


def cover_page(elements):

    title = "Gate-Checker レポート"
    title_style = ParagraphStyle('title_style',
                                 fontName="GenShinGothic",
                                 fontSize=32,
                                 alignment=1,
                                 spaceAfter=14)
    elements.append(Paragraph(title, title_style))

    elements.append(PageBreak())


def user_table(elements):

    # Title of User Table
    title = "エンドユーザー"
    title_style = ParagraphStyle('title_style',
                                 fontName="GenShinGothic",
                                 fontSize=24,
                                 alignment=1,
                                 spaceAfter=14)
    elements.append(Paragraph(title, title_style))

    # User Table
    heading = [["ユーザーID", "名称"]]
    users = []
    user_query = User.objects.all()
    for user in user_query:
        users.append([user.user_id, user.name])
    data = [*heading, *users]   # equal to heading + users

    table = Table(data, colWidths=(60*mm, 60*mm), rowHeights=12*mm, repeatRows=1)
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.cyan),
                               ('TEXTCOLOR', (0, 0), (0, -1), colors.red),
                               ('FONT', (0, 0), (-1, -1), "GenShinGothic", 14),
                               ('GRID', (0, 0), (-1, -1), 0.25, colors.black)]))
    elements.append(table)

    elements.append(Spacer(1, 10*mm))
