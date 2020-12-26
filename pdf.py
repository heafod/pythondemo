from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('pingbold', '/Users/hetao/Downloads/font/PingBold.ttf'))
pdfmetrics.registerFont(TTFont('ping', '/Users/hetao/Downloads/font/ping.ttf'))
pdfmetrics.registerFont(TTFont('hv', '/Users/hetao/Downloads/font/Helvetica.ttf'))

# 生成PDF文件
class PDFGenerator:
    def __init__(self, filename):
        self.filename = filename
        self.file_path = '/Users/hetao/Dev/Code/test/python3demo'
        self.title_style = ParagraphStyle(name="TitleStyle", fontName="pingbold", fontSize=48, alignment=TA_LEFT,)
        self.sub_title_style = ParagraphStyle(name="SubTitleStyle", fontName="hv", fontSize=32,
                                              textColor=colors.HexColor(0x666666), alignment=TA_LEFT, )
        self.content_style = ParagraphStyle(name="ContentStyle", fontName="ping", fontSize=18, leading=25, spaceAfter=20,
                                            underlineWidth=1, alignment=TA_LEFT, )
        self.foot_style = ParagraphStyle(name="FootStyle", fontName="ping", fontSize=14, textColor=colors.HexColor(0xB4B4B4),
                                         leading=25, spaceAfter=20, alignment=TA_CENTER, )
        self.table_title_style = ParagraphStyle(name="TableTitleStyle", fontName="pingbold", fontSize=20, leading=25,
                                                spaceAfter=10, alignment=TA_LEFT, )
        self.sub_table_style = ParagraphStyle(name="SubTableTitleStyle", fontName="ping", fontSize=16, leading=25,
                                                spaceAfter=10, alignment=TA_LEFT, )
        self.basic_style = TableStyle([('FONTNAME', (0, 0), (-1, -1), 'ping'),
                                       ('FONTSIZE', (0, 0), (-1, -1), 12),
                                       ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                                       ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                                       ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
                                       # 'SPAN' (列,行)坐标
                                       ('SPAN', (1, 0), (3, 0)),
                                       ('SPAN', (1, 1), (3, 1)),
                                       ('SPAN', (1, 2), (3, 2)),
                                       ('SPAN', (1, 5), (3, 5)),
                                       ('SPAN', (1, 6), (3, 6)),
                                       ('SPAN', (1, 7), (3, 7)),
                                       ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
                                       ])
        self.common_style = TableStyle([('FONTNAME', (0, 0), (-1, -1), 'ping'),
                                      ('FONTSIZE', (0, 0), (-1, -1), 12),
                                      ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                                      ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                                      ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
                                      ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
                                     ])

    def genTaskPDF(self, home_data, task_data, basic_data, case_set_data, fail_case_data, p0_case_data):
        story = []

        # 首页内容
        story.append(Spacer(1, 20 * mm))
        img = Image('/Users/hetao/Downloads/12.jpeg')
        img.drawHeight = 20 * mm
        img.drawWidth = 40 * mm
        img.hAlign = TA_LEFT
        story.append(img)
        story.append(Spacer(1, 10 * mm))
        story.append(Paragraph("测试报告", self.title_style))
        story.append(Spacer(1, 20 * mm))
        story.append(Paragraph("Test Report of XXX", self.sub_title_style))
        story.append(Spacer(1, 45 * mm))
        story.append(Paragraph("报告编号：" + home_data['report_code'], self.content_style))
        story.append(Paragraph("计划名称：" + home_data['task_name'], self.content_style))
        story.append(Paragraph("报告日期：" + home_data['report_date'], self.content_style))
        story.append(Paragraph(" 负责人：" + home_data['report_creator'], self.content_style))
        story.append(Spacer(1, 55 * mm))
        story.append(Paragraph("内部文档，请勿外传", self.foot_style))
        story.append(PageBreak())

        # 表格允许单元格内容自动换行格式设置
        stylesheet = getSampleStyleSheet()
        body_style = stylesheet["BodyText"]
        body_style.wordWrap = 'CJK'
        body_style.fontName = 'ping'
        body_style.fontSize = 12

        # 测试计划
        story.append(Paragraph("测试计划", self.table_title_style))
        story.append(Spacer(1, 3 * mm))
        task_table = Table(task_data, colWidths=[25 * mm, 141 * mm], rowHeights=12 * mm, style=self.common_style)
        story.append(task_table)

        story.append(Spacer(1, 10 * mm))

        # 基础参数
        story.append(Paragraph("基础参数", self.sub_table_style))
        basic_table = Table(basic_data, colWidths=[25*mm, 61*mm, 25*mm, 55*mm], rowHeights=12 * mm, style=self.basic_style)
        story.append(basic_table)

        story.append(Spacer(1, 10 * mm))

        # 测试用例集
        story.append(Paragraph("用例集参数", self.sub_table_style))
        case_set_table = Table(case_set_data, colWidths=[25 * mm, 141 * mm], rowHeights=12 * mm, style=self.common_style)
        story.append(case_set_table)

        # story.append(PageBreak())
        story.append(Spacer(1, 15 * mm))

        # 失败用例--使用可以自动换行的方式需要data里都是str类型的才OK
        story.append(Paragraph("失败用例", self.table_title_style))
        story.append(Spacer(1, 3 * mm))
        para_fail_case_data = [[Paragraph(cell, body_style) for cell in row] for row in fail_case_data]
        fail_case_table = Table(para_fail_case_data, colWidths=[20 * mm, 35 * mm, 91 * mm, 20 * mm])
        fail_case_table.setStyle(self.common_style)
        story.append(fail_case_table)

        story.append(Spacer(1, 15 * mm))

        # 基础用例（P0）
        story.append(Paragraph("基础用例（P0）", self.table_title_style))
        story.append(Spacer(1, 3 * mm))
        para_p0_case_data = [[Paragraph(cell, body_style) for cell in row] for row in p0_case_data]
        p0_case_table = Table(para_p0_case_data, colWidths=[20 * mm, 35 * mm, 91 * mm, 20 * mm])
        p0_case_table.setStyle(self.common_style)
        story.append(p0_case_table)

        doc = SimpleDocTemplate(self.file_path + self.filename + ".pdf",
                                leftMargin=20 * mm, rightMargin=20 * mm, topMargin=20 * mm, bottomMargin=20 * mm)


        doc.build(story)


