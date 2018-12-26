import socialblip.config
import socialblip.data
import socialblip.blipfoto
import socialblip.facebook
import smtplib

class Engine:
    
    def __init__(self,  config_file_name,  data_dir_name):
        self.config = socialblip.config.Config(config_file_name)
        self.data = socialblip.data.Data(data_dir_name)
        self.blipfoto = socialblip.blipfoto.Blipfoto(self.config,  self.data)
        self.facebook = socialblip.facebook.Facebook(self.config,  self.data)
        
        
    def init(self):
        if self.data.has_been_inited():
            raise Exception('Already inited')
            
        self.data.init(self.blipfoto)
        

    def run(self):
        if not self.data.has_been_inited():
            raise Exception('Must init first')
            
        entries = self.blipfoto.get_entries()
        urls = []
        for entry in entries:
            (year, month,  day) = entry['date'].split("-")
            if not self.data.has_entry(year,  month,  day):
                urls.append(self.facebook.get_url(entry))
                self.data.create_entry(year,  month,  day)
        
        if urls:
            self._send_email(urls)
        
    def _send_email(self,  urls):
        email_text = "From: " +  self.config.config['email']['from'] + "\n"
        email_text += "To: " +  self.config.config['email']['to'] + "\n"
        email_text += "Subject: " +  self.config.config['email']['subject'] + "\n\n\n\n"
        for url in urls:
            email_text += url + "\n\n\n"
        
        server = smtplib.SMTP(self.config.config['email']['smtp_host'], self.config.config['email']['smtp_port'])
        server.ehlo()
        if self.config.config['email']['smtp_starttls']:
            server.starttls()
        server.login(self.config.config['email']['smtp_user'], self.config.config['email']['smtp_password'])
        server.sendmail(self.config.config['email']['from'],  self.config.config['email']['to'],  email_text)
        server.close()
            
