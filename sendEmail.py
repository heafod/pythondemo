from drymail import SMTPMailer, Message

from xlsx2html import xlsx2html

file_path = '/Users/hetao/Dev/Code/test/python3demo/CI系统-2020-11-17.xlsx'
out_stream = xlsx2html(file_path)
out_stream.seek(0)
html_msg = out_stream.read()

# 配置发件服务
client = SMTPMailer(host='mail.qq.com', user='test', password='', tls=False)
# 如果启用 ssl, 则会验证发件人  'Mail from must equal authorized user'
# 构造邮件
message = Message(subject='Congrats on the new job!', 
sender=('John Doe', 'noreplay@qq.com'),
                  receivers=[('张三', 'heafod@qq.com'), 'test@qq.com'], 
                #   cc=[('李四', 'test@qq.com')], # 抄送
                #   bcc=['test@qq.com'], # 密送
                  text='When is the party? ;)', # 纯文本
                #   html='<h1>Hello</h1>',  # html 优先
                  html=html_msg
                  )

# 构造附件
with open(file_path, 'rb') as pdf_file:
    message.attach(filename='CI系统-2020-11-17.xlsx', data=pdf_file.read())

client.send(message)