if __name__ == "__main__":
    x = PDFGenerator("test")
    home_data = {
        "report_code": "0001",
        "task_name": "计划名称001",
        "report_date": "报告日期001",
        "report_creator": "负责人12"
    }
    task_data = [('计划ID', 16),('计划名称', "测试计划0812-Zoe"),('计划时间', "2019-08-11~2019-08-29")]
    basic_data = [('产品ID', 'xxxx'),
('设备ID', "xxx-nnn-001"),
('固件KEY', "001002"),
('固件版本', "2.1", "MCU版本", "3.5"),('APP版本', "2.1", "网关版本", "3.2")]
    case_set_data = [('任务名称1', '测试用例集1'),('任务名称2',"测试用例集2"),('任务名称3', "测试用例集23")]
    fail_case_data = [('任务名称1', '测试用例集1'),('任务名称2', "测试用例集2")]
    p0_case_data = [('任务名称1', '测试用例集1-1测试用例集1-1测试用例集1-1测试用例集1-1测试用例集1-1测试用例集1-1'), 
    ('任务名称2', "测试用例集2测试用例集2测试用例集2测试用例集2测试用例集2测试用例集2测试用例集2测试用例集2测试用例集2测试用例集2")]
    x.genTaskPDF(home_data, task_data, basic_data, case_set_data, fail_case_data, p0_case_data)